import time
import os

class Timer():

    def __init__(self):
        self.hours = 0
        self.mins = 1
        self.secs = 5

    def time(self):
        if self.hours >= 0:
            while True:
                print(f"{self.hours} : {self.mins} : {self.secs}")
                time.sleep(1)
                os.system("cls")
                self.secs -= 1
                if self.secs == 0:
                    self. secs = 59
                    self.mins -= 1

                if self.mins < 0:
                    self.mins = 59
                    self.hours -= 1

                if self.hours < 0:
                    print("""0 : 0 : 0
                    Time is Up !!""")
                    break
        else:
            print("Error")

    def choose(self):
        self.hours = int(input("Hours > "))
        self.mins = int(input("Minutes > "))
        self.secs = int(input("Secs > "))

        if self.hours < 0:
            print("Hour Error")
            os.system('cls')
            Timer.choose(self)

        if self.mins < 0:
            print("Min Error")
            os.system('cls')
            Timer.choose(self)

        if self.secs < 0:
            print("Secs Error")
            os.system('cls')
            Timer.choose(self)

        Timer.time(self)

timer = Timer()

timer.choose()
