#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from astropy.io import fits
import os


class Frames():

    def __init__(self, source):
        self.source = source
        self.headers = {}
        
        #self.db_init()
        self.read_all_headers()
        self.save_headers_to_db()
        pass

    def read_all_headers(self):
        # TODO: Check that we work only with .fits files.

        files = [os.path.join(self.source, f) for f in os.listdir(self.source) 
                 if os.path.isfile(os.path.join(self.source, f))]

        for fits_file in files:
            self.headers[fits_file] = fits.getheader(fits_file)

    def save_headers_to_db(self):
        
        for frame in self.headers:
            print(frame, '\t', self.headers[frame]['OBJECT'])
