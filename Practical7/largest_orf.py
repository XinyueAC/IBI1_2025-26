# largest_orf.py
def find_longest_orf(seq):
    start_codon = "AUG"
    stop_codons = ["UAA", "UAG", "UGA"]
    longest_length = 0
    
    # 遍历寻找起始密码子
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            # 找到起始点，开始寻找终止密码子
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    # 计算 ORF 长度 (包含起始不包含终止，或者包含都行，通常算核苷酸数)
                    length = j + 3 - i # 包含终止密码子的3个碱基
                    if length > longest_length:
                        longest_length = length
                    break # 找到第一个终止密码子即结束该阅读框
    return longest_length

# 1. 定义变量 seq
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# 2. 调用函数并打印结果
result = find_longest_orf(seq)
print(f"最长ORF的长度为: {result} 个核苷酸")