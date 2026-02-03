# This repository contains modified code from the original sourcecode hosted at https://sourceforge.net/projects/plek2/files/
The purpose of this repository is to make working with PLEKv2 easier and more user-friendly. 
For any queries related to working of the tool and models, please contact the original authors given below.

Haotian Zhou, Master
School of Computer Science and Engineering,
Xi'an University of Technology,
5 South Jinhua Road,
Xi'an, Shaanxi 710048, P.R China


Aimin Li, PhD
School of Computer Science and Engineering,
Xi'an University of Technology,
5 South Jinhua Road,
Xi'an, Shaanxi 710048, P.R China


liaiminmail AT gmail.com

emanlee815 AT 163.com


Please see and cite the original publication at https://pmc.ncbi.nlm.nih.gov/articles/PMC11295476/
===========================================================
PLEK2: a novel method for predicting lncRNA and mRNA based on sequence intrinsic features and Coding-Net model (Upgraded version of PLEK)
===========================================================


LncRNA participates in many important regulatory activities of organisms. Its biological structure is similar to messenger RNA (mRNA), in order to distinguish between lncRNA and mRNA (messenger RNA) transcripts more quickly and accurately, we upgraded the alignment-free PLEK to PLEK2.

Requirements
------------
+ [Linux]
+ [Python version > = 3.8.5] (http://www.python.org/)
+ regex package
+ keras==2.4.3 package
+ pandas package
+ tensorflow==2.4.1 package
+ bio version >= 1.3.2 package
+ numpy package
--------------------------------------------------

# PLEK2 Quick Start Guide

## Automated Setup (Easiest)

```bash
# 1. Clone repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# 2. Run setup script
./setup.sh
```

The setup script will:
- Create conda environment "PLEK2" with all dependencies
- Download models from SourceForge
- Copy files to conda environment

## Manual Setup (Step by Step)

### 1. Create Conda Environment

```bash
# Create environment with all dependencies via conda
conda create -n PLEK2 -y -c conda-forge \
    python=3.8.5 \
    numpy=1.19.2 \
    pandas \
    biopython \
    keras=2.4.3 \
    tensorflow=2.4.1 \
    regex

# Activate environment
conda activate PLEK2
```

### 2. Clone Repository

```bash
git clone https://github.com/AHinsu/plek2.git
cd plek2
```

### 3. Download Models

```bash
# Navigate to utils directory
cd utils

# Download from SourceForge
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz

# Extract and decompress
tar -xzf PLEK2_model_v3.tar.gz
bunzip2 PLEK2_model_v3/*.bz2
mv PLEK2_model_v3/*.h5 .
rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz

cd ..
```

### 4. Copy to Conda Environment

```bash
# Copy scripts and models
conda activate PLEK2
cp bin/*.py $CONDA_PREFIX/bin/
mkdir -p $CONDA_PREFIX/utils
cp utils/*.h5 $CONDA_PREFIX/utils/
```

## Usage

```bash
# Activate conda environment
conda activate PLEK2

# Run from repository
bin/PLEK2.py -i INPUT.fa -m MODEL -o OUTPUT_PREFIX

# Or from conda environment bin
PLEK2.py -i INPUT.fa -m MODEL -o OUTPUT_PREFIX

# Or with explicit Python interpreter
python bin/PLEK2.py -i INPUT.fa -m MODEL -o OUTPUT_PREFIX
```

### Parameters
- `-i` : Input FASTA file
- `-m` : Model type (`ve` for vertebrate, `pl` for plant)
- `-o` : Output prefix (can include directory path)

### Examples

```bash
# Test with sample data
conda activate PLEK2
bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test

# With custom data - vertebrate model
bin/PLEK2.py -i my_sequences.fa -m ve -o output/vertebrate_analysis

# Plant model with subdirectory output
bin/PLEK2.py -i plant_data.fa -m pl -o results/plants/sample1

# From conda environment bin
PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test
```

## Output Files

For output prefix `results`:

1. **results_scores.txt** - Sequence classifications and scores
2. **results_noncoding.txt** - List of non-coding sequence names  
3. **results_stats.txt** - Summary statistics
4. Intermediate files: `results_*.txt`, `results_*.fasta`

## Example Output

### results_stats.txt
```
PLEK2 Prediction Statistics
==================================================

Total input sequences: 100

Coding sequences:
  Number: 65
  Percentage: 65.00%

Non-coding sequences:
  Number: 35
  Percentage: 35.00%
```

### results_scores.txt
```
Sequence_Name                  Classification  Score
>sequence1                     Coding          1
>sequence2                     Non-coding      0
>sequence3                     Coding          1
...
```

### results_noncoding.txt
```
>sequence2
>sequence5
>sequence7
...
```

For detailed help, see INSTALLATION.md
