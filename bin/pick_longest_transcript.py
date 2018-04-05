#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="name of file with format: transcript ID <tab> transcript length")
parser.add_argument("--listfile", help="file containing list of genes to pull transcripts")
parser.add_argument("--verbose", help="verbose output to terminal", action="store_true")
args = parser.parse_args()

infile = args.infile

if (args.listfile):
    listfile = args.listfile
    genef = open(listfile)
    listoutfile = listfile + ".out"
    listoutfilef = open(listoutfile, 'w')

if args.verbose:
    print("opening %s" % infile)

f = open(infile)

outfile = '.'.join((infile, "out"))
if args.verbose:
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
#print("geneID: '%s', length: '%s', transcriptID: '%s'" % ("TRINITY_DN151_c0_g1", sizeMap["TRINITY_DN151_c0_g1"], txptMap["TRINITY_DN151_c0_g1"]))
#print(txptMap["TRINITY_DN151_c0_g1"])

for tid in txptMap.values():
    f_out.write(str(tid) + "\n")

if args.listfile:

    for line in genef:
        geneID = line.rstrip();
        if geneID in txptMap:
            print txptMap[geneID]
            listoutfilef.write(str(txptMap[geneID]) + "\n")

f.close()
f_out.close()

