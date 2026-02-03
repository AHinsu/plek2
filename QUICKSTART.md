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
chmod +x $CONDA_PREFIX/bin/PLEK2.py
```

## Usage

```bash
# Activate conda environment
conda activate PLEK2

# Run from repository
python bin/PLEK2.py -i INPUT.fa -m MODEL -o OUTPUT_PREFIX

# Or from conda environment bin
python $CONDA_PREFIX/bin/PLEK2.py -i INPUT.fa -m MODEL -o OUTPUT_PREFIX
```

### Parameters
- `-i` : Input FASTA file
- `-m` : Model type (`ve` for vertebrate, `pl` for plant)
- `-o` : Output prefix (can include directory path)

### Examples

```bash
# Test with sample data
conda activate PLEK2
python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test

# With custom data - vertebrate model
python bin/PLEK2.py -i my_sequences.fa -m ve -o output/vertebrate_analysis

# Plant model with subdirectory output
python bin/PLEK2.py -i plant_data.fa -m pl -o results/plants/sample1
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

## Tips

- Intermediate files are kept for analysis - remove manually if not needed
- Output directory is created automatically if it doesn't exist
- Sequences must be >= 200 bp (filtered automatically)
- Use absolute or relative paths for input/output files

## Common Issues

**Models not found:**
- Ensure models are in `utils/` directory
- Check models are decompressed (.h5 not .h5.bz2)

**Import errors:**
- Install all dependencies with pip
- Use Python >= 3.8

**File not found:**
- Check input file path
- Ensure read permissions

For detailed help, see INSTALLATION.md and DIRECTORY_STRUCTURE.md
