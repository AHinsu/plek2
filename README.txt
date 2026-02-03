PLEK2: a novel method for predicting lncRNA and mRNA based on sequence intrinsic features and Coding-Net model (Upgraded version of PLEK)
===========================================================
PLEK: predictor of long non-coding RNAs and mRNAs based on k-mer scheme (PLEK download | SourceForge.net)
===========================================================

REPOSITORY STRUCTURE
--------------------
plek2/
├── bin/                      # Python scripts
│   ├── PLEK2.py             # Main script
│   └── functions.py         # Helper functions
├── test/                     # Test FASTA files
│   ├── PLEK2_test.fa
│   ├── PLEK2_test_lncrna.fa
│   └── PLEK2_test_mrna.fa
├── utils/                    # Model files (download separately)
│   └── README.md            # Instructions for downloading models
├── setup.sh                  # Automated setup script
└── INSTALLATION.md          # Detailed installation guide


INSTALLATION
-------------
LncRNA participates in many important regulatory activities of organisms. Its biological structure is similar to messenger RNA (mRNA), in order to distinguish between lncRNA and mRNA (messenger RNA) transcripts more quickly and accurately, we upgraded the alignment-free PLEK to PLEK2.

QUICK SETUP:
Run the automated setup script:
$ ./setup.sh

This will create conda environment, download models, and set up everything.

For detailed installation instructions, see INSTALLATION.md


Requirements
------------
+ [Linux/macOS]
+ [Python version >= 3.8.5] (http://www.python.org/)

Conda Environment "PLEK2":
$ conda create -n PLEK2 -y python=3.8.5 numpy=1.19.2 pandas biopython
$ conda activate PLEK2
$ pip install keras==2.4.3 tensorflow==2.4.1 regex

For manual installation and other methods, see INSTALLATION.md
--------------------------------------------------

SETUP
-----
1. Download PLEK2_model_v3.tar.gz from SourceForge:
   $ cd utils
   $ wget https://sourceforge.net/projects/plek2/files/PLEK2_model_v3.tar.gz

2. Extract and decompress models:
   $ tar -xzf PLEK2_model_v3.tar.gz
   $ bunzip2 PLEK2_model_v3/*.bz2
   $ mv PLEK2_model_v3/*.h5 .
   $ cd ..

3. Copy to conda environment (optional):
   $ conda activate PLEK2
   $ cp bin/*.py $CONDA_PREFIX/bin/
   $ mkdir -p $CONDA_PREFIX/utils
   $ cp utils/*.h5 $CONDA_PREFIX/utils/


USAGE
-----
python bin/PLEK2.py -i fasta_file -m model -o output_prefix

Arguments:
  -i, --input_file   Input fasta file with sequences to be predicted (required)
  -m, --model        Model type: ve (vertebrate) or pl (plant) (required)
  -o, --output       Output file prefix, can include directory path (required)
   
Examples:
$ conda activate PLEK2
$ python bin/PLEK2.py -i test/PLEK2_test.fa -m ve -o results/test_output

This will create:
  - results/test_output_scores.txt       (sequence classifications and scores)
  - results/test_output_noncoding.txt    (list of non-coding sequence names)
  - results/test_output_stats.txt        (summary statistics)
  - Plus intermediate files for debugging

Alternative - Run from conda environment bin:
$ python $CONDA_PREFIX/bin/PLEK2.py -i input.fa -m ve -o output_prefix


OUTPUT FILES
------------
PLEK2 generates three main output files:

1. <prefix>_scores.txt: Contains sequence names, classification (Coding/Non-coding), and scores
2. <prefix>_noncoding.txt: List of all non-coding sequence names
3. <prefix>_stats.txt: Summary statistics with counts and percentages

Intermediate processing files are also kept with the output prefix for analysis.

==============
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

2350837044@qq.com 

liaiminmail AT gmail.com
emanlee815 AT 163.com
