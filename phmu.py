#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Photometry utils.

Usage:
    phmu.py <input>
    phmu.py (-h | --help)
    phmu.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""

from docopt import docopt
import os
import src.frames


def main(argv):
    
    if not os.path.exists(argv['<input>']):
        print('ERROR: Given path "{0}" isn\'t valid!'.format(argv['<input>']))
        return

    frames = src.frames.Frames(argv['<input>'])

if __name__ == "__main__":
    argv = docopt(__doc__, version='phmu 0.0.1')
    main(argv)
