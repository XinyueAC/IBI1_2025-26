#seq1="MLSRAVCGT"
#seq2="MLCRAACST"
#edit_distance=0 #set	initial	distance	as	zero
#for	i in range(len(seq1)): #compare	each	amino	acid
#		if	seq1[i]!=seq2[i]:		
#		    edit_distance+=1 #add	 a	 score	 1	 if	 amino	 acids	 are	different
#print(edit_distance)



# alignment.py
# 实验13：简单的序列比对程序

# 1. 定义 BLOSUM62 矩阵 (部分核心数据，足够运行)
# 这是一个字典，里面嵌套了字典
blosum62 = {
    'A': {'A': 4, 'R': -1, 'N': -2, 'D': -2, 'C': 0, 'Q': -1, 'E': -1, 'G': 0, 'H': -2, 'I': -1, 'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1, 'T': 0, 'W': -3, 'Y': -2, 'V': 0},
    'R': {'A': -1, 'R': 5, 'N': 0, 'D': -2, 'C': -3, 'Q': 1, 'E': 0, 'G': -2, 'H': 0, 'I': -3, 'L': -2, 'K': 2, 'M': -1, 'F': -3, 'P': -2, 'S': -1, 'T': -1, 'W': -3, 'Y': -2, 'V': -3},
    'N': {'A': -2, 'R': 0, 'N': 6, 'D': 1, 'C': -3, 'Q': 0, 'E': 0, 'G': 0, 'H': 1, 'I': -3, 'L': -3, 'K': 0, 'M': -2, 'F': -3, 'P': -2, 'S': 1, 'T': 0, 'W': -4, 'Y': -2, 'V': -3},
    'D': {'A': -2, 'R': -2, 'N': 1, 'D': 6, 'C': -3, 'Q': 0, 'E': 2, 'G': -1, 'H': 0, 'I': -3, 'L': -4, 'K': -1, 'M': -3, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -4, 'Y': -3, 'V': -3},
    'C': {'A': 0, 'R': -3, 'N': -3, 'D': -3, 'C': 9, 'Q': -3, 'E': -4, 'G': -3, 'H': -3, 'I': -1, 'L': -1, 'K': -3, 'M': -1, 'F': -2, 'P': -3, 'S': -1, 'T': -1, 'W': -2, 'Y': -2, 'V': -1},
    'Q': {'A': -1, 'R': 1, 'N': 0, 'D': 0, 'C': -3, 'Q': 5, 'E': 2, 'G': -2, 'H': 0, 'I': -3, 'L': -2, 'K': 1, 'M': -1, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -2, 'Y': -2, 'V': -2},
    'E': {'A': -1, 'R': 0, 'N': 0, 'D': 2, 'C': -4, 'Q': 2, 'E': 5, 'G': -2, 'H': 0, 'I': -3, 'L': -3, 'K': 1, 'M': -2, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -3, 'Y': -2, 'V': -2},
    'G': {'A': 0, 'R': -2, 'N': 0, 'D': -1, 'C': -3, 'Q': -2, 'E': -2, 'G': 6, 'H': -2, 'I': -4, 'L': -4, 'K': -2, 'M': -3, 'F': -3, 'P': -2, 'S': 0, 'T': -2, 'W': -2, 'Y': -3, 'V': -3},
    'H': {'A': -2, 'R': 0, 'N': 1, 'D': 0, 'C': -3, 'Q': 0, 'E': 0, 'G': -2, 'H': 8, 'I': -3, 'L': -3, 'K': -1, 'M': -2, 'F': -1, 'P': -2, 'S': -1, 'T': -2, 'W': -2, 'Y': 2, 'V': -3},
    'I': {'A': -1, 'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -3, 'E': -3, 'G': -4, 'H': -3, 'I': 4, 'L': 2, 'K': -3, 'M': 1, 'F': 0, 'P': -3, 'S': -2, 'T': -1, 'W': -3, 'Y': -1, 'V': 3},
    'L': {'A': -1, 'R': -2, 'N': -3, 'D': -4, 'C': -1, 'Q': -2, 'E': -3, 'G': -4, 'H': -3, 'I': 2, 'L': 4, 'K': -2, 'M': 2, 'F': 0, 'P': -3, 'S': -2, 'T': -1, 'W': -2, 'Y': -1, 'V': 1},
    'K': {'A': -1, 'R': 2, 'N': 0, 'D': -1, 'C': -3, 'Q': 1, 'E': 1, 'G': -2, 'H': -1, 'I': -3, 'L': -2, 'K': 5, 'M': -1, 'F': -3, 'P': -1, 'S': 0, 'T': -1, 'W': -3, 'Y': -2, 'V': -2},
    'M': {'A': -1, 'R': -1, 'N': -2, 'D': -3, 'C': -1, 'Q': -1, 'E': -2, 'G': -3, 'H': -2, 'I': 1, 'L': 2, 'K': -1, 'M': 5, 'F': 0, 'P': -2, 'S': -1, 'T': -1, 'W': -1, 'Y': -1, 'V': 1},
    'F': {'A': -2, 'R': -3, 'N': -3, 'D': -3, 'C': -2, 'Q': -3, 'E': -3, 'G': -3, 'H': -1, 'I': 0, 'L': 0, 'K': -3, 'M': 0, 'F': 6, 'P': -3, 'S': -2, 'T': -2, 'W': 1, 'Y': 3, 'V': -1},
    'P': {'A': -1, 'R': -2, 'N': -2, 'D': -1, 'C': -3, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -3, 'L': -3, 'K': -1, 'M': -2, 'F': -3, 'P': 7, 'S': -1, 'T': -1, 'W': -4, 'Y': -3, 'V': -2},
    'S': {'A': 1, 'R': -1, 'N': 1, 'D': 0, 'C': -1, 'Q': 0, 'E': 0, 'G': 0, 'H': -1, 'I': -2, 'L': -2, 'K': 0, 'M': -1, 'F': -2, 'P': -1, 'S': 4, 'T': 1, 'W': -3, 'Y': -2, 'V': -2},
    'T': {'A': 0, 'R': -1, 'N': 0, 'D': -1, 'C': -1, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -1, 'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S': 1, 'T': 5, 'W': -2, 'Y': -2, 'V': 0},
    'W': {'A': -3, 'R': -3, 'N': -4, 'D': -4, 'C': -2, 'Q': -2, 'E': -3, 'G': -2, 'H': -2, 'I': -3, 'L': -2, 'K': -3, 'M': -1, 'F': 1, 'P': -4, 'S': -3, 'T': -2, 'W': 11, 'Y': 2, 'V': -3},
    'Y': {'A': -2, 'R': -2, 'N': -2, 'D': -3, 'C': -2, 'Q': -2, 'E': -2, 'G': -3, 'H': 2, 'I': -1, 'L': -1, 'K': -2, 'M': -1, 'F': 3, 'P': -3, 'S': -2, 'T': -2, 'W': 2, 'Y': 7, 'V': -1},
    'V': {'A': 0, 'R': -3, 'N': -3, 'D': -3, 'C': -1, 'Q': -2, 'E': -2, 'G': -3, 'H': -3, 'I': 3, 'L': 1, 'K': -2, 'M': 1, 'F': -1, 'P': -2, 'S': -2, 'T': 0, 'W': -3, 'Y': -1, 'V': 4}
}
# 2. 定义读取 FASTA 文件的函数
def read_fasta(file_path):
    sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):  # 跳过标题行
                continue
            else:
                sequence += line.strip() # 去掉空格和换行符
    return sequence

# 3. 定义比对函数
def align_sequences(seq1, seq2, matrix):
    if len(seq1) != len(seq2):
        print("警告：序列长度不同！将按较短的序列计算。")
    
    min_len = min(len(seq1), len(seq2))
    total_score = 0
    identical_count = 0
    
    print(f"\n--- 正在比对 ---")
    print(f"序列 1: {seq1[:30]}...") # 打印前30个字符预览
    print(f"序列 2: {seq2[:30]}...")
    
    for i in range(min_len):
        aa1 = seq1[i]
        aa2 = seq2[i]
        
        # 查表得分
        # 如果氨基酸不在标准20种内（比如X或*），给个默认低分或跳过
        if aa1 in matrix and aa2 in matrix[aa1]:
            score = matrix[aa1][aa2]
        else:
            score = -1 # 未知字符惩罚
        
        total_score += score
        
        # 统计完全相同的氨基酸
        if aa1 == aa2:
            identical_count += 1
    
    identity_percent = (identical_count / min_len) * 100
    
    return total_score, identity_percent, min_len

# 4. 主程序入口
if __name__ == "__main__":
    print("实验13：简单序列比对程序开始运行...\n")
    
    # 读取三个文件 (请确保这三个文件和你的py文件在同一个文件夹里)
    try:
        human_seq = read_fasta('human_dlx5.fasta')
        mouse_seq = read_fasta('mouse_dlx5.fasta')
        random_seq = read_fasta('random_seq.fasta')
        
        print(f"人类序列长度: {len(human_seq)}")
        print(f"小鼠序列长度: {len(mouse_seq)}")
        print(f"随机序列长度: {len(random_seq)}")
        
        # 执行三组比对
        # 1. 人类 vs 小鼠
        score1, id1, length1 = align_sequences(human_seq, mouse_seq, blosum62)
        print(f"【人类 vs 小鼠】 得分: {score1}, 相同性: {id1:.2f}%, 长度: {length1}")
        
        # 2. 人类 vs 随机
        score2, id2, length2 = align_sequences(human_seq, random_seq, blosum62)
        print(f"【人类 vs 随机】 得分: {score2}, 相同性: {id2:.2f}%, 长度: {length2}")
        
        # 3. 小鼠 vs 随机
        score3, id3, length3 = align_sequences(mouse_seq, random_seq, blosum62)
        print(f"【小鼠 vs 随机】 得分: {score3}, 相同性: {id3:.2f}%, 长度: {length3}")
        
        # 5. 结果分析 (回答实验问题)
        print("\n--- 结果分析 ---")
        print("1. 人类和小鼠的序列得分和相同性都非常高，说明它们有很近的亲缘关系（同源）。")
        print("2. 人类/小鼠与随机序列的得分很低（甚至为负），说明随机序列没有任何生物学关联。")
        print("3. 结论：人类和小鼠的 DLX5 蛋白在进化上是高度保守的。")
        
    except FileNotFoundError as e:
        print(f"错误：找不到文件。请检查文件名是否正确，且文件是否在当前目录下。")
        print(f"报错详情: {e}")