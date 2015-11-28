#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from astropy.io import fits
import datetime
import os


class Frames():

    def __init__(self, source):
        self.source = source
        self.headers = {}

        #self.db_init()
        self.read_all_headers()
        #self.save_headers_to_db()
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


    def get_headers(self):
        """ Vrati slovnik vhondny pro zapis do storage
        """
        result = []
        for k in self.headers:

            #if 'DATE-OBS' in self.headers[k]:
                #print(self.headers[k]['DATE-OBS'])

                    #time = datetime.datetime.strptime(self.headers[k]['TIME-OBS'], "%H:%M:%S.%f")
            date = datetime.datetime.strptime(self.headers[k]['DATE-OBS']+'  '+
                self.headers[k]['TIME-OBS'], "%Y-%m-%d %H:%M:%S.%f")
            #date_time = datetime.datetime.combine(date,time)
            #print(date)

            jd = 0.0
            hjd = 0.0

            result.append({'filename':k,
                            'name':self.headers[k]['OBJECT'],
                            'obj_type':self.headers[k]['IMAGETYP'],
                            'filter':self.headers[k]['FILTER'],
                            'exp_duration':self.headers[k]['EXPTIME'],
                            'place':self.headers[k]['OBSERVAT'],
                            'gain':self.headers[k]['GAIN'],
                            'ra':self.headers[k]['RA'],
                            'dec':self.headers[k]['DEC'],
                            'exp_time': date,
                            'jd':jd,
                            'hjd':hjd
                            })
        return result
"""
datetime.datetime.combine(
datetime.date(
datetime.strptime(self.headers[k]['DATE-OBS'], "%y-%m-%d")),
datetime.timetz(self.headers[k]['TIME-OBS']))
"""
