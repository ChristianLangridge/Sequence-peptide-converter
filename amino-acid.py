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

codon_sequence = ['CCA', 'CAA', 'GUC', 'AAG', 'CCA', 'UUG', 'CCU', 'CUC', 'UGA', 'CAC', 'GCC', 'GUA', 'AGA', 'AUU', 'AAU', 'AUG', 'UAA', 'ACU', 'UUG', 'CGC', 'GGG', 'UUG', 'ACU', 'GCG', 'AUC', 'CGU', 'UCA', 'GUC', 'UCG', 'UCC', 'GAG', 'GGC', 'ACA', 'AUC', 'CUA', 'UUC', 'CCA', 'UUU', 'GUA', 'UGU', 'UCA', 'GCU', 'AAC', 'UUC', 'UAC', 'CCA', 'UCC', 'CCC', 'GAA', 'GUU', 'AAG', 'UAG', 'GUC', 'GUG', 'AGA', 'UGC', 'CAU', 'GGA', 'GGC', 'UCU', 'CGU', 'UCA', 'UCC', 'CGU', 'GGG', 'ACA', 'UCA', 'AGC', 'UUC', 'CCC', 'UUG', 'AUA', 'AAG', 'CAC', 'CCC', 'GCU', 'CGG', 'GUG', 'UAG', 'CAG', 'AGA', 'AGA', 'CGC', 'CUU', 'CUG', 'AAU', 'UGU', 'GCA', 'AUC', 'CCU', 'CCA', 'CCU', 'UAU', 'CUA', 'AGC', 'UUG', 'CUA', 'CCA', 'AUA', 'AUU', 'AGC', 'AUU', 'UUU', 'GCC', 'UUG', 'CGA', 'CAG', 'ACC', 'UCC', 'UAC', 'UUA', 'GAU', 'UGC', 'CAC', 'ACA', 'UUG', 'AGC', 'UAG', 'UCA', 'GUG', 'AGC', 'GAU', 'AAG', 'CUU', 'GAC', 'GCG', 'CUU', 'UCA', 'AGG', 'GUC', 'GCG', 'AGU', 'ACG', 'UGA', 'ACU', 'AAG', 'GCU', 'CCG', 'GAC', 'AGG', 'ACU', 'AUA', 'UAC', 'UUG', 'GGU', 'UUG', 'AUC', 'UCG', 'CCC', 'CGA', 'CAA', 'CUG', 'CAA', 'ACC', 'UCA', 'ACU', 'UUU', 'UUA', 'GAU', 'UAU', 'AUG', 'GUU', 'AGC', 'CGA', 'AGU', 'UGC', 'ACG', 'AGG', 'UGG', 'CGU', 'CCG', 'CGG', 'ACU', 'GCU', 'CCC', 'CGA', 'GUG', 'UGG', 'CUC', 'UUU', 'CAU', 'CUG', 'ACA', 'ACG', 'UGC', 'AAC', 'CCC', 'UAU', 'CGC', 'GGC', 'CGA', 'UUG', 'UUU', 'CUG', 'CGG', 'ACG', 'AUG', 'UUG', 'UCC', 'UCA', 'UAG', 'UUU', 'GGG', 'CAU', 'GUU', 'UCC', 'CUU', 'GUA', 'GGU', 'GUG', 'AAA', 'CCA', 'CUU', 'AGC', 'UUC', 'GCG', 'CCG', 'UAG', 'UCC', 'CAA', 'UGA', 'AAA', 'ACC', 'UAU', 'GGA', 'CUU', 'UGU', 'UUU', 'GGG', 'UAG', 'CAC', 'CAG', 'GAA', 'UCU', 'GAA', 'CCG', 'UGU', 'GAA', 'UGU', 'GGA', 'CGU', 'CGC', 'GCG', 'CGU', 'AGA', 'CCU', 'UUA', 'UCU', 'CCG', 'GUU', 'CAA', 'GCU', 'AGG', 'GAU', 'GUG', 'GCU', 'GCA', 'UGC', 'UAC', 'GUU', 'GUC', 'ACA', 'CCU', 'ACA', 'CUG', 'CUC', 'GAA', 'GUA', 'AAU', 'AUG', 'CGA', 'AGC', 'GCG', 'CGG', 'CCU', 'GGC', 'CGG', 'AGG', 'CGU', 'UCC', 'GCG', 'CCG', 'CCA', 'CGU', 'GUU', 'CGU', 'UAA', 'CUG', 'UUG', 'AUU', 'GGU', 'GGC', 'ACA', 'UAA', 'GCA', 'AUA', 'UCG', 'UAG', 'UCC', 'GUC', 'AAA', 'UUC', 'AGC', 'UCU', 'GUU', 'AUC', 'CCG', 'GGC', 'GUU', 'AUG', 'UGU', 'CAA', 'AUG', 'GCG', 'UAG', 'AAC', 'GGG', 'AUU', 'GAC', 'UGU', 'UUG', 'ACG', 'GUA', 'GCU', 'GCU', 'GAU', 'CGG', 'UAC', 'GGU', 'AAC', 'GGA', 'GAA', 'UCU', 'GUC', 'GGG', 'CUA', 'UGU', 'CAC', 'UAA', 'UAC', 'UUU', 'CCA', 'AAC', 'GCC', 'CCG', 'UAC', 'CGA', 'UGC', 'UGA', 'ACA', 'AGU', 'CGA', 'UGC', 'AGG', 'CUC', 'CCG', 'UCU', 'UUG', 'AAA', 'AGG', 'GGU', 'AAA', 'CAU', 'ACA', 'AGU', 'GGA', 'UA']
result = amino_converter(codon_sequence)
print(result)