from Adafruit_PWM_Servo_Driver import PWM

class Begiak:
    __pwm = PWM(0x40)
    __servoMin = 150
    __servoMax = 600
    def __init__(self,begien_posizioa):
        self.ezkerreko_begia = begien_posizioa[0]
        self.eskuineko_begia = begien_posizioa[1]
        __pwm.setPWM(self.ezkerreko_begia,0,__servoMin)
        __pwm.setPWM(self.eskuineko_begia,0,__servoMax)

    def mugitu_begiak_hasieran(self):
        __pwm.setPWM(self.ezkerreko_begia, 0, __servoMax)
        __pwm.setPWM(self.eskuineko_begia, 0, __servoMax)


    def mugitu_begiak_bukaeran(self):
        __pwm.setPWM(self.ezkerreko_begia, 0, __servoMin)
        __pwm.setPWM(self.eskuineko_begia, 0, __servoMin)