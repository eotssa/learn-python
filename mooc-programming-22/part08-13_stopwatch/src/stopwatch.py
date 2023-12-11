


class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0            
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else: 
            self.seconds += 1

      
    def __str__(self): 
        return f"{self.minutes:02d}:{self.seconds:02d}"



if __name__ == "__main__":
    clock = Stopwatch()
    # advance hour minus one second
    for i in range(60*59+59):
        clock.tick()         
    clock.tick()

    print(clock)

