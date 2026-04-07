import re

stop_codons = ["TAA", "TAG", "TGA"]

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f_in, open("stop_genes.fa", "w") as f_out:
    current_header = ""
    current_seq = ""

    # output pattern
    def write_fasta(header, seq, file_handle):
        file_handle.write(f"{header}\n")
        
        for i in range(0, len(seq), 60):
            file_handle.write(f"{seq[i:i+60]}\n")

    for line in f_in:
        line = line.strip()

        if line.startswith(">"):
            # new header,new sequence, but before that we need to check the previous one
            if current_header:
                seq_combined = current_seq.replace("\n", "")

                # find stop codons after the first ATG
                found_stops = []

                # 1. find the index of the first ATG (start codon)
                start_idx = seq_combined.find("ATG")

                if start_idx != -1:
                    # 2. scan through the sequence in steps of 3 (codon by codon) starting from the first ATG
                    for i in range(start_idx + 3, len(seq_combined), 3):
                        codon = seq_combined[i:i+3]
                        if codon in stop_codons:
                            if codon not in found_stops:
                                found_stops.append(codon)

                # 3. write to output if any stop codons found
                if found_stops:
                    # the pattern of the new header 
                    # sort out Gene ID ( >YBR024W_mRNA... -> YBR024W_mRNA)
                    # the first word without ">" is usually the gene ID
                    gene_id = current_header.split()[0].replace(">", "")

                    # piece together the new header with found stop codons
                    # if there are multiple stop codons, join them with underscores
                    new_header = f">{gene_id};{'_'.join(found_stops)}"

                    write_fasta(new_header, seq_combined, f_out)

            # reset for the new sequence
            current_header = line
            current_seq = ""
        else:
            current_seq += line + "\n"

    #the last sequence might not be followed by a new header, so we need to check it after the loop
    if current_header:
        seq_combined = current_seq.replace("\n", "")
        found_stops = []
        start_idx = seq_combined.find("ATG")

        if start_idx != -1:
            for i in range(start_idx + 3, len(seq_combined), 3):
                codon = seq_combined[i:i+3]
                if codon in stop_codons:
                    if codon not in found_stops:
                        found_stops.append(codon)

        if found_stops:
            gene_id = current_header.split()[0].replace(">", "")
            new_header = f">{gene_id};{'_'.join(found_stops)}"
            write_fasta(new_header, seq_combined, f_out)

        #if found_stops:
        #    gene_id = current_header.split()[0].replace(">", "")
        #    stops_str = ";".join(found_stops)
        #    new_header = f">{gene_id};{stops_str}"
        #    write_fasta(new_header, seq_combined, f_out)