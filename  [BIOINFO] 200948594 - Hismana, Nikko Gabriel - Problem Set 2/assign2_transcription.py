#2 Transcribing DNA into RNA
# An RNA string is formed from alphabet containing A, C, G, U (U replaces T from the DNA string)

# 'tt' refers to the dna string
# 'uu' refers to the rna string
def transcribe(tt):
    # change the string to uppercase (to avoid case sensitivity error)
    # remove all white spaces (to avoid length error) 
    tt = tt.upper().replace(' ','')
    # DNA string ss should be at most 1000 characters long
    if len(tt) > 1000:
        print("The sequence is too long")
    else:
        # use replace() method to replace T with U
        uu = tt.replace("T", "U")
        # prints the transcribed RNA string
        print(uu)

# testing the transcribe function with the sample_data
sample_data = "GATGGAACTTGACTACGTAAATT"
transcribe(sample_data)