from Adafruit_PWM_Servo_Driver import PWM

class Begiak:

    def __init__(self,begien_posizioa):
        self.ezkerreko_begia = begien_posizioa[0]
        self.eskuineko_begia = begien_posizioa[1]

        pwm = PWM(0x40)
        servoMin = 150
        servoMax = 600

        pwm.setPWM(self.ezkerreko_begia,0,servoMin)
        pwm.setPWM(self.eskuineko_begia,0,servoMax)

    def mugitu_begiak_hasieran(self):
        pwm.setPWM(self.ezkerreko_begia, 0, servoMax)
        pwm.setPWM(self.eskuineko_begia, 0, servoMax)


    def mugitu_begiak_bukaeran(self):
        pwm.setPWM(self.ezkerreko_begia, 0, servoMin)
        pwm.setPWM(self.eskuineko_begia, 0, servoMin)