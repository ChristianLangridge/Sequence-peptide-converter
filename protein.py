"Installation of Biopython"

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

# Example usage
protein_seq = "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"  # test sequence with Human Insulin Uniprot
get_alphafold_prediction(protein_seq)