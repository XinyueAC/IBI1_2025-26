import numpy as np
import matplotlib.pyplot as plt 

#基因表达，创建字典
gene_expression = {"TP53":12.4, "EGFR":15.1, "BRCA1":8.2, "PTEN":5.3, "ESR1":10.7}
#添加基因“MYC”及其表达水平,11.6
gene_expression["MYC"] = 11.6


#提取基因名称和表达水平
genes = list(gene_expression.keys())
expression_levels = list(gene_expression.values())

# 生成一个带有标签的条形图，显示所有基因的表达值。
plt.figure(figsize=(10, 6))
plt.bar(genes, expression_levels, color='skyblue')
plt.xlabel('gene')
plt.ylabel('expression level')
plt.title('gene expression levels')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 创建一个代表目标基因的变量，并编写代码打印该基因的表达值。如果该基因不在数据集中，打印一条有信息量的错误消息。不要要求用户输入，你可以创建一个表示所请求活动的变量，该变量可以被修改——只需确保在你的脚本中用伪代码标出该变量的位置。
target_gene = "MYC"  # 这是一个示例变量，可以修改为任何你想查询的基因
#input("请输入你想查询的基因名称：")  # 这里可以替换为直接赋值，例如 target_gene = "TP53"
if target_gene in gene_expression:
    print(f"The expression level of {target_gene} is {gene_expression[target_gene]}.")
else:
    print(f"Gene {target_gene} not found in the dataset.")

#计算所有基因的平均基因表达水平并打印输出。
average_expression = np.mean(expression_levels)
print(f"The average gene expression level is {average_expression:.2f}.")
