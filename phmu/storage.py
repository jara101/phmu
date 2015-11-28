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
                place TEXT,
                gain REAL,
                ra REAL,
                dec REAL,
                exp_time DATETIME,
                jd REAL,
                hjd REAl
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
                    frame['place'],
                    frame['gain'],
                    frame['ra'],
                    frame['dec'],
                    frame['exp_time'],
                    frame['jd'],
                    frame['hjd']
                    )
            query.append(data)

        conn = sqlite3.connect('phmu.db')
        c = conn.cursor()
        c.executemany('INSERT INTO frames VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', query)
        conn.commit()
        conn.close()
