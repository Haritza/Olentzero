from Adafruit_PWM_Servo_Driver import PWM

class Begiak:

    def __init__(self,begien_posizioa):
        self.ezkerreko_begia = begien_posizioa[0]
        self.eskuineko_begia = begien_posizioa[1]

        self.pwm = PWM(0x40)
        self.servoMin = 150
        self.servoMax = 600

        self.pwm.setPWM(self.ezkerreko_begia,0,self.servoMin)
        self.pwm.setPWM(self.eskuineko_begia,0,self.servoMax)

    def mugitu_begiak_hasieran(self):
        self.pwm.setPWM(self.ezkerreko_begia, 0, self.servoMax)
        self.pwm.setPWM(self.eskuineko_begia, 0, self.servoMax)


    def mugitu_begiak_bukaeran(self):
        self.pwm.setPWM(self.ezkerreko_begia, 0, self.servoMin)
        self.pwm.setPWM(self.eskuineko_begia, 0, self.servoMin)