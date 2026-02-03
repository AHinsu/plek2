# PLEK2 Model Files Directory

This directory should contain the PLEK2 model files.

## Required Files

The following model files need to be downloaded and placed in this directory:

1. `Coding_Net_kmer6_orf.h5` - Vertebrate model
2. `Coding_Net_kmer6_orf_Arabidopsis.h5` - Plant model

## Download and Setup Instructions

### Quick Setup

```bash
# From the repository root directory
cd utils

# Download the model archive
wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz

# Extract the archive
tar -xzf PLEK2_model_v3.tar.gz

# Decompress the model files
bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf.h5.bz2
bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf_Arabidopsis.h5.bz2

# Move model files to this directory
mv PLEK2_model_v3/*.h5 .

# Clean up
rm -rf PLEK2_model_v3 PLEK2_model_v3.tar.gz
```

### Alternative: Direct Download

If wget is not available or you prefer manual download:

1. Visit: https://sourceforge.net/projects/plek2/files/
2. Download `PLEK2_model_v3.tar.gz`
3. Extract it: `tar -xzf PLEK2_model_v3.tar.gz`
4. Decompress models:
   - `bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf.h5.bz2`
   - `bunzip2 PLEK2_model_v3/Coding_Net_kmer6_orf_Arabidopsis.h5.bz2`
5. Move the `.h5` files to this `utils/` directory

## Verification

After setup, this directory should contain:

```
utils/
├── Coding_Net_kmer6_orf.h5
├── Coding_Net_kmer6_orf_Arabidopsis.h5
└── README.md
```

You can verify with:

```bash
ls -lh *.h5
```

Both model files should be present and have sizes of several hundred MB each.

## Notes

- Model files are compressed with bzip2 (.bz2) when downloaded
- They must be decompressed before use
- The models are not included in the git repository due to their large size
- These models are required for PLEK2 to function properly
