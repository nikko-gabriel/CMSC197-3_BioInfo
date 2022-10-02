#3 Translation RNA into Protein
# translate RNA string into protein string based on rna codon ta

# RNA Codon Dictionary
rna_codon = {   'UUU':'F', 'UCU':'S','UAU':'Y','UGU':'C',
                'UUC':'F', 'UCC':'S','UAC':'Y','UGC':'C',
                'UUA':'L', 'UCA':'S','UAA':'Stop','UGA':'Stop',
                'UUG':'L', 'UCG':'S','UAG':'Stop','UGG':'W',
                
                'CUU':'L', 'CCU':'P','CAU':'H','CGU':'R',
                'CUC':'L', 'CCC':'P','CAC':'H','CGC':'R',
                'CUA':'L', 'CCA':'P','CAA':'Q','CGA':'R',
                'CUG':'L', 'CCG':'P','CAG':'Q','CGG':'R',

                'AUU':'I', 'ACU':'T','AAU':'N','AGU':'S',
                'AUC':'I', 'ACC':'T','AAC':'N','AGC':'S',
                'AUA':'I', 'ACA':'T','AAA':'K','AGA':'R',
                'AUG':'M', 'ACG':'T','AAG':'K','AGG':'R',

                'GUU':'V', 'GCU':'A','GAU':'D','GGU':'G',
                'GUC':'V', 'GCC':'A','GAC':'D','GGC':'G',
                'GUA':'V', 'GCA':'A','GAA':'E','GGA':'G',
                'GUG':'V', 'GCG':'A','GAG':'E','GGG':'G'}

# # check if the rna_codon dict is correct, reviewing dict
# print(rna_codon["GUA"])
# dna_sample = "GCCCAG"
# first_codon = dna_sample[0:3]
# second_codon = dna_sample[-3:]
# print(f"First codon {first_codon} translation is {rna_codon.get(first_codon)},\nSecond codon {second_codon} translation is {rna_codon[second_codon]}")

# 'ss' refers to the rna string
def translate(ss):
    # change the string to uppercase (to avoid case sensitivity error)
    # remove all white spaces (to avoid length error) 
    ss = ss.upper().replace(' ','')
    # rna string ss should be at most 1000 characters long, and should be multiple of 3
    if len(ss) > 10000 or len(ss)%3 != 0:
        print("Invalid RNA sequence length")
    else:
        # store in protein string
        protein = ""
        # reads the rna string 3 nucleotides at a time
        for i in range(0, len(ss), 3):
            #store the codon (3 nucleotides) in a temp variable
            codon = ss[i:i+3]
            # if the codon is in the rna_codon dict, 
            # store in amino variable the corresponding amino acid, 
            # then add to the protein string
            amino = rna_codon.get(codon) #also works with rna_codon[codon]
            # if the amino acid is Stop, stop the translation
            if amino == "Stop":
                break
            else:
                protein += amino
        # prints the translated protein string
        print(protein)

# testing the translate function with the sample_data
sample_data = "AUG GCC AUG G CG CCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
translate(sample_data)