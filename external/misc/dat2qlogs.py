#!/usr/bin/env python

import argparse, os, re, struct, sys

def main():
    parser = argparse.ArgumentParser(description="Parses out quest logs from a Twilight Princess savefiles")
    parser.add_argument("wsd", help="A valid twilight princess save data file extracted from a savefile (data.bin)")
    wsdbytes = None
    args = parser.parse_args()
    file_in = args.wsd
    with open(file_in,"rb") as wsdfile:
        wsdbytes = bytearray(wsdfile.read())
    
    qlog1 = wsdbytes[0x0008:0x0A9B]
    qlog2 = wsdbytes[0x0A9C:0x152F]
    qlog3 = wsdbytes[0x1530:0x1FC3]

    with open("qlog1.bin", "wb") as outfile:
        outfile.write(qlog1)

    with open("qlog2.bin", "wb") as outfile:
        outfile.write(qlog2)

    with open("qlog3.bin", "wb") as outfile:
        outfile.write(qlog3)
    
if __name__ == "__main__":
    main()