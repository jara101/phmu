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

    def add_frames(self, frames):
        pass
