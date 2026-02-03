# PLEK2 Directory Structure Guide

## Overview
This document describes the recommended directory structure for PLEK2 after installation.

## Recommended Structure

### Option 1: Repository Structure (for development/manual installation)
```
plek2/
├── PLEK2.py                    # Main script
├── functions.py                # Helper functions
├── README.txt                  # Basic README
├── INSTALLATION.md             # Detailed installation guide
├── .gitignore                  # Git ignore file
├── conda-recipe/               # Conda recipe for building package
│   ├── meta.yaml
│   └── build.sh
├── utils/                      # Models directory (create this)
│   ├── Coding_Net_kmer6_orf.h5
│   └── Coding_Net_kmer6_orf_Arabidopsis.h5
└── test_data/                  # Optional: test datasets
    ├── PLEK2_test.fa
    ├── PLEK2_test_lncrna.fa
    └── PLEK2_test_mrna.fa
```

### Option 2: Scripts in Subdirectory (recommended for organized installations)
```
plek2/
├── scripts/
│   ├── PLEK2.py                # Main script
│   └── functions.py            # Helper functions
├── utils/                      # Models directory (one level up from scripts)
│   ├── Coding_Net_kmer6_orf.h5
│   └── Coding_Net_kmer6_orf_Arabidopsis.h5
├── README.txt
├── INSTALLATION.md
└── conda-recipe/
    ├── meta.yaml
    └── build.sh
```

### Option 3: System-wide Installation
```
/opt/plek2/                     # Or any system directory
├── scripts/
│   ├── PLEK2.py
│   └── functions.py
└── utils/
    ├── Coding_Net_kmer6_orf.h5
    └── Coding_Net_kmer6_orf_Arabidopsis.h5

/usr/local/bin/plek2            # Symlink to /opt/plek2/scripts/PLEK2.py
```

### Option 4: Conda Installation
```
$CONDA_PREFIX/                  # Your conda environment
├── bin/
│   └── plek2                   # Executable wrapper
└── share/
    └── plek2/
        ├── functions.py
        └── utils/              # Models go here
            ├── Coding_Net_kmer6_orf.h5
            └── Coding_Net_kmer6_orf_Arabidopsis.h5
```

## Important Notes

### Model File Location
The scripts look for model files in the `utils/` directory, which should be **one directory level up** from where the scripts are located.

For example:
- If `PLEK2.py` is in `/path/to/scripts/`, models should be in `/path/to/utils/`
- If `PLEK2.py` is in `/path/to/plek2/`, models should be in `/path/to/plek2/utils/`

### Output Files Location
When you run PLEK2 with an output prefix, all output files will be created using that prefix:

```bash
# Example 1: Output in current directory
python PLEK2.py -i input.fa -m ve -o myresults

# Creates:
# - myresults_scores.txt
# - myresults_noncoding.txt
# - myresults_stats.txt
# - myresults_kmer_seqs
# - myresults_kmer_6.txt
# - myresults_orf_length.txt
# - myresults_features.txt
# - ... and other intermediate files

# Example 2: Output in subdirectory
python PLEK2.py -i input.fa -m ve -o results/experiment1/sample1

# Creates results/experiment1/ directory and files:
# - results/experiment1/sample1_scores.txt
# - results/experiment1/sample1_noncoding.txt
# - results/experiment1/sample1_stats.txt
# - ... etc.
```

## Setup Instructions

### Method 1: Clone and Create Structure

```bash
# Clone repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Create utils directory
mkdir -p utils

# Download and extract models
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz
tar -xzf PLEK2_model_v3.tar.gz
cd PLEK2_model_v3
bunzip2 Coding_Net_kmer6_orf.h5.bz2
bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2

# Move models to utils
mv *.h5 ../utils/
cd ..

# Test installation
python PLEK2.py -h
```

### Method 2: Organize into Scripts Directory

```bash
# Clone repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Create directory structure
mkdir -p scripts utils

# Move scripts
mv PLEK2.py functions.py scripts/

# Download and extract models (as above)
# ... then move to utils/

# Add to PATH or create alias
export PATH="$PWD/scripts:$PATH"
```

### Method 3: System Installation

```bash
# Create installation directory
sudo mkdir -p /opt/plek2/scripts /opt/plek2/utils

# Copy files
sudo cp PLEK2.py functions.py /opt/plek2/scripts/

# Download and install models to /opt/plek2/utils/

# Create system-wide command
sudo ln -s /opt/plek2/scripts/PLEK2.py /usr/local/bin/plek2
sudo chmod +x /opt/plek2/scripts/PLEK2.py

# Add Python shebang to script if needed
```

## Verifying Installation

Check that the directory structure is correct:

```bash
# Check scripts location
ls -l PLEK2.py functions.py

# Check utils directory (should be one level up from scripts)
ls -l utils/*.h5

# Or if using scripts subdirectory
ls -l scripts/PLEK2.py scripts/functions.py
ls -l utils/*.h5
```

The key is ensuring that when `functions.py` looks for models in `../utils/` relative to its location, it can find them.

## Testing

Once installed, test with the provided test data:

```bash
# Create output directory
mkdir -p test_output

# Run test
python PLEK2.py -i PLEK2_test.fa -m ve -o test_output/test

# Check outputs
ls -l test_output/test_*.txt
cat test_output/test_stats.txt
```

Expected output files:
- `test_output/test_scores.txt` - Detailed predictions for each sequence
- `test_output/test_noncoding.txt` - List of non-coding sequences
- `test_output/test_stats.txt` - Summary statistics
- Plus intermediate files with `test_output/test_*` prefix

## Troubleshooting

### "Model file not found" error
- Verify models are in `utils/` directory
- Check file names are exact: `Coding_Net_kmer6_orf.h5` and `Coding_Net_kmer6_orf_Arabidopsis.h5`
- Ensure models are decompressed (not .bz2)
- Verify relative path: utils should be `../utils/` from script location

### Permission denied
- Check file permissions: `chmod +x PLEK2.py`
- Check directory permissions for output directory

### Import errors
- Install all required dependencies
- Use Python 3.8 or higher
- Consider using a conda environment
