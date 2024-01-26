#!/usr/bin/env python
# print_version.py
# written by ChillerDragon
#
# parses BlmapChill version from text tile layer
#
# usage: python print_version.py BlmapChill.map
#
# expected sample output: 184
#

import sys

import twmap

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} map")
    sys.exit(0)

m = twmap.Map(sys.argv[1])

# TXT+Deep (version number text)
txt_tiles = m.groups[17].layers[5].tiles

digits = []
digits.append(txt_tiles[1][4][0])
digits.append(txt_tiles[1][5][0])
digits.append(txt_tiles[1][6][0])
digits.append(txt_tiles[1][7][0])

version_str = ''
for digit in digits:
    if digit == 39:
        version_str += '0'
    else:
        version_str += str(digit - 29)

version = int(version_str)

print(str(version))
