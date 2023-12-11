
class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def tick(self):
        
        if self.hours == 23 and self.minutes == 59 and self.seconds == 59:
            self.hours = 0
            self.seconds = 0
            self.minutes = 0   
        elif self.minutes == 59 and self.seconds == 59:
            self.hours += 1
            self.seconds = 0
            self.minutes = 0            
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else: 
            self.seconds += 1

        
    def set(self, *my_args):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        try: 
            if my_args[0]:
                self.hours = my_args[0]
        except: 
            self.hours = 0

        try: 
            if my_args[1]:
                self.minutes = my_args[1]
        except: 
            self.minutes = 0
        
        try:
            if my_args[2]:
                self.seconds = my_args[2]
        except:
            self.seconds = 0

    def __str__(self): 
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"




if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(15, 15)
    print(clock)

