#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from astropy.io import fits
import datetime
import os


class Frames():
    
    time_fmt_iso = "%Y-%m-%d %H:%M:%S.%f"
    time_fmt_date = "%Y-%m-%d"
    time_fmt_time = "%H:%M:%S.%f"
    
    def __init__(self, source):
        self.source = source
        self.headers = {}

        self.read_all_headers()
        pass

    def read_all_headers(self):
        # TODO: Check that we work only with .fits files.

        files = [os.path.join(self.source, f) for f in os.listdir(self.source)
                 if os.path.isfile(os.path.join(self.source, f))]

        for fits_file in files:
            self.headers[fits_file] = fits.getheader(fits_file)

    def get_headers(self):
        """ Vrati slovnik vhondny pro zapis do storage
        """
        result = []
        for k in self.headers:

            #if 'DATE-OBS' in self.headers[k]:
                #print(self.headers[k]['DATE-OBS'])

                    #time = datetime.datetime.strptime(self.headers[k]['TIME-OBS'], "%H:%M:%S.%f")
            #date_time = datetime.datetime.combine(date,time)
            #print(date)
            
            date = datetime.datetime.strptime(self.headers[k]['DATE-OBS']+'  '+
                self.headers[k]['TIME-OBS'], time_fmt_iso)
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
    
    def _check_time_format(self,frame,key,time_format):
        """Return True, if frame has time_format in key.
        """
        try:
            print(datetime.datetime.strptime(frame[key], time_format))
        except ValueError:
            return False
        return True

    # TODO: Napat funkci, ktera rekne so s tim casem....
        
    def check(self):
        """Check if frames are valid => return True.
        """
        mandatory = ['OBJECT','IMAGETYP','FILTER','EXPTIME','OBSERVAT','GAIN',
                    'RA','DEC','DATE-OBS','JD','HJD']
        is_valid = True
        for header in self.headers:

            for key in mandatory:
                if key not in self.headers[header]:
                    print("In file "+header+" missing "+key)
                    is_valid = False

            is_date-obs_iso = self._check_time_format(self.headers[header],'DATE-OBS',Frames.time_fmt_iso)
            if not is_date-obs_iso:
                is_date-obs_date = self._check_time_format(self.headers[header],'DATE-OBS',Frames.time_fmt_date)
                if not is_date-obs_date:
                    is_valid = False
                    print("In header bad values in: DATE-OBS")
                
                is_time-obs_time = self._check_time_format(self.headers[header],'TIME-OBS',Frames.time_fmt_time)
                if not is_time-obs_time:
                    is_valid = False
                    print("In header bad values in: TIME-OBS")
                

        return is_valid
            
"""
datetime.datetime.combine(
datetime.date(
datetime.strptime(self.headers[k]['DATE-OBS'], "%y-%m-%d")),
datetime.timetz(self.headers[k]['TIME-OBS']))
"""
