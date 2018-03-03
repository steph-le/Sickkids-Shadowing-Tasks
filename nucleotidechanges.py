#!/usr/bin/python

file = open("NA12878_high_quality_variant_subset.vcf")

nucleotide_change = {}

for line in file:
	if not line.startswith("#"):
		split_line = line.rstrip("\r\n").split("\t")
		if not split_line[3] == split_line[4]:
			change = '{0}>{1}'.format(split_line[3], split_line[4])
			if change not in nucleotide_change:
				nucleotide_change[change] = 1
			else:
				nucleotide_change[change] +=1

for key in nucleotide_change:
	print('{0} {1}'.format(key, nucleotide_change[key]))

file.close()
