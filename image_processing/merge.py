from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

f0 = open('data0.txt', 'r')
f1 = open('data.txt', 'r')
with open('result_data.txt', 'w') as f:
    lines0 = f0.readlines()
    lines1 = f1.readlines()
    i0, i1 = 0, 0
    while i0 < len(lines0) or i1 < len(lines1):
        if lines0[i0].isspace():
            i0 += 1
            continue
        if lines1[i1].isspace():
            i1 += 1
            continue
        if i0 >= len(lines0):
            f.write(lines1[i1])
            i1 += 1
            continue
        if i1 >= len(lines1):
            f.write(lines1[i0])
            i0 += 1
            continue
        if similar(lines0[i0], lines1[i1]) > 0.6:
            f.write(lines1[i1])
            i0 += 1
            i1 += 1
            continue
        print("line {} and {}, similarity: {}".format(i0, i1, similar(lines0[i0], lines1[i1])))
        print("1: ", lines0[i0], "2: ", lines1[i1], "3: any", sep='')
        symb = None
        while symb != '1' and symb != '2' and symb != '3':
            symb = str(input())
        if symb == '1':
            f.write(lines0[i0])
            i0 += 1
        elif symb == '2':
            f.write(lines1[i1])
            i1 += 1
        else:
            f.write(lines1[i1])
            i0 += 1
            i1 += 1

f0.close()
f1.close()
