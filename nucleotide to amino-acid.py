
def split_into_codons(sequence):
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

def amino_converter(sequence):
    """
    Converts codons into amino acids using a codon table.
    Args:
        sequence (list): list of codon sequences in a string format.
    Returns:
        list (each string is an amino acid)
    """
    codon_table = {
    "AAA": "Lys","AAC": "Asn","AAG": "Lys","AAU": "Asn","ACA": "Thr","ACC": "Thr","ACG": "Thr","ACU": "Thr",
    "AGA": "Arg","AGC": "Ser","AGG": "Arg","AGU": "Ser","AUA": "Ile","AUC": "Ile","AUG": "Met","AUU": "Ile",
    "CAA": "Gln","CAC": "His","CAG": "Gln","CAU": "His","CCA": "Pro","CCC": "Pro","CCG": "Pro","CCU": "Pro",
    "CGA": "Arg","CGC": "Arg","CGG": "Arg","CGU": "Arg","CUA": "Leu","CUC": "Leu","CUG": "Leu","CUU": "Leu",
    "GAA": "Glu","GAC": "Asp","GAG": "Glu","GAU": "Asp","GCA": "Ala","GCC": "Ala","GCG": "Ala","GCU": "Ala",
    "GGA": "Gly","GGC": "Gly","GGG": "Gly","GGU": "Gly","GUA": "Val","GUC": "Val","GUG": "Val","GUU": "Val",
    "UAA": "Stop","UAC":"Tyr","UAG": "Stop","UAU":"Tyr","UCA": "Ser","UCC": "Ser","UCG": "Ser","UCU": "Ser",
    "UGA": "Stop","UGC":"Cys","UGG": "Trp","UGU": "Cys","UUA": "Leu","UUC": "Phe","UUG": "Leu","UUU": "Phe"
}
    
    amino_acids = []
    for codon in sequence:
        amino_acid = codon_table.get(codon, None)
        if amino_acid is not None:
            amino_acids.append(amino_acid)
        else:
            amino_acids.append("Unknown")
    return amino_acids


# Example usage:
nucleotide_sequence = 'CCACAAGTCAAGCCATTGCCTCTCTGACACGCCGTAAGAATTAATATGTAAACTTTGCGCGGGTTGACTGCGATCCGTTCAGTCTCGTCCGAGGGCACAATCCTATTCCCATTTGTATGTTCAGCTAACTTCTACCCATCCCCCGAAGTTAAGTAGGTCGTGAGATGCCATGGAGGCTCTCGTTCATCCCGTGGGACATCAAGCTTCCCCTTGATAAAGCACCCCGCTCGGGTGTAGCAGAGAAGACGCCTTCTGAATTGTGCAATCCCTCCACCTTATCTAAGCTTGCTACCAATAATTAGCATTTTTGCCTTGCGACAGACCTCCTACTTAGATTGCCACACATTGAGCTAGTCAGTGAGCGATAAGCTTGACGCGCTTTCAAGGGTCGCGAGTACGTGAACTAAGGCTCCGGACAGGACTATATACTTGGGTTTGATCTCGCCCCGACAACTGCAAACCTCAACTTTTTTAGATTATATGGTTAGCCGAAGTTGCACGAGGTGGCGTCCGCGGACTGCTCCCCGAGTGTGGCTCTTTCATCTGACAACGTGCAACCCCTATCGCGGCCGATTGTTTCTGCGGACGATGTTGTCCTCATAGTTTGGGCATGTTTCCCTTGTAGGTGTGAAACCACTTAGCTTCGCGCCGTAGTCCCAATGAAAAACCTATGGACTTTGTTTTGGGTAGCACCAGGAATCTGAACCGTGTGAATGTGGACGTCGCGCGCGTAGACCTTTATCTCCGGTTCAAGCTAGGGATGTGGCTGCATGCTACGTTGTCACACCTACACTGCTCGAAGTAAATATGCGAAGCGCGCGGCCTGGCCGGAGGCGTTCCGCGCCGCCACGTGTTCGTTAACTGTTGATTGGTGGCACATAAGCAATATCGTAGTCCGTCAAATTCAGCTCTGTTATCCCGGGCGTTATGTGTCAAATGGCGTAGAACGGGATTGACTGTTTGACGGTAGCTGCTGATCGGTACGGTAACGGAGAATCTGTCGGGCTATGTCACTAATACTTTCCAAACGCCCCGTACCGATGCTGAACAAGTCGATGCAGGCTCCCGTCTTTGAAAAGGGGTAAACATACAAGTGGATA'
result = split_into_codons(nucleotide_sequence)
final_result = amino_converter(result)
print(final_result)


