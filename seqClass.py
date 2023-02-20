#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
from collections import Counter


parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
#parser.add_argument("-n", "--nucleotide", action= store_true, help = "Print nucleotide percentage") 
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()  
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND motif")
    else:
        print("NOT FOUND")
#now we are  able to classify rna and dna correctly

# Count the occurrences of each nucleotide in the sequence
counts = Counter(args.seq)

# Compute the total number of nucleotides in the sequence
total_nucleotides = sum(counts.values())

# Compute the percentage of each nucleotide
percentages = {nucleotide: count / total_nucleotides * 100 for nucleotide, count in counts.items()}

# Print the percentages
print("Nucleotide percentages:")
for nucleotide, percentage in percentages.items():
  print(f"{nucleotide}: {percentage:.2f}%")

# Add an argument to output the raw count of each nucleotide
parser.add_argument("-c", "--counts", action="store_true", help="Output the raw count of each nucleotide")

# If the --counts argument is passed, output the raw counts
if args.counts:
    print("Nucleotide counts:")
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count}")
