#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="name of file with format: transcript ID <tab> transcript length")
args = parser.parse_args()

infile = args.infile

print("opening %s" % infile)

f = open(infile)

outfile = '.'.join((infile, "out"))
print("creating output file: '%s'" % outfile)
f_out = open(outfile, 'w')

sizeMap = {}
txptMap = {}

for line in f:
#    print(line.rstrip())
    vals = line.rstrip().split("\t")
#    print vals[0]

    txptvals = vals[0].split("_")
    geneID = '_'.join(txptvals[0:4])
#    print("geneid: '%s'" % geneID)

    if geneID in sizeMap:
        if int(sizeMap[geneID]) < int(vals[1]):
            sizeMap[geneID] = vals[1]
            txptMap[geneID] = vals[0]
    else:
        sizeMap[geneID] = vals[1]
        txptMap[geneID] = vals[0]

#print(sizeMap)
print("geneID: '%s', length: '%s', transcriptID: '%s'" % ("TRINITY_DN151_c0_g1", sizeMap["TRINITY_DN151_c0_g1"], txptMap["TRINITY_DN151_c0_g1"]))
print(txptMap["TRINITY_DN151_c0_g1"])


for tid in txptMap.values():
    f_out.write(str(tid) + "\n")

f.close()
f_out.close()

