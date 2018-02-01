from student import Student, ItaPair, Pairing

itas = []
pairs = []
consultants = []

def pair_itas():
    for i in range(len(itas)):
        for j in range(i + 1, len(itas)):
            ita1 = itas[i]
            ita2 = itas[j]

            has_overlap, times = ita1.attempt_pairing(ita2)

            if has_overlap:
                pair = ItaPair(ita1, ita2, times)
                pairs.append(pair)
                ita1.pairings.append(pair)
                ita2.pairings.append(pair)

def pair_with_consultants():
    return pair_with_consultants_helper(consultants, pairs)

def pair_with_consultants_helper(consultants, pairs):
    pairings = []

    for pair in pairs:
        has_overlap, times = consultants[0].attempt_pairing(pair)

        if has_overlap:
            c_pairs = wipe_pairs(pair, pairs)

            if len(consultants) > 1:
                p = pair_with_consultants_helper(consultants[1:], c_pairs)
                for pairing in p:
                    pairing.append(Pairing(consultants[0], pair, times))
                    pairings.append(pairing)
            else:
                pairings.append([Pairing(consultants[0], pair, times)])

    return pairings

def wipe_pairs(pairing, pairs):
    c_pairs = pairs[:]
    for pair in pairs:
        if pair.contains_student(pairing.ita1) or pair.contains_student(pairing.ita2):
            c_pairs.remove(pair)

    return c_pairs

def display_pairings(pairings):
    i = 0
    for pairing in pairings:
        print 'Pairing %d:' % i
        for pair in pairing:
            print pair

        print
        i += 1

if __name__ == '__main__':
    while True:
        inp = raw_input('Would you like to enter an ita? y/n  ')

        if inp == 'y':
            itas.append(Student(False))

        else:
            break

    while True:
        inp = raw_input('Would you like to enter a consultant? y/n')

        if inp == 'y':
            consultants.append(Student(False))

        else:
            break

    print
    print
    pair_itas()
    pairings = pair_with_consultants()
    display_pairings(pairings)
