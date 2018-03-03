#!/usr/bin/python

file = open("NA12878_high_quality_variant_subset.vcf")

gene_names = {}
for line in file:
	if not line.startswith("#"):
		line = line.rstrip("\r\n").split("\t")
	if "GENE=" in line[7]:
		line = line[7].split(";")
		gene = line[-1]
		gene = gene[5:]
		if gene not in gene_names:
			gene_names[gene] = 1
		else:
			gene_names[gene] = gene_names[gene] + 1
for key in gene_names:
	print('{0} {1}'.format(key, gene_names[key]))

file.close()	
