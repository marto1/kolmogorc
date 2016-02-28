#!/usr/bin/env python3.2
# encoding: utf-8
"""
De/Compress a file using "code blocks"(see Kolmogorov complexity).

compress.py <code blocks file> <output>


It's totally insecure for now as it runs arbitrary code on your machine!!!

compression ratio is really bad for trivial things.
blocks are executed in sequence, ordering matters.


code blocks language support:
Python 3.2

"""
import sys
import configparser as cp

def decompress_py32(path):
    module, func = path.split("/")
    m = __import__(module)
    return vars(m)[func]()

def main():
    config = cp.ConfigParser()
    config.read(sys.argv[1])
    with open(sys.argv[2], "w") as f:
        for sec in config.sections():
            s = config[sec]
            if config[sec]['lang'] == 'py3.2':
                res = decompress_py32(s['decompress'])
                f.write(res)

if __name__ == '__main__':
    main()
