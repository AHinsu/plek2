#!/bin/bash
# PLEK2 Setup Script
# This script sets up PLEK2 with conda environment and downloads required models

set -e  # Exit on error

echo "================================================"
echo "PLEK2 Setup Script"
echo "================================================"
echo ""

# Function to check if conda is available
check_conda() {
    if ! command -v conda &> /dev/null; then
        echo "Error: conda is not installed or not in PATH"
        echo "Please install Miniconda or Anaconda first:"
        echo "  https://docs.conda.io/en/latest/miniconda.html"
        exit 1
    fi
    echo "✓ Conda found: $(conda --version)"
}

# Function to create conda environment
create_conda_env() {
    echo ""
    echo "Creating conda environment 'PLEK2'..."
    
    # Check if environment already exists
    if conda env list | grep -q "^PLEK2 "; then
        echo "Warning: Environment 'PLEK2' already exists."
        read -p "Do you want to remove and recreate it? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            conda env remove -n PLEK2 -y
        else
            echo "Skipping environment creation. Using existing environment."
            return
        fi
    fi
    
    # Create environment with all dependencies via conda
    conda create -n PLEK2 -y -c conda-forge \
        python=3.8.5 \
        numpy=1.19.2 \
        pandas \
        biopython \
        keras=2.4.3 \
        tensorflow=2.4.1 \
        regex
    
    echo "✓ Conda environment 'PLEK2' created successfully"
}

# Function to download models
download_models() {
    echo ""
    echo "Downloading model files from SourceForge..."
    
    cd utils
    
    # Check if models already exist
    if [ -f "Coding_Net_kmer6_orf.h5" ] && [ -f "Coding_Net_kmer6_orf_Arabidopsis.h5" ]; then
        echo "Models already exist in utils/ directory."
        read -p "Do you want to re-download them? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Skipping model download."
            cd ..
            return
        fi
    fi
    
    # Download model archive
    if command -v wget &> /dev/null; then
        wget -O PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz/download
    elif command -v curl &> /dev/null; then
        curl -L -o PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz/download
    else
        echo "Error: Neither wget nor curl is available."
        echo "Please download manually from: https://sourceforge.net/projects/plek2/files/"
        cd ..
        return 1
    fi
    
    # Extract archive
    echo "Extracting model archive..."
    tar -xzf PLEK2_model_v3.tar.gz
    
    # Decompress models
    echo "Decompressing model files..."
    bunzip2 -f PLEK2_model_v3/Coding_Net_kmer6_orf.h5.bz2
    bunzip2 -f PLEK2_model_v3/Coding_Net_kmer6_orf_Arabidopsis.h5.bz2
    
    # Move models to utils directory
    mv PLEK2_model_v3/*.h5 .
    
    # Clean up
    rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz
    
    echo "✓ Model files downloaded and extracted successfully"
    cd ..
}

# Function to copy files to conda environment
copy_to_conda_env() {
    echo ""
    echo "Copying PLEK2 files to conda environment..."
    
    # Get conda environment path
    source $(conda info --base)/etc/profile.d/conda.sh
    conda activate PLEK2
    CONDA_ENV_PATH=$(conda info --envs | grep "^PLEK2 " | awk '{print $NF}')
    
    if [ -z "$CONDA_ENV_PATH" ]; then
        echo "Error: Could not find PLEK2 conda environment path"
        exit 1
    fi
    
    echo "Installing to: $CONDA_ENV_PATH"
    
    # Create directories
    mkdir -p "$CONDA_ENV_PATH/bin"
    mkdir -p "$CONDA_ENV_PATH/utils"
    
    # Copy bin files
    echo "Copying scripts to $CONDA_ENV_PATH/bin..."
    cp bin/PLEK2.py "$CONDA_ENV_PATH/bin/"
    cp bin/functions.py "$CONDA_ENV_PATH/bin/"
    
    # Scripts are already executable - verify permissions
    ls -l "$CONDA_ENV_PATH/bin/PLEK2.py"
    
    # Copy utils files (models)
    if [ -f "utils/Coding_Net_kmer6_orf.h5" ]; then
        echo "Copying model files to $CONDA_ENV_PATH/utils..."
        cp utils/*.h5 "$CONDA_ENV_PATH/utils/" 2>/dev/null || true
    else
        echo "Warning: Model files not found in utils/ directory"
        echo "You'll need to download them manually and place in $CONDA_ENV_PATH/utils/"
    fi
    
    echo "✓ Files copied to conda environment successfully"
}

# Main execution
main() {
    # Get repository root
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    cd "$SCRIPT_DIR"
    
    echo "Working directory: $(pwd)"
    echo ""
    
    # Step 1: Check conda
    check_conda
    
    # Step 2: Create conda environment
    read -p "Create conda environment 'PLEK2' with dependencies? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        create_conda_env
    else
        echo "Skipping conda environment creation."
    fi
    
    # Step 3: Download models
    read -p "Download model files from SourceForge? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        download_models
    else
        echo "Skipping model download."
        echo "You can download manually later - see utils/README.md for instructions"
    fi
    
    # Step 4: Copy to conda environment
    read -p "Copy bin/ and utils/ to conda environment 'PLEK2'? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        copy_to_conda_env
    else
        echo "Skipping file copy to conda environment."
    fi
    
    echo ""
    echo "================================================"
    echo "Setup complete!"
    echo "================================================"
    echo ""
    echo "To use PLEK2:"
    echo "  1. Activate the environment: conda activate PLEK2"
    echo "  2. Run PLEK2 directly: PLEK2.py -i input.fa -m ve -o output"
    echo ""
    echo "Or from this directory:"
    echo "  conda activate PLEK2"
    echo "  bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test"
    echo ""
    echo "Or with explicit Python interpreter:"
    echo "  python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test"
    echo ""
    echo "For more information, see INSTALLATION.md"
    echo ""
}

# Run main function
main
