#!/usr/bin/python

file = open("NA12878_high_quality_variant_subset.vcf")

for line in file:
	if not line.startswith("#"):
		split_line = line.rstrip("\r\n").split("\t")
		if float(split_line[5]) > 5000:
			print(line)

file.close()
