# PLEK2 Quick Start Guide

## Installation (Quick)

```bash
# 1. Clone repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# 2. Install dependencies
pip install numpy==1.19.2 pandas keras==2.4.3 tensorflow==2.4.1 biopython regex

# 3. Create utils directory
mkdir -p utils

# 4. Download and install models
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz
tar -xzf PLEK2_model_v3.tar.gz
bunzip2 PLEK2_model_v3/*.bz2
mv PLEK2_model_v3/*.h5 utils/
```

## Usage

```bash
python PLEK2.py -i INPUT.fa -m MODEL -o OUTPUT_PREFIX
```

### Parameters
- `-i` : Input FASTA file
- `-m` : Model type (`ve` for vertebrate, `pl` for plant)
- `-o` : Output prefix (can include directory path)

### Examples

```bash
# Basic usage
python PLEK2.py -i sequences.fa -m ve -o results

# With output directory
python PLEK2.py -i sequences.fa -m ve -o output/sample1

# Plant model
python PLEK2.py -i plant_seqs.fa -m pl -o plant_results
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
