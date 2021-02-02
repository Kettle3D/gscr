#!/bin/python3
# GSCR Version 1 for Python

import glob
import copy
import sys
import os

args = copy.deepcopy(sys.argv)
del args[0]
files   = []
rfiles  = []
prgargs = []
eatArgs = True
logo    = True

specialArgs = [
    "--nologo",
    "--help",
    "-n",
    "-h"
]

for arg in args:
    if arg == '--':
        if eatArgs:
            eatArgs = False
        else:
            prgargs += ['--']
    elif eatArgs:
        if arg not in specialArgs:
            files += [arg]
        elif arg in ['-h', '--help']:
            print("""\
\x1b[0;1;96m\
╓──────────────────────────────────────────────────────╖
║    gscr ─ A highly modular GUI scripting language    ║
║                    Built-in help                     ║
╟──────────────────────────────────────────────────────╢
\x1b[0;1;92m\
║                                                      ║
║ Usage: gscr [OPTIONS] [FILE...] [-- PROGRAM OPTIONS] ║
║                                                      ║
║ Valid options:                                       ║
║   -h --help     Show this help text                  ║
║   -n --nologo   Don't show a banner when you start   ║
║                 the program                          ║
║                                                      ║
╙──────────────────────────────────────────────────────╜\
\x1b[0m""")
            sys.exit(0)
        elif arg in ['-n', '--nologo']:
            logo = False
    else:
        prgargs += [arg]

if logo: # Disable the banner with the -n command line flag.
    print("""\x1b[0;1m\
┌────────────────────────────────────────┐
│ Made for                               │
│   _____     ____    ______   _______   │
│  / ____\\   / __ \\  /  ___/  |  ___  \\  │
│ / /        | ||_| /  /      | |___| |  │
│ | |  __    \\__ \\  |  |      |    ___/  │
│ | | |_ |    _ \\ \\ |  |      | |\\ \\     │
│ \\ \\__| |   | L| | \\  \\___   | | \\ \\    │
│  \\_____/   \\___/   \\_____\\  |_|  \\_\\   │
│ Graphical Programming. Made Easy.      │
│ https://github.com/Kettle3D/gscr       │
└────────────────────────────────────────┘\
\x1b[0m""")

if len(files) == 0:
    sys.stderr.write('\x1b[0;1;31mError: No input files specified. For help, type gscr --help.\x1b[0m\n')
    sys.exit(1)

for file in files:
    if os.path.exists(file):
        rfiles += [file]
    else:
        sys.stderr.write("\x1b[0;1;31mError: %s: file not found\x1b[0m\n" % file)

for file in [os.getenv('HOME') + '/.config/gscr.d/base' if 
    os.path.exists(os.getenv('HOME') + '/.config/gscr.d/base') else ''
]+ glob.glob(
    os.getenv('HOME') + '/.config/gscr.d/*.base'
) + glob.glob(
    os.getenv('HOME') + '/.config/gscr.d/*.dep1'
) + glob.glob(
    os.getenv('HOME') + '/.config/gscr.d/*.dep2'
) + glob.glob(
    os.getenv('HOME') + '/.config/gscr.d/*.dep3'
):
    if file != '':
        with open(file) as f:
            exec(f.read())