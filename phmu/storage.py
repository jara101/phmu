#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


class Storage():

    def __init__(self):
        self.db_init()

    def db_init(self):
        conn = sqlite3.connect('phmu.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE frames (
                filename TEXT,
                name TEXT,
                obj_type TEXT,
                filter TEXT,
                exp_duration REAL,
                place TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def add_frames(self, frames):
        
        query = []
        
        for frame in frames:
            data = (frame['filename'],
                    frame['name'],
                    frame['obj_type'],
                    frame['filter'],
                    frame['exp_duration'],
                    frame['place']
                    #frame['exp_time']                  
                    )
            query.append(data)
       
        conn = sqlite3.connect('phmu.db')
        c = conn.cursor()
        c.executemany('INSERT INTO frames VALUES (?,?,?,?,?,?)', query)
        conn.commit()
        conn.close()
        
"""
                exp_time DATETIME,
                gain REAL,
                ra REAL,
                dec REAL,
                jd REAL,
                hjd REAl
"""
