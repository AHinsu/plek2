# PLEK2 Installation Guide

## Overview
PLEK2 is a tool for predicting long non-coding RNAs (lncRNAs) and messenger RNAs (mRNAs) based on sequence intrinsic features and a Coding-Net model.

## Installation Methods

### Method 1: Conda Installation (Recommended)

#### Step 1: Build and Install via Conda

```bash
# Clone the repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Build the conda package
conda build conda-recipe

# Install the package
conda install --use-local plek2
```

#### Step 2: Download and Install Models

The model files are too large to include in the conda package and must be downloaded separately:

```bash
# Download model files from SourceForge
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz

# Extract the archive
tar -xzf PLEK2_model_v3.tar.gz

# Decompress the models
cd PLEK2_model_v3
bunzip2 Coding_Net_kmer6_orf.h5.bz2
bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2

# Find your conda installation prefix
CONDA_PREFIX=$(conda info --base)
INSTALL_PREFIX="$CONDA_PREFIX/envs/YOUR_ENV_NAME"  # Or just $CONDA_PREFIX if in base

# Copy models to the utils directory
mkdir -p $INSTALL_PREFIX/share/plek2/utils
cp Coding_Net_kmer6_orf.h5 $INSTALL_PREFIX/share/plek2/utils/
cp Coding_Net_kmer6_orf_Arabidopsis.h5 $INSTALL_PREFIX/share/plek2/utils/
```

### Method 2: Manual Installation with Symlinks

#### Step 1: Clone the Repository

```bash
git clone https://github.com/AHinsu/plek2.git
cd plek2
```

#### Step 2: Create Directory Structure

```bash
# Create a directory for installation (e.g., in your home directory)
mkdir -p ~/plek2_install/scripts
mkdir -p ~/plek2_install/utils

# Copy scripts to the scripts directory
cp PLEK2.py ~/plek2_install/scripts/
cp functions.py ~/plek2_install/scripts/
```

#### Step 3: Download and Install Models

```bash
# Download model files
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz
tar -xzf PLEK2_model_v3.tar.gz

# Decompress models
cd PLEK2_model_v3
bunzip2 Coding_Net_kmer6_orf.h5.bz2
bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2

# Copy models to utils directory
cp Coding_Net_kmer6_orf.h5 ~/plek2_install/utils/
cp Coding_Net_kmer6_orf_Arabidopsis.h5 ~/plek2_install/utils/
```

#### Step 4: Create Symlinks (Optional)

If you prefer to keep files in the cloned repository:

```bash
# Create scripts directory
mkdir -p scripts
mv PLEK2.py scripts/
mv functions.py scripts/

# Create utils directory and add models
mkdir -p utils
cp PLEK2_model_v3/Coding_Net_kmer6_orf.h5 utils/
cp PLEK2_model_v3/Coding_Net_kmer6_orf_Arabidopsis.h5 utils/

# Make script executable
chmod +x scripts/PLEK2.py
```

#### Step 5: Add to PATH

Add the scripts directory to your PATH:

```bash
# Add to ~/.bashrc or ~/.bash_profile
echo 'export PATH="$HOME/plek2_install/scripts:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Or create an alias
echo 'alias plek2="python $HOME/plek2_install/scripts/PLEK2.py"' >> ~/.bashrc
source ~/.bashrc
```

### Method 3: Permanent Installation (Move Files)

Instead of creating symlinks, you can permanently move the files:

```bash
# Clone and setup
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Create installation directory
sudo mkdir -p /opt/plek2/scripts
sudo mkdir -p /opt/plek2/utils

# Move files
sudo cp PLEK2.py /opt/plek2/scripts/
sudo cp functions.py /opt/plek2/scripts/

# Download and install models
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz
tar -xzf PLEK2_model_v3.tar.gz
cd PLEK2_model_v3
bunzip2 Coding_Net_kmer6_orf.h5.bz2
bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2
sudo cp Coding_Net_kmer6_orf.h5 /opt/plek2/utils/
sudo cp Coding_Net_kmer6_orf_Arabidopsis.h5 /opt/plek2/utils/

# Create symlink in /usr/local/bin
sudo ln -s /opt/plek2/scripts/PLEK2.py /usr/local/bin/plek2
sudo chmod +x /opt/plek2/scripts/PLEK2.py
```

## Requirements

- Python >= 3.8
- numpy == 1.19.2
- pandas
- keras == 2.4.3
- tensorflow == 2.4.1
- biopython >= 1.3.2
- regex

### Installing Dependencies

If not using conda:

```bash
pip install numpy==1.19.2
pip install pandas
pip install keras==2.4.3
pip install tensorflow==2.4.1
pip install biopython
pip install regex
```

## Usage

```bash
# Basic usage
python PLEK2.py -i input.fasta -m ve -o output_prefix

# With output in a specific directory
python PLEK2.py -i input.fasta -m ve -o results/sample1

# Using plant model
python PLEK2.py -i input.fasta -m pl -o output_prefix
```

### Parameters

- `-i, --input_file`: Input file in FASTA format (required)
- `-m, --model`: Model type - 've' for vertebrate, 'pl' for plant (required)
- `-o, --output`: Output file prefix, can include directory names (required)

### Output Files

PLEK2 now generates three main output files:

1. **`<prefix>_scores.txt`**: Contains sequence names, classification (Coding/Non-coding), and scores
2. **`<prefix>_noncoding.txt`**: List of sequence names classified as non-coding
3. **`<prefix>_stats.txt`**: Summary statistics including:
   - Total input sequences
   - Number and percentage of coding sequences
   - Number and percentage of non-coding sequences

### Intermediate Files

Intermediate files are now kept with the output prefix for debugging and analysis:
- `<prefix>_kmer_seqs`: Processed k-mer sequences
- `<prefix>_kmer_6.txt`: K-mer features
- `<prefix>_orf_length.txt`: ORF length features
- `<prefix>_features.txt`: Combined features
- And various other processing files

## Example

```bash
# Run PLEK2 on test data
python PLEK2.py -i PLEK2_test.fa -m ve -o test_results/plek2_test

# This will create:
# - test_results/plek2_test_scores.txt
# - test_results/plek2_test_noncoding.txt
# - test_results/plek2_test_stats.txt
# - Plus intermediate files in test_results/
```

## Directory Structure

After installation, the directory structure should be:

```
plek2/
├── scripts/
│   ├── PLEK2.py
│   └── functions.py
└── utils/
    ├── Coding_Net_kmer6_orf.h5
    └── Coding_Net_kmer6_orf_Arabidopsis.h5
```

Or for conda installation:

```
$CONDA_PREFIX/
├── bin/
│   └── plek2
└── share/
    └── plek2/
        ├── functions.py
        └── utils/
            ├── Coding_Net_kmer6_orf.h5
            └── Coding_Net_kmer6_orf_Arabidopsis.h5
```

## Troubleshooting

### Models not found error

If you get an error about models not being found:
1. Verify models are in the `utils` directory
2. Check that the utils directory is one level up from the scripts directory
3. Ensure models are decompressed (not .bz2 files)

### Import errors

If you get import errors:
1. Check that all dependencies are installed
2. Verify you're using Python >= 3.8
3. Try creating a new conda environment

## Support

For issues and questions:
- GitHub: https://github.com/AHinsu/plek2
- Email: emanlee815@163.com

## Citation

If you use PLEK2 in your research, please cite:
[Add citation information here]
