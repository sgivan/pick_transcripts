#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('listfile', help="file containing list of genes to pick transcripts for")
args = parser.parse_args()

listfile = args.listfile



