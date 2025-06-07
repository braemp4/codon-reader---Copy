
import pandas as pd


codons_df = pd.read_csv("Codons - Sheet1.csv")

#print(codons_df)
codon_keys = list(codons_df["UUU"])
#print(codon_keys)
codons_df = codons_df.transpose()


codons_df.columns= codon_keys
#print(codons_df.index)
codons_df = codons_df.drop(index="UUU")

codons_df.index = ["Residue: "]
#print(codons_df["AUG"])
#print(codons_df.columns)
codons_df.astype(str)

#print(codons_df["GUC"])

def translate_seq(sequence):
        #first split into triplets
    triplets = []
    for i in range(0, len(sequence.upper()), 3):
        triplets.append(sequence.upper()[i:i+3])
        
        #but what if a string is not divisible by 3? 
    residues = []
    for codon in triplets:
        if len(codon) == 3 and codon in codon_keys:
            if codons_df[codon][0] != "STOP":
                residues.append(codons_df[codon][0])
            elif codons_df[codon][0] == "STOP":
                return residues
    return residues
#I need to convert all dataframe entries into dtype string instead of dt object - notice the residues dont have quotation marks
#print(translate_seq("AUCAUG"))


