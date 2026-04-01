# stop_codons.py
def contains_inframe_stop(sequence):
    start = "ATG"
    stops = ["TAA", "TAG", "TGA"]
    
    # 查找起始密码子
    start_pos = sequence.find(start)
    if start_pos == -1:
        return None # 没有起始密码子
    
    # 从起始位置开始，按密码子读取
    for i in range(start_pos, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in stops:
            return codon # 返回找到的终止密码子类型
    return None # 有起始但无终止

def process_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        header = ""
        seq = ""
        
        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                # 处理上一条序列（如果有）
                if seq:
                    stop_codon_found = contains_inframe_stop(seq)
                    if stop_codon_found:
                        # 简化Header，只保留基因名和终止密码子信息
                        # 这里假设基因名在 > 后第一个空格前
                        gene_id = header.split()[0][1:] 
                        new_header = f">{gene_id}_{stop_codon_found}\n"
                        outfile.write(new_header)
                        outfile.write(seq + '\n')
                
                # 读取新序列的Header
                header = line
                seq = ""
            else:
                seq += line # 拼接多行序列
        
        # 循环结束后，别忘了处理最后一条序列
        if seq:
            stop_codon_found = contains_inframe_stop(seq)
            if stop_codon_found:
                gene_id = header.split()[0][1:]
                new_header = f">{gene_id}_{stop_codon_found}\n"
                outfile.write(new_header)
                outfile.write(seq + '\n')

# 调用函数 (请确保文件名与下载的完全一致)
process_fasta('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'stop_genes.fa')
print("处理完成，结果已保存至 stop_genes.fa")