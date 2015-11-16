#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import RPi.GPIO as GPIO
import time,os,pygame,json,httplib,datetime,urllib,random
from keys import PARSE_API_KEY,PARSE_APP_ID,TXAPA,TXAPAREN_IRAUPENA
from pydub import AudioSegment

class Panpin:
    # panpin guztien ahoen gpio pinak gordetzen ditu
    gpio_pinak = []
    def __init__(self,izena,parse_api_class,textu_fitxategia,audio_fitxategia,gpio_pin):
        
        #    izena: panpinaren izena: Instantziaren izena adib: 'Olentzero'
        #    parse_api_class: Parseko apiaren url-a adib: '/1/classes/Olentzero'
        #    textu_fitxategia: panpin honi dagokion textu fitxagegiaren izena adib: 'olentzero.txt'
        #    audio_fitxategia: panpin honi dagokion audio fitxategiaren izena adib: 'olentzero.wav'
        #    gpio_pin: panpin honen ahoari dagokion gpio pina adib: 17

        self.izena = izena
        self.parse_api_class = parse_api_class
        self.textu_fitxategia = textu_fitxategia
        self.audio_fitxategia = audio_fitxategia
        self.gpio_pin = gpio_pin
        GPIO.setup(gpio_pin, GPIO.OUT)
        GPIO.output(gpio_pin, False)
        Panpin.gpio_pinak.append(gpio_pin)
        self.esaldi_berriak()

    def hitzegin(self):

        #    panpinak bere audio fitxategia
        #    irakurri eta dagokion led-a pizten du
        #    hitz egiten duen bitartean

        for pin in Panpin.gpio_pinak:
            GPIO.output(pin, False)

        pygame.mixer.init(17000)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load(self.audio_fitxategia)
        pygame.mixer.music.play()
        GPIO.output(self.gpio_pin, True)
        while pygame.mixer.music.get_busy() == True:
            continue

        GPIO.output(self.gpio_pin, False)
        return

    def pinak(self):
        # panpin guztien pinak itzultzen ditu
        return Panpin.gpio_pinak

    def esaldi_berriak(self):
        # panaren esaldiak eguneratzen ditu
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        params = urllib.urlencode({"where":json.dumps({"noizarte": {"$gt": {"__type": "Date", "iso": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ') }}},{"noiztik": {"$lt": {"__type": "Date", "iso": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ') }}})})
        connection.connect()
        connection.request('GET', self.parse_api_class+'?%s' % params, '', {
               "X-Parse-Application-Id": PARSE_APP_ID,
               "X-Parse-REST-API-Key": PARSE_API_KEY
             })
        emaitza = connection.getresponse()
        print emaitza.status # 200 ondo bestela ez
        result = json.loads(emaitza.read())

        data = result["results"]
        # data = random.shuffle(data)
        self.esaldiak = data
	print data
        self.esaldien_luzeera = len(data)
        self.ind = 0
        return data

    def get_esaldia(self):
        # esaldi bat jasotzen du esaldien zerrendatik
        nire_esaldia = self.esaldiak[self.ind]
        if self.ind < self.esaldien_luzeera-1:
            self.ind = self.ind+1
        else:
            self.esaldi_berriak()

        return nire_esaldia

    def moztuEsaldia(self):
        fitx = AudioSegment.from_wav(self.audio_fitxategia)
        denbora = len(fitx) - TXAPAREN_IRAUPENA
        azken_esaldia = fitx[-denbora:]
        azken_esaldia.export(self.audio_fitxategia,format="wav")
        return

    def idatzi(self,esaldia):
        # textu fitxategian esaldi bat idazten du
        text_file = open(self.textu_fitxategia, "w")
        text_file.write(TXAPA + esaldia)
        text_file.close()
        return
