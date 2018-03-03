#!/usr/bin/python

file = open("NA12878_high_quality_variant_subset.vcf")

indels = []

for line in file:
	if not line.startswith("#"):
		split_line = line.rstrip("\r\n").split("\t")
		if not len(split_line[3])==len(split_line[4]):
			print(line)

file.close()
