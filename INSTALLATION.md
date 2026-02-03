# PLEK2 Installation Guide

## Overview
PLEK2 is a tool for predicting long non-coding RNAs (lncRNAs) and messenger RNAs (mRNAs) based on sequence intrinsic features and a Coding-Net model.

## Repository Structure

```
plek2/
├── bin/                      # Python scripts
│   ├── PLEK2.py             # Main script
│   └── functions.py         # Helper functions
├── test/                     # Test data
│   ├── PLEK2_test.fa
│   ├── PLEK2_test_lncrna.fa
│   └── PLEK2_test_mrna.fa
├── utils/                    # Model files (download separately)
│   ├── Coding_Net_kmer6_orf.h5              # Vertebrate model
│   ├── Coding_Net_kmer6_orf_Arabidopsis.h5  # Plant model
│   └── README.md
├── setup.sh                  # Automated setup script
├── INSTALLATION.md          # This file
└── README.txt

```

## Quick Start (Automated Setup)

The easiest way to set up PLEK2 is using the provided setup script:

```bash
# Clone the repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Run automated setup
./setup.sh
```

This script will:
1. Create a conda environment named "PLEK2" with all dependencies
2. Download model files from SourceForge
3. Copy bin/ and utils/ contents to the conda environment

## Manual Installation

### Method 1: Conda Environment Setup (Recommended)

#### Step 1: Create Conda Environment

```bash
# Create conda environment named PLEK2 with all dependencies
conda create -n PLEK2 -y -c conda-forge \
    python=3.8.5 \
    numpy=1.19.2 \
    pandas \
    biopython \
    keras=2.4.3 \
    tensorflow=2.4.1 \
    regex

# Activate the environment
conda activate PLEK2
```

#### Step 2: Clone Repository

```bash
git clone https://github.com/AHinsu/plek2.git
cd plek2
```

#### Step 3: Download and Extract Models

```bash
# Navigate to utils directory
cd utils

# Download model files from SourceForge
wget -O PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEKv2_allfiles_240807.tar.gz

# Or using curl if wget is not available:
# curl -L -o PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEKv2_allfiles_240807.tar.gz

# Extract the archive
tar -xzf PLEK2_model_v3.tar.gz

# Decompress the model files
bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf.h5.bz2
bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf_Arabidopsis.h5.bz2

# Move model files to utils directory
mv PLEK2_model_v3/*.h5 .

# Clean up
rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz

# Return to repository root
cd ..
```

#### Step 4: Copy Files to Conda Environment

```bash
# Get the conda environment path
CONDA_PREFIX=$(conda info --envs | grep "^PLEK2 " | awk '{print $NF}')

# Copy scripts to conda environment bin
cp bin/PLEK2.py $CONDA_PREFIX/bin/
cp bin/functions.py $CONDA_PREFIX/bin/

# Copy models to conda environment utils
mkdir -p $CONDA_PREFIX/utils
cp utils/*.h5 $CONDA_PREFIX/utils/

# Scripts are already executable - verify permissions
ls -l $CONDA_PREFIX/bin/PLEK2.py
```

#### Step 5: Verify Installation

```bash
# Activate the environment
conda activate PLEK2

# Test with sample data - direct execution
bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o test_output

# Or from conda environment bin
PLEK2.py -i test/PLEK2_test.fa -m ve -o test_output

# Or with explicit Python interpreter
python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o test_output
```

### Method 2: Using from Repository Directory

If you prefer to run PLEK2 directly from the cloned repository:

```bash
# Clone the repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Create conda environment with all dependencies
conda create -n PLEK2 -y -c conda-forge \
    python=3.8.5 \
    numpy=1.19.2 \
    pandas \
    biopython \
    keras=2.4.3 \
    tensorflow=2.4.1 \
    regex

# Activate the environment
conda activate PLEK2

# Download and extract models to utils/ directory
cd utils
wget -O PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEKv2_allfiles_240807.tar.gz
tar -xzf PLEK2_model_v3.tar.gz
bunzip2 PLEK2_model_v3/*.bz2
mv PLEK2_model_v3/*.h5 .
rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz
cd ..

# Run directly from repository
bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test

# Or with explicit Python interpreter
python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test
```

## Requirements

### System Requirements
- Linux or macOS operating system
- Python >= 3.8
- At least 4GB RAM
- ~2GB disk space for model files

### Python Dependencies

All dependencies are installed via conda from the conda-forge channel:

- python = 3.8.5
- numpy = 1.19.2
- pandas
- keras = 2.4.3
- tensorflow = 2.4.1
- biopython >= 1.3.2
- regex

**Note:** The installation commands use the `-c conda-forge` flag to ensure all packages are available. This channel provides the most comprehensive package coverage including keras, tensorflow, and regex.

## Detailed Setup Commands

### Creating Conda Environment "PLEK2"

Complete command sequence to create and set up the conda environment:

```bash
# 1. Create conda environment with all dependencies
conda create -n PLEK2 -y -c conda-forge \
    python=3.8.5 \
    numpy=1.19.2 \
    pandas \
    biopython \
    keras=2.4.3 \
    tensorflow=2.4.1 \
    regex

# 2. Activate environment
conda activate PLEK2

# 3. Verify installation
python -c "import numpy, pandas, keras, tensorflow, Bio, regex; print('All dependencies installed successfully')"
```

### Downloading Models from SourceForge

```bash
# Navigate to utils directory in repository
cd plek2/utils

# Download using wget (Linux/macOS with wget)
wget -O PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEKv2_allfiles_240807.tar.gz

# OR download using curl (macOS default)
curl -L -o PLEK2_model_v3.tar.gz https://sourceforge.net/projects/plek2/files/PLEKv2_allfiles_240807.tar.gz

# Extract archive
tar -xzf PLEK2_model_v3.tar.gz

# Decompress model files (they are compressed with bzip2)
bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf.h5.bz2
bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf_Arabidopsis.h5.bz2

# Move models to utils directory
mv PLEK2_model_v3/*.h5 .

# Verify models are in place
ls -lh *.h5

# Clean up downloaded files
rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz
```

### Copying to Conda Environment

After downloading models and setting up the conda environment:

```bash
# Activate PLEK2 environment
conda activate PLEK2

# Get conda environment path
CONDA_ENV=$(conda info --envs | grep "^PLEK2 " | awk '{print $NF}')

# Or use the automatic variable when environment is activated
CONDA_ENV=$CONDA_PREFIX

# Copy bin directory contents
mkdir -p $CONDA_ENV/bin
cp bin/PLEK2.py $CONDA_ENV/bin/
cp bin/functions.py $CONDA_ENV/bin/

# Scripts are already executable - verify permissions
ls -l $CONDA_ENV/bin/PLEK2.py

# Copy utils directory contents  
mkdir -p $CONDA_ENV/utils
cp utils/*.h5 $CONDA_ENV/utils/

# Verify files are copied
ls -l $CONDA_ENV/bin/PLEK2.py
ls -l $CONDA_ENV/utils/*.h5
```

## Usage

### Basic Usage

```bash
# Activate conda environment (if using conda)
conda activate PLEK2

# Run directly from repository
bin/PLEK2.py -i input.fasta -m ve -o output_prefix

# Run from conda environment
PLEK2.py -i input.fasta -m ve -o output_prefix

# Or with explicit Python interpreter
python bin/PLEK2.py -i input.fasta -m ve -o output_prefix
```

### Parameters

- `-i, --input_file`: Input file in FASTA format (required)
- `-m, --model`: Model type - 've' for vertebrate, 'pl' for plant (required)
- `-o, --output`: Output file prefix, can include directory names (required)

### Examples

```bash
# Example 1: Using vertebrate model
conda activate PLEK2
bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/vertebrate_test

# Example 2: Using plant model with output in specific directory
bin/PLEK2.py -i my_sequences.fa -m pl -o output/plant_analysis/sample1

# Example 3: Running from conda environment bin
conda activate PLEK2
PLEK2.py -i input.fa -m ve -o results/test
```

### Output Files

PLEK2 generates three main output files:

1. **`<prefix>_scores.txt`**: Contains sequence names, classification (Coding/Non-coding), and scores
2. **`<prefix>_noncoding.txt`**: List of sequence names classified as non-coding
3. **`<prefix>_stats.txt`**: Summary statistics including:
   - Total input sequences
   - Number and percentage of coding sequences
   - Number and percentage of non-coding sequences

### Intermediate Files

Intermediate files are kept for debugging and analysis:
- `<prefix>_kmer_seqs`: Processed k-mer sequences
- `<prefix>_kmer_6.txt`: K-mer features
- `<prefix>_orf_length.txt`: ORF length features
- `<prefix>_features.txt`: Combined features
- And various other processing files

## Directory Structure After Installation

### Repository Structure
```
plek2/
├── bin/
│   ├── PLEK2.py
│   └── functions.py
├── test/
│   ├── PLEK2_test.fa
│   ├── PLEK2_test_lncrna.fa
│   └── PLEK2_test_mrna.fa
├── utils/
│   ├── Coding_Net_kmer6_orf.h5
│   ├── Coding_Net_kmer6_orf_Arabidopsis.h5
│   └── README.md
└── setup.sh
```

### Conda Environment Structure
```
$CONDA_PREFIX/  (e.g., ~/miniconda3/envs/PLEK2/)
├── bin/
│   ├── PLEK2.py
│   ├── functions.py
│   ├── python
│   └── ...
├── utils/
│   ├── Coding_Net_kmer6_orf.h5
│   └── Coding_Net_kmer6_orf_Arabidopsis.h5
└── lib/
    └── python3.8/
        └── site-packages/
            ├── numpy/
            ├── pandas/
            ├── keras/
            └── ...
```

## Troubleshooting

### Models not found error

If you get an error about models not being found:
1. Verify models are in the `utils/` directory (repository) or `$CONDA_PREFIX/utils/` (conda env)
2. Check that models are decompressed (not .bz2 files)
3. Verify file names are exactly: `Coding_Net_kmer6_orf.h5` and `Coding_Net_kmer6_orf_Arabidopsis.h5`
4. Check the path: models should be in `../utils/` relative to where functions.py is located

### Import errors

If you get import errors:
1. Ensure the PLEK2 conda environment is activated: `conda activate PLEK2`
2. Verify all dependencies are installed: `conda list | grep -E "numpy|pandas|keras|tensorflow"`
3. Check Python version: `python --version` (should be 3.8.x)

### Download issues

If model download fails:
1. Try using curl instead of wget, or vice versa
2. Download manually from browser: https://sourceforge.net/projects/plek2/files/
3. Check internet connection and firewall settings
4. Verify SourceForge is accessible from your network

### Permission errors

If you get permission errors when copying to conda environment:
1. Ensure you have write permissions to the conda environment
2. Don't use `sudo` with conda commands
3. Check conda environment ownership: `ls -ld $CONDA_PREFIX`

## Testing Installation

After installation, test with the provided sample data:

```bash
# Activate environment
conda activate PLEK2

# Create output directory
mkdir -p test_results

# Run test
python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o test_results/test

# Or run directly (scripts are executable)
bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o test_results/test

# Check outputs
ls -lh test_results/test_*.txt
cat test_results/test_stats.txt
```

Expected output:
- `test_results/test_scores.txt` - Detailed predictions
- `test_results/test_noncoding.txt` - Non-coding sequence list  
- `test_results/test_stats.txt` - Summary statistics


