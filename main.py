from student import Student, ItaPair

itas = []
pairs = []

def pair_itas():
    for i in range(len(itas)):
        for j in range(i + 1, len(itas)):
            ita1 = itas[i]
            ita2 = itas[j]

            has_overlap, times = ita1.attempt_pairing(ita2)

            if has_overlap:
                pairs.append(ItaPair(ita1, ita2, times))

if __name__ == '__main__':
    while True:
        inp = raw_input('Would you like to enter an ita? y/n  ')

        if inp == 'y':
            itas.append(Student(False))

        else:
            break

    print
    pair_itas()
    for pair in pairs:
        print pair