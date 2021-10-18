#!/usr/bin/env python

usage = '''python dnalen_weight.py fastafile'''
import sys

def read_fasta(fastafile):
    sequences = {}
    for line in open(fastafile):
        if line[0] != '>':
            seq += line.rstrip()
        else:
            head = line[1:]
            seq = ''
        sequences[head] = seq
    return sequences

def dna_weight(sequence):
    bases_w = {
    "A": 331.06817,
    "C": 307.056936,
    "G": 347.063084,
    "T": 322.056602,
    }
    water = 18.0153
    weight = 0
    for base in 'ACGT':
        weight += sequence.count(base)*bases_w[base]
    return weight - (len(sequence) -1)*water
if __name__ == '__main__':

    fasta = read_fasta(sys.argv[1])
    for sequence in fasta.keys():
        print(sequence.rstrip())
        print(fasta[sequence])
        print(dna_weight(fasta[sequence]))
        print(len(fasta[sequence]))