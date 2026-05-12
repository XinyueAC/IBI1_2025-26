



import matplotlib.pyplot as plt

user_stop = input("Enter a stop codon (TAA, TAG, TGA): ").strip().upper()
codon_count = {}

try:
    with open("stop_genes.fa") as f:
        current_seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if user_stop not in line:
                    current_seq = ""
                    continue
                if current_seq:
                    start = current_seq.find("ATG")
                    if start != -1:
                        longest_orf = ""
                        for i in range(start, len(current_seq), 3):
                            if current_seq[i:i+3] == "ATG":
                                for j in range(i, len(current_seq), 3):
                                    c = current_seq[j:j+3]
                                    if c == user_stop:
                                        orf = current_seq[i:j]
                                        if len(orf) > len(longest_orf):
                                            longest_orf = orf
                                        break
                        for k in range(0, len(longest_orf) - len(longest_orf)%3, 3):
                            codon = longest_orf[k:k+3]
                            codon_count[codon] = codon_count.get(codon, 0) + 1
                current_seq = ""
            else:
                current_seq += line

    if codon_count:
        plt.figure(figsize=(8,8))
        plt.pie(codon_count.values(), labels=codon_count.keys(), autopct='%1.1f%%')
        plt.title(f'Codon Frequency for stop codon {user_stop}')
        plt.savefig(f'{user_stop}_codon_frequency.png')
        plt.close()
        print(f"File saved: {user_stop}_codon_frequency.png")
    else:
        print("No codons counted.")

except FileNotFoundError:
    print("Error: Please run stop_codons.py first.")
except Exception as e:
    print(f"Error: {e}")