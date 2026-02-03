#!/bin/bash

# Create directory structure
mkdir -p $PREFIX/bin
mkdir -p $PREFIX/share/plek2/utils

# Copy main scripts to share directory
cp PLEK2.py $PREFIX/share/plek2/
cp functions.py $PREFIX/share/plek2/

# Create a wrapper script in bin that calls the main script
cat > $PREFIX/bin/plek2 << 'WRAPPER'
#!/usr/bin/env python
import sys
import os

# Get the directory where this wrapper is located
wrapper_dir = os.path.dirname(os.path.abspath(__file__))
# Scripts are in share/plek2 relative to bin
script_dir = os.path.join(wrapper_dir, '..', 'share', 'plek2')
script_path = os.path.join(script_dir, 'PLEK2.py')

# Add script directory to Python path so imports work
sys.path.insert(0, script_dir)

# Execute the main script
exec(compile(open(script_path).read(), script_path, 'exec'))
WRAPPER

chmod +x $PREFIX/bin/plek2

# Create utils directory for models (user will need to download models separately)
# This creates the expected directory structure
echo "Models should be placed in the utils directory" > $PREFIX/share/plek2/utils/README.txt
echo "Download models from: https://sourceforge.net/projects/plek2/files/" >> $PREFIX/share/plek2/utils/README.txt
echo "Place the following files in this directory:" >> $PREFIX/share/plek2/utils/README.txt
echo "  - Coding_Net_kmer6_orf.h5" >> $PREFIX/share/plek2/utils/README.txt
echo "  - Coding_Net_kmer6_orf_Arabidopsis.h5" >> $PREFIX/share/plek2/utils/README.txt

echo "PLEK2 installation complete!"
echo ""
echo "IMPORTANT: You need to download the model files separately:"
echo "1. Download models from: https://sourceforge.net/projects/plek2/files/"
echo "2. Decompress the models:"
echo "   bunzip2 Coding_Net_kmer6_orf.h5.bz2"
echo "   bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2"
echo "3. Place them in: $PREFIX/share/plek2/utils/"
