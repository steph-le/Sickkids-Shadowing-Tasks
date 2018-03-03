# Sickkids-Shadowing-Tasks
These are files I created and worked on while I was shadowing a Bioinformatician at Sickkids.

VCF FILE WORK

Task for indels.py

With a one line Unix command, find the number of variants.

Task for multiallelic.py

Extract all the multi-allelic sites (the ones that have a comma in the ALT field), you can either print them to the screen or keep the output in a new file.

Task for genevariants.py

Make a list of gene names in the first column and in the second column how many variants was found per each gene.

Task for nucleotidechanges.py

Make a list of nucleotide changes and how many of each, for example:
C>T   3645
G>A  1432

Task for qual5000.py

Make a VCF file with QUAL field bigger than 5000


BAM WORK

Task for readsatlocation.py (commannd line task)

General command to read numbers at a specific location using samtools


PATIENT RELATED FILE TASKS


Create a subset VCF file consisting only of header lines and chromosome 1 using two methods: 
Unix commands (e.g. Grep)
Bcftools (note: requires compressing the vcf file with bgzip)
Create a new VCF file with only the first 5 columns of each variant (i.e. CHROM  POS     ID      REF     ALT)
Extract all the variants that have at the homozygous ALT (1/1) genotype
With a one line Unix command, list how many variants are found for each chromosome
Add ‘chr’ to the CHROM feld (so “1” should read “chr1”, “2” should read “chr2”, etc.)

Obtain statistics about your VCF file using bcftools (hint: see which command provides stats)
Compress and index your vcf file (need to load tabix module and then use bgzip to compress first)
Use “bcftools view” to extract variants in chromosome 1 between 43500000 and 46500000

Show the header lines
Extract region chr22:10000000-30000000 from your BAM file and save it to another BAM file
Obtain the first 100 reads from the BAM files and save them into another file
Obtain all the reads from the BAM file that cover position chr22:16132160-16132190
