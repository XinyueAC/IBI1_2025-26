import numpy as np
import matplotlib.pyplot as plt 

#create a dictionary to store gene names and their expression levels
gene_expression = {"TP53":12.4, "EGFR":15.1, "BRCA1":8.2, "PTEN":5.3, "ESR1":10.7}
#add a new gene "MYC" and its expression level"11.6" to the dictionary
gene_expression["MYC"] = 11.6


#select the gene names and their corresponding expression levels from the dictionary and store them in separate lists
genes = list(gene_expression.keys())
expression_levels = list(gene_expression.values())

# create a bar chart to visualize the gene expression levels using matplotlib. Label the x-axis as "gene", the y-axis as "expression level", and give the chart a title "gene expression levels". Rotate the x-axis labels for better readability if necessary.
plt.figure(figsize=(10, 6))
plt.bar(genes, expression_levels, color='skyblue')
plt.xlabel('gene')
plt.ylabel('expression level')
plt.title('gene expression levels')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# allow the user to input a gene name and print the corresponding expression level. If the gene is not found in the dictionary, print a message indicating that the gene is not found.
target_gene = "MYC"  # Others can replace this 
if target_gene in gene_expression:
    print(f"The expression level of {target_gene} is {gene_expression[target_gene]}.")
else:
    print(f"Gene {target_gene} not found in the dataset.")

#calculate and print the average expression level of all the genes in the dictionary.   
average_expression = np.mean(expression_levels)
print(f"The average gene expression level is {average_expression:.2f}.")
