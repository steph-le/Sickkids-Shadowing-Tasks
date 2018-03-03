#!/usr/bin/python

file = open("NA12878_high_quality_variant_subset.vcf")

for line in file:
	if not line.startswith("#"):
		split_line = line.rstrip("\r\n").split("\t")
		if "," in split_line[4]:
			print(line)

file.close()
