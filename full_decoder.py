###### RNA codon converter from FASTA file 

def codon_converter(sequence):
    """
    Splices a list of nucleotide characters into groups of three (codons).
    Args:
        sequence (string): string of characters "ATCG" representing nucleotides.
    Returns:
        list of strings (each string is a codon).
    """
    sequence = sequence.replace('T', 'U')
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    return codons


###### Amino acid converter (Uniprot 1-letter code key compatible)

def amino_converter(sequence):
    """
    Converts codons into amino acids using a codon table.
    Args:
        sequence (list): list of codon sequences in a string format.
    Returns:
        list (each string is an amino acid)
    """
    codon_table = {
        "AAA": "K", "AAC": "N", "AAG": "K", "AAU": "N", "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
        "AGA": "R", "AGC": "S", "AGG": "R", "AGU": "S", "AUA": "I", "AUC": "I", "AUG": "M", "AUU": "I",
        "CAA": "Q", "CAC": "H", "CAG": "Q", "CAU": "H", "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
        "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
        "GAA": "E", "GAC": "D", "GAG": "E", "GAU": "D", "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
        "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G", "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
        "UAA": "*", "UAC": "Y", "UAG": "*", "UAU": "Y", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
        "UGA": "*", "UGC": "C", "UGG": "W", "UGU": "C", "UUA": "L", "UUC": "F", "UUG": "L", "UUU": "F"
    }
    
    amino_acids = []
    for codon in sequence:
        amino_acid = codon_table.get(codon, None)
        if amino_acid is not None:
            amino_acids.append(amino_acid)
        else:
            amino_acids.append("Unknown")
    return amino_acids


###### Protein sequencing and AlphaFold API interaction

import requests

def get_alphafold_prediction(protein_sequence):
    url = "https://alphafold.ebi.ac.uk/api/prediction/Q5VSL9?key=AIzaSyCeurAJz7ZGjPQUtEaerUkBZ3TaBkXrY94"
    response = requests.get(url)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    if response.ok:
        predictions = response.json()
        if predictions:
            # Example: print the UniProt accession and download link for the PDB file
            for pred in predictions:
                print("UniProt accession:", pred.get("uniprotAccession"))
                print("PDB download link:", pred.get("pdbUrl"))
        else:
            print("No prediction found for this sequence.")
    else:
        print("Error querying AlphaFold API.")


# Example usage with Human Insulin Uniprot sequence:

# Use triple-quoted strings for easier editing of long sequences

nucleotide_sequence = """
ATGGGCGCTGTGGATGCGCCTGCTGCCGCTGCTGGGCCTGCTGGGCCTGTGGGGCCCGGAT
CCGGCGGCGGCGTTTGTGAACCAGCATCTGTGCGGCAGCCATCTGGTGGAAGCGCTGTAT
CTGGTGTGCGGCGAACGCGGCTTTTTTTATACCCCGAAAACCCGCCGCGAAGCGGAGGAT
CTGCAGGTGGGCCAGGTGGAACTGGGCGGCGGCCCGGGCGCGGGCAGCCTGCAGCCGCTG
GCGCTGGAAGGCAGCCTGCAGAAACGCGGCATTGTGGAACAGTGCTGCACCAGCATTTGC
AGCCTGTATCAGCTGGAAAACTATTGCAAC
"""

codon_result = codon_converter(nucleotide_sequence)
amino_result = amino_converter(codon_result)
get_alphafold_prediction(amino_result)




