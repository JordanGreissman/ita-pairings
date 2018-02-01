from schedule import Interval, Time

class Student(object):
    def __init__(self, from_backup):
        self.name = raw_input('What is their name? ')
        self.net_id = raw_input('What is their net-id? ')
        self.schedule = {'monday': [],
                        'tuesday': [],
                        'wednesday': [],
                        'thursday': [],
                        'friday': []}

        self.pairings = []

        if from_backup:
            pass

        else:
            self.prompt_for_schedule()

    def prompt_for_schedule(self):
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for day in week:
            print(day + ' schedule:')
            print('\tEnter an interval (hh:mm AM/PM - hh:mm AM/PM) or done when done')

            while True:
                inp = raw_input('\t')

                if inp == 'done':
                    break

                l = inp.split(' ')
                h1, m1 = l[0].split(':')
                h2, m2 = l[3].split(':')

                start = Time(int(h1), int(m1), l[1])
                end = Time(int(h2), int(m2), l[4])

                self.schedule[day.lower()].append(Interval(start, end))

    def attempt_pairing(self, s2):
        times = {}
        has_overlap = False
        for day, intervals in self.schedule.iteritems():
            intervals2 = s2.schedule[day]
            overlaps = []
            for i1 in intervals:
                for i2 in intervals2:
                    overlap = i1.find_compatible_time(i2)

                    if overlap:
                        has_overlap = True
                        overlaps.append(overlap)

            times[day] = overlaps

        return has_overlap, times

    def __str__(self):
        return '%s (%s)' % (self.name, self.net_id)

    def __repr__(self):
        return '%s (%s)' % (self.name, self.net_id)

class ItaPair(object):
    def __init__(self, ita1, ita2, times):
        self.ita1 = ita1
        self.ita2 = ita2
        self.schedule = times

    def __str__(self):
        monday = '\tMonday\n\t\t%s\n' % self.schedule['monday'] \
                    if self.schedule['monday'] != [] else ''
        tuesday = '\tTuesday\n\t\t%s\n' % self.schedule['tuesday'] \
                    if self.schedule['tuesday'] != [] else ''
        wednesday = '\tWednesday\n\t\t%s\n' % self.schedule['wednesday'] \
                    if self.schedule['wednesday'] != [] else ''
        thursday = '\tThursday\n\t\t%s\n' % self.schedule['thursday'] \
                    if self.schedule['thursday'] != [] else ''
        friday = '\tFriday\n\t\t%s\n' % self.schedule['friday'] \
                    if self.schedule['friday'] != [] else ''

        return 'Pair: \n\t%s, %s\nTimes:\n%s%s%s%s%s' % \
            (str(self.ita1), str(self.ita2), monday, tuesday, wednesday, thursday, friday)

    def __repr__(self):
        return str(self)

    def contains_student(self, s):
        return self.ita1 == s or self.ita2 == s

class Pairing(object):
    def __init__(self, consultant, itas, times):
        self.consultant = consultant
        self.ita1 = itas.ita1
        self.ita2 = itas.ita2
        self.schedule = times

    def __str__(self):
        monday = '\tMonday\n\t\t%s\n' % self.schedule['monday'] \
                    if self.schedule['monday'] != [] else ''
        tuesday = '\tTuesday\n\t\t%s\n' % self.schedule['tuesday'] \
                    if self.schedule['tuesday'] != [] else ''
        wednesday = '\tWednesday\n\t\t%s\n' % self.schedule['wednesday'] \
                    if self.schedule['wednesday'] != [] else ''
        thursday = '\tThursday\n\t\t%s\n' % self.schedule['thursday'] \
                    if self.schedule['thursday'] != [] else ''
        friday = '\tFriday\n\t\t%s\n' % self.schedule['friday'] \
                    if self.schedule['friday'] != [] else ''

        return 'Consultant: \n\t%s\nItas: \n\t%s, %s\nTimes:\n%s%s%s%s%s' % \
            (str(self.consultant), str(self.ita1), str(self.ita2), monday, tuesday, wednesday, thursday, friday)

    def __repr__(self):
        return str(self)
