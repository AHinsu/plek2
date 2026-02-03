# PLEK2 Optimization - Changes Summary

## Overview
This document summarizes all the changes made to optimize PLEK2 according to the requirements.

## Changes Made

### 1. Output File Prefix Support ✅

**Modified Files:**
- `PLEK2.py`
- `functions.py`

**Changes:**
- Added `-o/--output` command-line parameter (required)
- Output prefix can include directory paths (e.g., `results/sample1`)
- Output directory is automatically created if it doesn't exist
- All intermediate and output files now use the specified prefix

**Example:**
```bash
python PLEK2.py -i input.fa -m ve -o results/experiment1/sample1
```

Creates:
- `results/experiment1/sample1_scores.txt`
- `results/experiment1/sample1_noncoding.txt`
- `results/experiment1/sample1_stats.txt`
- Plus intermediate files with same prefix

### 2. Three Output Files Generated ✅

**New Output Files:**

1. **`<prefix>_scores.txt`** - Main results file
   - Format: Tab-separated values
   - Columns: Sequence_Name, Classification, Score
   - Contains all sequences with their coding/non-coding classification

2. **`<prefix>_noncoding.txt`** - Non-coding sequences list
   - One sequence name per line
   - Only includes sequences classified as non-coding
   - Useful for downstream analysis of lncRNAs

3. **`<prefix>_stats.txt`** - Summary statistics
   - Total input sequences count
   - Coding sequences (number and percentage)
   - Non-coding sequences (number and percentage)

**Implementation:**
- New function `output_results()` replaces old `output_acc()`
- Captures sequence names from input FASTA file
- Generates comprehensive statistics

### 3. Intermediate Files Preserved ✅

**Previous Behavior:** All intermediate files were deleted after processing

**New Behavior:** Some intermediate files are kept with output prefix

**Intermediate Files Kept:**
- `<prefix>_filter_sequence_minlength.fasta` - Filtered sequences (>200bp)

**Benefits:**
- Enables debugging and validation
- Allows inspection of intermediate processing steps

### 4. Model Path Updated ✅

**Previous Behavior:**
- Models hardcoded in current directory
- `Coding_Net_kmer6_orf.h5`
- `Coding_Net_kmer6_orf_Arabidopsis.h5`

**New Behavior:**
- Models searched in `../utils/` directory (one level up from scripts)
- Uses `os.path` for cross-platform compatibility
- Better integration with conda and system installations

**Expected Directory Structure:**
```
plek2/
├── bin/          (or just root directory)
│   ├── PLEK2.py
│   └── functions.py
└── utils/
    ├── Coding_Net_kmer6_orf.h5
    └── Coding_Net_kmer6_orf_Arabidopsis.h5
```

### 5. Comprehensive Documentation ✅

**New Documentation Files:**

1. **`INSTALLATION.md`** - Complete installation guide
   - Three installation methods (conda, manual with symlinks, permanent installation)
   - Step-by-step instructions
   - Requirements and dependencies
   - Troubleshooting section
   - Usage examples

2. **`README.md`** - Quick reference
   - Condensed installation steps
   - Basic usage examples
   - Common issues and solutions

### 6. Git Configuration ✅

**New Files:**
- `.gitignore` - Excludes build artifacts, models, and intermediate files

**Excluded:**
- Python cache files (`__pycache__`, `*.pyc`)
- Model files (`*.h5`, `*.h5.bz2`)
- Intermediate processing files
- Example output files
- Virtual environments
- IDE configuration

## Functional Changes Summary

### Before:
```bash
python PLEK2.py -i input.fa -m ve
# No output parameter
# Hardcoded filenames in current directory
# Intermediate files deleted
# No comprehensive output files
```

### After:
```bash
python PLEK2.py -i input.fa -m ve -o results/sample1
# Required output prefix
# All files use prefix
# Intermediate files preserved
# Three comprehensive output files
# Models in utils/ directory
```

## Installation Workflows

1. Clone repository
2. Create utils directory
3. Build conda environment
4. Download models separately
5. Place models in utils directory
6. Run with `plek2` command in cloned directory
7. (Alternatively) place files from bin and utils in conda environment for global access. 

### Automated setup:
Run `setup.sh` to perform all steps.

## Backward Compatibility

**Breaking Changes:**
- `-o/--output` parameter is now REQUIRED
- Old scripts relying on default filenames will need to be updated

**Non-Breaking:**
- Model files use same names (just different location)
- Input format unchanged
- Processing logic unchanged
- Output classifications unchanged (only format improved)

## Benefits of Changes

1. **Flexibility**: Output prefix allows organized results
2. **Reproducibility**: Intermediate files enable validation
3. **Convenience**: Multiple output formats for different uses
4. **Portability**: Better directory structure for installations
5. **Integration**: Conda recipe enables package management
6. **Documentation**: Comprehensive guides for all scenarios

## Files Modified

- `PLEK2.py` - Added output parameter, directory creation
- `functions.py` - Updated all functions for output prefix, model path
- `README.txt` - Updated usage instructions

## Files Created

- `INSTALLATION.md` - Installation guide
- `DIRECTORY_STRUCTURE.md` - Directory organization guide
- `QUICKSTART.md` - Quick reference
- `CHANGES.md` - This file
- `.gitignore` - Git ignore configuration


