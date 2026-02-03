PLEK2: a novel method for predicting lncRNA and mRNA based on sequence intrinsic features and Coding-Net model (Upgraded version of PLEK)
===========================================================
PLEK: predictor of long non-coding RNAs and mRNAs based on k-mer scheme (PLEK download | SourceForge.net)
===========================================================


INSTALLATION
-------------
LncRNA participates in many important regulatory activities of organisms. Its biological structure is similar to messenger RNA (mRNA), in order to distinguish between lncRNA and mRNA (messenger RNA) transcripts more quickly and accurately, we upgraded the alignment-free PLEK to PLEK2.


Requirements
------------
+ [Linux]
+ [Python version >= 3.8.5] (http://www.python.org/)

For detailed installation instructions, see INSTALLATION.md

Quick install with pip:
$ pip install regex
$ pip install keras==2.4.3
$ pip install pandas
$ pip install tensorflow==2.4.1
$ pip install biopython
$ pip install numpy==1.19.2

For conda installation and detailed setup instructions, see INSTALLATION.md
--------------------------------------------------

SETUP
-----
1. Download PLEK2_model_v3.tar.gz from https://sourceforge.net/projects/plek2/files/ and decompress it.
$ tar zvxf PLEK2_model_v3
2. Decompress models
$ bunzip2 Coding_Net_kmer6_orf.h5.bz2 
$ bunzip2 Coding_Net_kmer6_orf_Arabidopsis.h5.bz2
3. Place models in utils directory (one level up from scripts)
   See INSTALLATION.md for directory structure details


USAGE
-----
Python PLEK2.py -i fasta_file -m model -o output_prefix

Arguments:
  -i, --input_file   Input fasta file with sequences to be predicted (required)
  -m, --model        Model type: ve (vertebrate) or pl (plant) (required)
  -o, --output       Output file prefix, can include directory path (required)
   
Examples:
$ python PLEK2.py -i PLEK2_test.fa -m ve -o results/test_output

This will create:
  - results/test_output_scores.txt       (sequence classifications and scores)
  - results/test_output_noncoding.txt    (list of non-coding sequence names)
  - results/test_output_stats.txt        (summary statistics)
  - Plus intermediate files for debugging

OUTPUT FILES
------------
PLEK2 now generates three main output files:

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
