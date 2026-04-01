#traditincal approach without regular expressions
# 1. define the RNA sequence
#seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
#start_codon = "AUG"
#stop_codons = ["UAA", "UAG", "UGA"]
#longest_orf = "" # 用来存最长的orf

# 2. scan the sequence for ORFs starting with AUG and ending with the first in-frame stop codon
#for i in range(len(seq)):
#    # find the starting AUG
#    if seq[i:i+3] == start_codon:
        # 3. find the first in-frame stop codon
        # j is starting from i and jumps 3 positions each time (because codons are 3 bases)
#        for j in range(i, len(seq), 3):
#            codon = seq[j:j+3]
            # calculate the current ORF from the start codon to the stop codon (inclusive)
#            if codon in stop_codons:
#                current_orf = seq[i:j+3] # orf the whle ORF includes the stop codon
#                # 4. just compare the length of current ORF with the longest one found so far
#                if len(current_orf) > len(longest_orf):
#                    longest_orf = current_orf
#                break # when we find the first stop codon
# 5. output the longest ORF and its length
#print("最长 ORF:", longest_orf)
#print("长度:", len(longest_orf))




# Alternative approach using regular expressions
#define the RNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
import re
# find all ORFs using regular expression
orfs = re.findall(r'AUG(?:...)*?(?:UAA|UAG|UGA)', seq)
# find the longest ORF
longest_orf = max(orfs, key=len) if orfs else ""
# print the longest ORF and its length
print("Longest ORF:", longest_orf)
print("Length:", len(longest_orf))
