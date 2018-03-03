#!/usr/bin/python

file = open(raw_input("Filename: "))

print("1" + "\t" + "30366" + "\t" + "30503")

for line in file:
	if not line.startswith("#"):
		split_line = line.rstrip("\r\n").split("\t")
		if str(split_line[0]) == "X":
			new_line = "1" + "\t" + str(int(split_line[1])-9000000) + "\t" + str(int(split_line[1]) + 1-9000000)
			print(new_line)

