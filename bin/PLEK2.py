#!/usr/bin/env python
import numpy as np
import pandas as pd
from functions import filter_fasta, get_kmer, get_ORF, contact, prediction, init_data, output_results
import argparse
import sys
import os

def parse_arguments():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Instruction of PLEK2(more details in README.txt):')
    parser.add_argument('-i', '--input_file', help='Input file in fasta format', required=True)
    parser.add_argument('-m', '--model', help='ve: vertebrate, pl: plant', required=True)
    parser.add_argument('-o', '--output', help='Output file prefix (can include directory)', required=True)
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Create output directory if needed
    output_prefix = args.output
    output_dir = os.path.dirname(output_prefix)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Read fasta file
        seq_names = filter_fasta(args.input_file, output_prefix)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    # Extract k-mer sequences
    get_kmer(output_prefix + '_kmer_seqs')

    # Extract ORF sequences
    get_ORF(output_prefix + '_seq_lines.fasta', output_prefix)

    # Get associations between k-mers and ORFs
    contact(output_prefix + '_kmer_6.txt', output_prefix + '_orf_length.txt', output_prefix)

    print("loading data ...")

    # Initialize data
    nums = init_data(output_prefix + "_features.txt")

    # Prepare data for prediction
    dataframe = pd.DataFrame(nums)
    dataset = dataframe.values

    X = np.zeros(shape=(len(dataset), 1, 5461, 1))

    for i, x in enumerate(dataset):
        x = np.asarray(x)
        x = np.resize(x, (1, 5461, 1))
        X[i] = x

    print("Loading Model and predicting ...")

    md = args.model

    # Perform prediction
    out = prediction(X, md)

    print(out)

    # Output prediction results
    output_results(out, seq_names, output_prefix)

if __name__ == "__main__":
    main()
