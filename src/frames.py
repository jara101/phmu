#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from astropy.io import fits
import os
import sqlite3


class Frames():

    def __init__(self, source):
        self.source = source
        self.headers = {}
        
        self.db_init()
        self.read_all_headers()
        self.save_headers_to_db()
        pass

    def db_init(self):
        conn = sqlite3.connect('phmu.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE frames (
                id INT PRIMARY KEY,
                filename TEXT,
                name TEXT,
                obj_type TEXT,
                filter TEXT,
                exp_duration REAL,
                place TEXT,
                exp_time DATETIME,
                gain REAL,
                ra REAL,
                dec REAL,
                jd REAL,
                hjd REAl
            )
        ''')
        conn.commit()
        conn.close()
        

    def read_all_headers(self):
        # TODO: Check that we work only with .fits files.

        files = [os.path.join(self.source, f) for f in os.listdir(self.source) 
                 if os.path.isfile(os.path.join(self.source, f))]

        for fits_file in files:
            self.headers[fits_file] = fits.getheader(fits_file)

    def save_headers_to_db(self):
        
        for frame in self.headers:
            print(frame, '\t', self.headers[frame]['OBJECT'])

