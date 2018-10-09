#!/usr/bin/env python3
# https://stackoverflow.com/questions/13613336/python-concatenate-text-files
import sys, os

def main():
    assert len(sys.argv)==3
    indir = sys.argv[1]
    outdir = sys.argv[2]

    with open(os.path.join(outdir, 'ref.bib'), 'w') as outfile:
        for fname in os.listdir(indir):
            with open(os.path.join(indir, fname), 'r') as infile:
                outfile.write(infile.read())

if __name__ == '__main__':
    main()
