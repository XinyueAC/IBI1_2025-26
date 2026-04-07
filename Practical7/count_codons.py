# Practical 7: Task 3 - Codon Frequency
# IBI1, 2025/26

import matplotlib.pyplot as plt

user_stop = input(" please enter a stop codon (TAA, TAG, TGA): ").strip()

codon_count = {}

try:
    # 3. read stop_genes.fa and count codons in the sequences
    with open("stop_genes.fa", 'r') as f:
        for line in f:
            line = line.strip()
            # skip Header line
            if line.startswith('>'):
                continue
            
            # sequence 
            sequence = line
            # step=3
            for i in range(0, len(sequence) - (len(sequence) % 3), 3):
                codon = sequence[i:i+3]
                
                if codon not in codon_count:
                    codon_count[codon] = 0
                codon_count[codon] += 1

    # 4. draw the pie chart using matplotlib
    # check if codon_count is not empty to avoid plotting an empty chart
    if codon_count:
        labels = codon_count.keys()
        sizes = codon_count.values()

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(f'Codon Frequency Distribution for genes with {user_stop}')
        
        # 5. save the figure
        filename = f'{user_stop}_codon_frequency.png'
        plt.savefig(filename)
        plt.close()
        print(f"任务3完成：已生成 {filename}")
    else:
        print("error: can't find any codons to plot. Please check if stop_genes.fa is generated correctly and contains sequences.")

except FileNotFoundError:
    print("error: can't find stop_genes.fa . Please run stop_codons.py first.")
except Exception as e:
    print(f"error: {e}")