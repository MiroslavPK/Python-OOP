class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):

        self.seconds = (self.seconds + 1) % 60
        self.minutes = (self.minutes + (self.seconds == 0)) % 60
        self.hours = (self.hours + (self.minutes == 0 and self.seconds == 0)) % 24

        return self.get_time()


time = Time(00, 00, 00)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
