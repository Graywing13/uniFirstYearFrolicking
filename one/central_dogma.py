DNA_to_mRNA = {"A": "U", "T": "A", "G": "C", "C": "G"}
codons = {"phe": ["UUU", "UUC"],
          "leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
          "ile": ["AUU", "AUC", "AUA"],
          "met": ["AUG"],
          "val": ["GUU", "GUC", "GUA", "GUG"],
          "ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
          "pro": ["CCU", "CCC", "CCA", "CCG"],
          "thr": ["ACU", "ACC", "ACA", "ACG"],
          "ala": ["GCU", "GCC", "GCA", "GCG"],
          "tyr": ["UAU", "UAC"],
          "STOP": ["UAA", "UAG", "UGA"],
          "his": ["CAU", "CAC"],
          "gln": ["CAA", "CAG"],
          "asn": ["AAU", "AAC"],
          "lys": ["AAA", "AAG"],
          "asp": ["GAU", "GAC"],
          "glu": ["GAA", "GAG"],
          "cys": ["UGU", "UGC"],
          "trp": ["UGG"],
          "arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
          "gly": ["GGU", "GGC", "GGA", "GGG"]}

"""################FUNCTIONS################"""

def transcription(DNA_string):
    DNA = DNA_string.upper()
    print("Entered Strand: " + DNA)
    mRNA = ""
    for base in DNA:
        complimentary = (DNA_to_mRNA.get(base))
        if complimentary == None:
            return ("Error at base {}: value {} is not in [A, T, C, G]".format((1+ DNA.index(base)), base))
        mRNA += complimentary
    return mRNA

def find_start_codon(mRNA_string):
    start_codon_pos = None
    bases_read = 0
    while (len(mRNA_string) > 0):
        for base in mRNA_string:
            if (base == "A"):
                if (mRNA_string[0:3] == "AUG"):
                    print("First base of start codon is at: {}".format(bases_read + 1))
                    return bases_read
            bases_read += 1
            mRNA_string = mRNA_string[1:]
    return "No Start Codon Found"

def translation(mRNA_string):
    coding_mRNA = find_start_codon(mRNA_string)
    reading_frame_current_codon = mRNA_string[coding_mRNA:(coding_mRNA+3)]
    if 
    

print(transcription("atatatat"))
print(transcription("acab"))
print(transcription("atCGaGcgAT"))
print(transcription(""))
print(translation("AUG"))
print(translation("AAAUG"))
print(translation("AUGAUG"))