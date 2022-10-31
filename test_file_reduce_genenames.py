import pandas as pd
from reduce_genenames import reduce_genenames

data = pd.read_csv("/Users/lisiarend/Desktop/Hiwi/proteomics_analysis/data/TMT_data/rat_plasma_diabetic/proteinGroups_filtered_remapped.txt", sep=" ", header=0)
data = data[["Gene names"]]

#data = data[1:10]

data = pd.DataFrame({"Gene names" : ["Mtco2;COXII;Mt-co2;COX2;Co2", "Mt-nd5;Nd5"]})
print(data)

organism = "rat"
mode = "ensembl"
gene_column = "Gene names"
keep_empty = True
HGNC_mode = "mostfrequent"

reduced_data, log_df = reduce_genenames(data=data, organism = organism, mode=mode, gene_column=gene_column, keep_empty=keep_empty, HGNC_mode=HGNC_mode, inplace=False)

print(data)
print(reduced_data)