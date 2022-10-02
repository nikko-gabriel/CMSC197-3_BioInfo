#1 COUNTING NUCLEOTIDES
# counts the number of each nucleotide in a string

# 'ss' refers to the dna string

def count_nucleotides(ss):
    # change the string to uppercase (to avoid case sensitivity error)
    # remove all white spaces (to avoid length error) 
    ss = ss.upper().replace(' ','')
    # DNA string ss should be at most 1000 characters long
    if len(ss) > 1000:
        print("The sequence is too long")
    else:
        # use count() method to count number of each nucleotide in the dna string
        count_A = ss.count("A")
        count_C = ss.count("C")
        count_G = ss.count("G")
        count_T = ss.count("T")
        # prints the number of each nucleotide
        print("A\tC\tG\tT")
        print(f"{count_A}\t{count_C}\t{count_G}\t{count_T}")

# testing the count_nucleotides function with the sample_data
sample_data = "BAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_nucleotides(sample_data)



