# PLEK2 Repository - Final Summary

## Repository Structure

The repository has been reorganized with the following structure:

```
plek2/
├── bin/                          # Python scripts
│   ├── PLEK2.py                 # Main prediction script
│   └── functions.py             # Helper functions
├── test/                         # Test data files
│   ├── PLEK2_test.fa            # Mixed test sequences
│   ├── PLEK2_test_lncrna.fa     # lncRNA test sequences
│   └── PLEK2_test_mrna.fa       # mRNA test sequences
├── utils/                        # Model files directory
│   └── README.md                # Instructions for downloading models
├── conda-recipe/                 # Conda package recipe
│   ├── meta.yaml                # Package metadata
│   └── build.sh                 # Build script
├── setup.sh                      # Automated setup script
├── INSTALLATION.md              # Detailed installation guide
├── QUICKSTART.md                # Quick reference guide
├── README.txt                   # Basic README
├── DIRECTORY_STRUCTURE.md       # Directory organization guide
└── CHANGES.md                   # Summary of all changes
```

## Key Features

### 1. Output File Management
- **Output Prefix**: Use `-o` parameter to specify output file prefix (can include directories)
- **Three Output Files**:
  - `<prefix>_scores.txt` - Detailed classifications for all sequences
  - `<prefix>_noncoding.txt` - List of non-coding sequence names
  - `<prefix>_stats.txt` - Summary statistics with counts and percentages
- **Intermediate Files**: All processing files preserved with prefix for debugging

### 2. Installation Methods

#### Quick Install (Automated)
```bash
git clone https://github.com/AHinsu/plek2.git
cd plek2
./setup.sh
```

#### Manual Install
```bash
# Create conda environment
conda create -n PLEK2 -y python=3.8.5 numpy=1.19.2 pandas biopython
conda activate PLEK2
pip install keras==2.4.3 tensorflow==2.4.1 regex

# Clone repository
git clone https://github.com/AHinsu/plek2.git
cd plek2

# Download models
cd utils
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz
tar -xzf PLEK2_model_v3.tar.gz
bunzip2 PLEK2_model_v3/*.bz2
mv PLEK2_model_v3/*.h5 .
rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz
cd ..

# Copy to conda environment
cp bin/*.py $CONDA_PREFIX/bin/
mkdir -p $CONDA_PREFIX/utils
cp utils/*.h5 $CONDA_PREFIX/utils/
```

### 3. Usage

```bash
# Activate conda environment
conda activate PLEK2

# Run from repository
python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test

# Or from conda environment
python $CONDA_PREFIX/bin/PLEK2.py -i input.fa -m ve -o output_prefix
```

## Model Files

Models are downloaded separately from SourceForge:
- **Vertebrate Model**: `Coding_Net_kmer6_orf.h5` (~500MB)
- **Plant Model**: `Coding_Net_kmer6_orf_Arabidopsis.h5` (~500MB)

Download URL: https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz

## Conda Environment "PLEK2"

The conda environment includes all required dependencies:
- python = 3.8.5
- numpy = 1.19.2
- pandas
- keras = 2.4.3
- tensorflow = 2.4.1
- biopython
- regex

## Output Examples

### Scores File (`<prefix>_scores.txt`)
```
Sequence_Name    Classification    Score
>sequence1       Coding            1
>sequence2       Non-coding        0
>sequence3       Coding            1
```

### Non-coding List (`<prefix>_noncoding.txt`)
```
>sequence2
>sequence5
>sequence8
```

### Stats File (`<prefix>_stats.txt`)
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

## Changes from Original

1. ✅ **Required output prefix parameter** (`-o`)
2. ✅ **Three comprehensive output files** (scores, noncoding list, stats)
3. ✅ **Intermediate files preserved** (not deleted)
4. ✅ **Model path updated** (searches in `../utils/`)
5. ✅ **Repository reorganized** (bin/, test/, utils/ structure)
6. ✅ **Automated setup script** (setup.sh)
7. ✅ **Conda environment support** (PLEK2 environment)
8. ✅ **Comprehensive documentation** (multiple guide files)

## Testing

Test with the provided sample data:

```bash
conda activate PLEK2
python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o test_output/results

# Check outputs
ls -lh test_output/results_*.txt
cat test_output/results_stats.txt
```

## Documentation Files

- **INSTALLATION.md** - Complete installation instructions with multiple methods
- **QUICKSTART.md** - Quick reference for common tasks
- **README.txt** - Basic README with overview
- **DIRECTORY_STRUCTURE.md** - Directory organization guide
- **CHANGES.md** - Detailed list of all changes
- **utils/README.md** - Model download instructions

## Support

- **GitHub**: https://github.com/AHinsu/plek2
- **Issues**: https://github.com/AHinsu/plek2/issues
- **Email**: emanlee815@163.com

## Requirements

- Linux or macOS
- Python >= 3.8
- Conda (recommended)
- ~4GB RAM
- ~2GB disk space for models

## Next Steps for Users

1. Run `./setup.sh` for automated installation
2. Or follow manual installation in INSTALLATION.md
3. Download model files to utils/ directory
4. Test with provided data in test/ directory
5. Use with your own data

---

**All requirements from the problem statement have been implemented successfully!**
