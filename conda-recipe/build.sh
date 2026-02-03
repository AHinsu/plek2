#!/bin/bash

# Create directory structure
mkdir -p $PREFIX/bin
mkdir -p $PREFIX/share/plek2/utils

# Copy main scripts to bin directory as executable scripts
cp PLEK2.py $PREFIX/bin/plek2
cp functions.py $PREFIX/share/plek2/

# Make PLEK2.py executable and add shebang
sed -i '1i#!/usr/bin/env python' $PREFIX/bin/plek2
chmod +x $PREFIX/bin/plek2

# Create utils directory for models (user will need to download models separately)
# This creates the expected directory structure
echo "Models should be placed in the utils directory" > $PREFIX/share/plek2/utils/README.txt
echo "Download models from: https://sourceforge.net/projects/plek2/files/" >> $PREFIX/share/plek2/utils/README.txt
echo "Place the following files in this directory:" >> $PREFIX/share/plek2/utils/README.txt
echo "  - Coding_Net_kmer6_orf.h5" >> $PREFIX/share/plek2/utils/README.txt
echo "  - Coding_Net_kmer6_orf_Arabidopsis.h5" >> $PREFIX/share/plek2/utils/README.txt

# Create a symlink from utils to the expected location relative to scripts
cd $PREFIX/share/plek2
ln -s utils ../utils

echo "PLEK2 installation complete!"
echo ""
echo "IMPORTANT: You need to download the model files separately:"
echo "1. Download models from: https://sourceforge.net/projects/plek2/files/"
echo "2. Decompress the models:"
echo "   bunzip2 Coding_Net_kmer6_orf.h5.bz2"
echo "   bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2"
echo "3. Place them in: $PREFIX/share/plek2/utils/"
