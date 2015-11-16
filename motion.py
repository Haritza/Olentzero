#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import RPi.GPIO as GPIO
import time,os,pygame,json,httplib
import keys
from panpina import Panpin

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

# olentzero hasten da hitz egiten
olentzerok_hitzegin = True

olentzero = Panpin("Olentzero", keys.OLENTZERO_PARSE_PATH, keys.OLENTZERO_TEXTU_FITXATEGIA, keys.OLENTZERO_AUDIO_FITXATEGIA,keys.OLENTZERO_AHOKO_GPIO_PINA)
maridomingi = Panpin("Maridomingi", keys.MARIDOMINGI_PARSE_PATH, keys.MARIDOMINGI_TEXTU_FITXATEGIA,keys.MARIDOMINGI_AUDIO_FITXATEGIA,keys.MARIDOMINGI_AHOKO_GPIO_PINA)

esaldi_berria = olentzero.get_esaldia()

olentzero.idatzi(esaldi_berria["esaldia"].decode('utf8').encode('iso8859-15'))
maridomingi.idatzi(esaldi_berria["erantzuna"].decode('utf8').encode('iso8859-15'))

# textu fitxategietako hitzak audiora bihurtzen ditu Ahotts-ren bitartez
os.system('sh prozesatu.sh')
olentzero.moztuEsaldia()
maridomingi.moztuEsaldia()

while True:
    current_state = GPIO.input(sensor)
    if current_state:
        # mugimendu sentsoreak norbait detektatzen badu
        if olentzerok_hitzegin: 
            # olentzerori dagokio hitz egitea
            
            olentzero.hitzegin()
            maridomingi.hitzegin()

            olentzerok_hitzegin = False
            
            esaldi_berria = maridomingi.get_esaldia()
            maridomingi.idatzi(esaldi_berria["esaldia"].decode('utf8').encode('iso8859-15'))
            olentzero.idatzi(esaldi_berria["erantzuna"].decode('utf8').encode('iso8859-15'))
        else: 
            # maridomingiri dagokio hitz egitea
            maridomingi.hitzegin()
            olentzero.hitzegin()

            olentzerok_hitzegin = True

            esaldi_berria = olentzero.get_esaldia()
            olentzero.idatzi(esaldi_berria["esaldia"].decode('utf8').encode('iso8859-15'))
            maridomingi.idatzi(esaldi_berria["erantzuna"].decode('utf8').encode('iso8859-15'))

	os.system('sh prozesatu.sh')
    olentzero.moztuEsaldia()
    maridomingi.moztuEsaldia()
        print "minutu bat itxaron"
        time.sleep(60)
    else:
        #ez dago inor
        print "ez dago inor"
