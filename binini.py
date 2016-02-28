#!/usr/bin/env python3.2
# encoding: utf-8
"""
Converts a text block file to a binary representation, 
togheter with the source paths.

You should never have to write binary blocks directly.

binini.py <code blocks file> <output>

ALWAYS big endian.
Blocks are ALWAYS anonymous. The tag in between [] is ignored

Blocks are mapped in the following way:
note: X -> byte slot; ... -> repeatance
note: ! -> \x10 ; @ -> \x11

! <- beginning of block
  @ <- beginning of clause
   X <- clause code(1 unsigned byte)
   XX <- value length(2 unsigned bytes)
   X... <- value (unsigned bytes)
  @ <- end of clause
! <- end of block/beginning of next block

...
EOF <- end of file/end of last block 
"""

import configparser as cp
import sys
import struct

clauses = {"decompress":"d",
           "lang": "l"}
vallen = "!H"

def main(): #TODO REFACTOR
    config = cp.ConfigParser()
    config.read(sys.argv[1])
    with open(sys.argv[2], "w") as f:
        for sec in config.sections():
            res = "\x10"
            s = config[sec]
            for cl, val in s.iteritems():
                res += "\x11" + clauses[cl]
                res += struct.pack(vallen, len(val))
                res += val
            f.write(res)
            


if __name__ == '__main__':
    main()
