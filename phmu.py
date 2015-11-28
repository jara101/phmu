#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Photometry utils.

Usage:
    phmu.py <input>
    phmu.py check <input>
    phmu.py (-h | --help)
    phmu.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""

from docopt import docopt
import os
import phmu.frames
import phmu.storage

def main(argv):
    
    if not os.path.exists(argv['<input>']):
        print('ERROR: Given path "{0}" isn\'t valid!'.format(argv['<input>']))
        return

    if argv['check']:
        frames = phmu.frames.Frames(argv['<input>'])
        print(frames.check())
        return
            

    storage = phmu.storage.Storage()
    frames = phmu.frames.Frames(argv['<input>'])
    storage.add_frames(frames.get_headers())

if __name__ == "__main__":
    argv = docopt(__doc__, version='phmu 0.0.1')
    main(argv)
