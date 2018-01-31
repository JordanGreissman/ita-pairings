class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.start) + ' - ' + str(self.end)

    def __repr__(self):
        return str(self.start) + ' - ' + str(self.end)

    def find_compatible_time(self, other):
        # self starts before other
        if self.start <= other.start:
            # self ends before other
            if self.end <= other.end:
                # check if there is an hour between other.start and self.end
                overlap = self.end - other.start
                end = self.end
                start = other.start
            # other ends before self
            else:
                # check if there is an hour between other.start and other.end
                overlap = other.end - other.start
                end = other.end
                start = other.start
        # other starts before self
        else:
            # self ends before other
            if self.end <= other.end:
                # check if there is an hour etween self.start and self.end
                overlap = self.end - self.start
                end = self.end
                start = self.start
            else:
                # check if there is an hour between self.start and other.end
                overlap = other.end - self.start
                end = other.end
                start = self.start

        if overlap >= 60:
            return Interval(start, end)

        return None

class Time(object):
    def __init__(self, hour, minute, period):
        self.hour = hour % 12 if period == 'AM' else (hour % 12) + 12
        self.minute = minute
        self.period = period

    def __str__(self):
        if self.hour > 12:
            hour = str(self.hour - 12)
        elif self.hour == 0:
            hour = '12'
        else:
            hour = str(self.hour)

        if self.minute < 10:
            minute = '0%d' % self.minute
        else:
            minute = str(self.minute)

        return '%s:%s %s' % (hour, minute, self.period)

    def __le__(self, other):
        return self.hour < other.hour or (self.hour == other.hour and self.minute <= other.minute)

    def __ge__(self, other):
        return self.hour > other.hour or (self.hour == other.hour and self.minute >= other.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __sub__(self, other):
        # returns the number of minutes between self and other
        return (self.hour - other.hour) * 60 + (self.minute - other.minute)
