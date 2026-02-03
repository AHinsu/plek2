import os
import numpy as np
from keras.models import load_model
from itertools import chain
from Bio import Seq
import regex as re

################  filter_fasta file ##############################
def filter_fasta(fa, output_prefix):
    # Change the format of the input fasta file ...
    f1 = open(fa, 'r').readlines()
    f2 = open(output_prefix + '_seq_to_one_line.fasta', 'w')
    n = 0
    for i in f1:
        if i.startswith('>'):
            n += 1
            if n == 1:
                f2.write(i)
            else:
                f2.write('\n' + i)
        else:
            f2.write(i.strip("\n"))  # strip function strips the left and right Spaces
    f2.close()

    # Remove seqences whose lengths are not more than minlength ...

    file_in = open(output_prefix + "_seq_to_one_line.fasta", 'r')

    fa_Con = file_in.read()

    file_in.close()

    every_fas = fa_Con.split(">")

    f3 = open(output_prefix + "_filter_sequence_minlength.fasta", 'w')

    minlength = 200

    for i in every_fas:
        if i != "":
            start = i.index("\n")
            # print(i[start:])
            if len(i[start:]) > minlength:
                f3.write(">" + i)
    f3.close()

    # Split define lines and nucleotide lines

    file_in = open(output_prefix + "_filter_sequence_minlength.fasta", 'r').readlines()

    f4 = open(output_prefix + "_define_lines.fasta", 'w')
    f5 = open(output_prefix + "_seq_lines.fasta", 'w')
    
    # Store sequence names for later use
    seq_names = []
    n = 0
    for i in file_in:
        if i.startswith('>'):
            seq_names.append(i.strip())
            n += 1
            if n == 1:
                f4.write(i)
            else:
                f4.write('\n' + i)
        else:
            f5.write(i)

    f4.close()
    f5.close()

    # Nucleotides to upper case ...
    
    file_in = open(output_prefix + "_seq_lines.fasta", 'r').readlines()

    f6 = open(output_prefix + "_seq_upper.fasta", 'w')

    for i in file_in:
        f6.write(i.upper())

    f6.close()

    # Replace U with T

    file_in = open(output_prefix + '_seq_upper.fasta', 'r')
    f_new = open(output_prefix + '_replace_u', 'w')
    find_str = 'U'
    replace_str = 'T'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()
    
    # Replace R Y M K S W H B V D with N
    file_in = open(output_prefix + '_replace_u', 'r')
    f_new = open(output_prefix + '_replace_R', 'w')
    find_str = 'R'
    replace_str = 'N'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_R', 'r')
    f_new = open(output_prefix + '_replace_Y', 'w')
    find_str = 'Y'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_Y', 'r')
    f_new = open(output_prefix + '_replace_M', 'w')
    find_str = 'M'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_M', 'r')
    f_new = open(output_prefix + '_replace_K', 'w')
    find_str = 'K'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_K', 'r')
    f_new = open(output_prefix + '_replace_S', 'w')
    find_str = 'S'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_S', 'r')
    f_new = open(output_prefix + '_replace_W', 'w')
    find_str = 'W'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_W', 'r')
    f_new = open(output_prefix + '_replace_H', 'w')
    find_str = 'H'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_H', 'r')
    f_new = open(output_prefix + '_replace_B', 'w')
    find_str = 'B'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_B', 'r')
    f_new = open(output_prefix + '_replace_V', 'w')
    find_str = 'V'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    file_in = open(output_prefix + '_replace_V', 'r')
    f_new = open(output_prefix + '_kmer_seqs', 'w')
    find_str = 'D'
    for line in file_in:
        if find_str in line:
            line = line.replace(find_str, replace_str)
            f_new.write(line)
        else:
            f_new.write(line)

    f_new.close()

    ## remove middle file
    os.remove(output_prefix + '_replace_u')
    os.remove(output_prefix + '_replace_R')
    os.remove(output_prefix + '_replace_Y')
    os.remove(output_prefix + '_replace_M')
    os.remove(output_prefix + '_replace_K')
    os.remove(output_prefix + '_replace_S')
    os.remove(output_prefix + '_replace_W')
    os.remove(output_prefix + '_replace_H')
    os.remove(output_prefix + '_replace_B')
    os.remove(output_prefix + '_replace_V')
    
    return seq_names


#################### get kmer_features #####################################

def get_kmer(kmer_seqs):
    # Define a class for k-mer featurization
    class kmer_featurization:
        # Constructor to initialize the class with k value and DNA letters
        def __init__(self, k):
            self.k = k
            self.letters = ['A', 'T', 'C', 'G']
            self.multiplyBy = 4 ** np.arange(k - 1, -1, -1)
            self.n = 4 ** k

        # Method to obtain k-mer features for a list of sequences
        def obtain_kmer_feature_for_a_list_of_sequences(self, seqs, write_number_of_occurrences=False):
            kmer_features = []
            for seq in seqs:
                this_kmer_feature = self.obtain_kmer_feature_for_one_sequence(seq.upper(),
                                                                              write_number_of_occurrences=write_number_of_occurrences)
                kmer_features.append(this_kmer_feature)
            kmer_features = np.array(kmer_features)
            return kmer_features

        # Method to obtain k-mer features for one sequence
        def obtain_kmer_feature_for_one_sequence(self, seq, write_number_of_occurrences=False):
            number_of_kmers = len(seq) - self.k + 1
            kmer_feature = np.zeros(self.n)
            for i in range(number_of_kmers):
                temporary = seq[i:(i + self.k)]
                if 'N' not in temporary:
                    this_kmer = seq[i:(i + self.k)]
                    this_numbering = self.kmer_numbering_for_one_kmer(this_kmer)
                    kmer_feature[this_numbering] += 1
            if not write_number_of_occurrences:
                kmer_feature = (kmer_feature / number_of_kmers) * pow(4, (self.k) - 5)
            return kmer_feature

        # Method to calculate the numbering for one k-mer
        def kmer_numbering_for_one_kmer(self, kmer):
            digits = []
            for letter in kmer:
                digits.append(self.letters.index(letter))
            digits = np.array(digits)
            numbering = (digits * self.multiplyBy).sum()
            return numbering

    # Read sequences from the input file
    with open(kmer_seqs, 'r') as f:
        seq_list = f.read().splitlines()

    # Count the number of sequences in the input file
    count_line = len(seq_list)

    # Generate k-mer features for k=1 to k=6
    k = 1
    obj = kmer_featurization(k)
    kmer_feature_1 = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=False)
    kmer_feature_1 = kmer_feature_1.reshape(count_line, 4)

    k = 2
    obj = kmer_featurization(k)
    kmer_feature_2 = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=False)
    kmer_feature_2 = kmer_feature_2.reshape(count_line, 16)

    k = 3
    obj = kmer_featurization(k)
    kmer_feature_3 = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=False)
    kmer_feature_3 = kmer_feature_3.reshape(count_line, 64)

    k = 4
    obj = kmer_featurization(k)
    kmer_feature_4 = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=False)
    kmer_feature_4 = kmer_feature_4.reshape(count_line, 256)

    k = 5
    obj = kmer_featurization(k)
    kmer_feature_5 = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=False)
    kmer_feature_5 = kmer_feature_5.reshape(count_line, 1024)

    k = 6
    obj = kmer_featurization(k)
    kmer_feature_6 = obj.obtain_kmer_feature_for_a_list_of_sequences(seq_list, write_number_of_occurrences=False)
    kmer_feature_6 = kmer_feature_6.reshape(count_line, 4096)

    # Concatenate k-mer features from k=1 to k=6
    kmer_6 = np.concatenate(
        (kmer_feature_1, kmer_feature_2, kmer_feature_3, kmer_feature_4, kmer_feature_5, kmer_feature_6), axis=1)

    # Save the concatenated k-mer features to a file
    np.savetxt(kmer_seqs.replace('_kmer_seqs', '_kmer_6.txt'), kmer_6)

    
   
def get_ORF(fa, output_prefix):
    # Function to read DNA sequence data from a file
    def read_data(seq_line):
        RNA_data = []
        try:
            with open(seq_line, "rt") as fp:
                lines = fp.readlines()
            for i in range(0, len(lines)):
                RNA_data.append(lines[i].replace("\n", "").strip().split())
        except:
            print("Exception occurred while reading data")
        finally:
            return RNA_data

    # Read DNA sequences from the input file
    seq = read_data(fa)
    seq = list(chain.from_iterable(seq))

    # ORF detection
    startP = re.compile('ATG')  # Start codon is ATG
    nuc = seq
    longest = (0,)  # Length of the peptide chain
    length = []
    for i in range(len(nuc)):
        for m in startP.finditer(nuc[i], overlapped=True):
            if len(Seq.Seq(nuc[i])[m.start():].translate(to_stop=True)) > longest[0]:
                pro = Seq.Seq(nuc[i])[m.start():].translate(to_stop=True)
                longest = (len(pro),
                           m.start(),
                           str(pro),
                           nuc[i][m.start():m.start() + len(pro) * 3 + 3])
        longest = (0,)
        length.append(len(pro) + 1)

    # Calculate the log base 10 of the peptide chain length
    length_log10 = np.log10(length)

    # Normalize the ORF length data
    orf_normalize = []
    for i in range(len(length_log10 - 1)):
        x = float(length_log10[i] - 0.48) / (4 - 0.48)
        orf_normalize.append(x)

    # Save the normalized data to a file
    with open(output_prefix + '_orf_length.txt', 'w') as f:
        for i in orf_normalize:
            f.write(str(i) + '\n')


def contact(kmer, ORF, output_prefix):
    # Load k-mer and ORF data from files
    k_mer = np.loadtxt(kmer)
    ORF = np.loadtxt(ORF)

    # Combine k-mer and ORF features
    features = np.column_stack((k_mer, ORF))
    np.savetxt(output_prefix + '_features.txt', features, fmt='%0.8f')

def read_data(human_data):
    RNA_data = []
    try:
        with open(human_data, "rt") as fp:
            lines = fp.readlines()
        for i in range(0, len(lines)):
            RNA_data.append(lines[i].replace("\n", "").strip().split())
    except:
        print("Exception occurred while reading data")
    finally:
        return RNA_data


def init_data(human_data):
    temp_datas = read_data(human_data)
    if len(temp_datas) <= 0:
        print("Data initialization failed")
    else:
        RNA_data = np.array(temp_datas)
        nums = RNA_data[:, :]
        nums = nums.astype(np.float)
        return nums


def prediction(dat, md):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Models are in utils directory, one level up from scripts
    utils_dir = os.path.join(script_dir, '..', 'utils')
    
    if md == 've':
        model_path = os.path.join(utils_dir, 'Coding_Net_kmer6_orf.h5')
        model = load_model(model_path)
    else:
        model_path = os.path.join(utils_dir, 'Coding_Net_kmer6_orf_Arabidopsis.h5')
        model = load_model(model_path)

    Y = model.predict_classes(dat)
    labels = np.array(Y)
    return labels


def output_results(Y, seq_names, output_prefix):
    """
    Create three output files:
    1. Scores file: sequence names and their coding/non-coding classification with scores
    2. Non-coding list: text file with names of non-coding sequences
    3. Stats file: summary statistics
    """
    seq_len = len(Y)
    
    # Validate input
    if seq_len == 0:
        print("Warning: No sequences to process. Creating empty output files.")
        # Create empty output files
        open(output_prefix + '_scores.txt', 'w').write("Sequence_Name\tClassification\tScore\n")
        open(output_prefix + '_noncoding.txt', 'w').close()
        with open(output_prefix + '_stats.txt', 'w') as f:
            f.write("PLEK2 Prediction Statistics\n")
            f.write("=" * 50 + "\n\n")
            f.write("Total input sequences: 0\n")
            f.write("No sequences processed.\n")
        return [0, 0]
    
    # Check if sequence names match predictions
    if len(seq_names) != seq_len:
        print(f"Warning: Number of sequence names ({len(seq_names)}) doesn't match predictions ({seq_len})")
    
    noncoding = 0
    coding = 0
    noncoding_names = []
    
    # Count coding and non-coding sequences
    for i in range(len(Y)):
        if Y[i] == 0:
            noncoding = noncoding + 1
            if i < len(seq_names):
                noncoding_names.append(seq_names[i])
        else:
            coding = coding + 1
    
    pred_noncoding_acc = noncoding / seq_len
    pred_coding_acc = 1 - pred_noncoding_acc
    
    print('non-coding =', pred_noncoding_acc)
    print('coding =', pred_coding_acc)
    
    # 1. Create scores file with sequence names and classifications
    scores_file = output_prefix + '_scores.txt'
    with open(scores_file, 'w') as f:
        f.write("Sequence_Name\tClassification\tScore\n")
        for i in range(len(Y)):
            if i < len(seq_names):
                seq_name = seq_names[i]
            else:
                seq_name = f">sequence_{i+1}"
                print(f"Warning: Missing sequence name for index {i}, using generic name")
            classification = "Non-coding" if Y[i] == 0 else "Coding"
            score = 0 if Y[i] == 0 else 1
            f.write(f"{seq_name}\t{classification}\t{score}\n")
    
    # 2. Create non-coding list file
    noncoding_file = output_prefix + '_noncoding.txt'
    with open(noncoding_file, 'w') as f:
        for name in noncoding_names:
            f.write(f"{name}\n")
    
    # 3. Create stats file
    stats_file = output_prefix + '_stats.txt'
    with open(stats_file, 'w') as f:
        f.write("PLEK2 Prediction Statistics\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total input sequences: {seq_len}\n\n")
        f.write(f"Coding sequences:\n")
        f.write(f"  Number: {coding}\n")
        f.write(f"  Percentage: {pred_coding_acc * 100:.2f}%\n\n")
        f.write(f"Non-coding sequences:\n")
        f.write(f"  Number: {noncoding}\n")
        f.write(f"  Percentage: {pred_noncoding_acc * 100:.2f}%\n")
    
    print(f"\nOutput files created:")
    print(f"  - Scores: {scores_file}")
    print(f"  - Non-coding list: {noncoding_file}")
    print(f"  - Statistics: {stats_file}")


    os.remove(output_prefix + '_define_lines.fasta')
    os.remove(output_prefix + '_seq_upper.fasta')
    # os.remove(output_prefix + 'filter_sequence_minlength.fasta')
    os.remove(output_prefix + '_kmer_6.txt')#
    os.remove(output_prefix + '_kmer_seqs')
    os.remove(output_prefix + '_orf_length.txt')
    os.remove(output_prefix + '_seq_lines.fasta')
    os.remove(output_prefix + '_seq_to_one_line.fasta')
    os.remove(output_prefix + '_features.txt')
    
    return [pred_noncoding_acc, pred_coding_acc]



