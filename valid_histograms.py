
# list of tuples that look like (type, a, b), 0 <= a, b <= 12
# if type = 0, it's a straight that starts on a
# if type = 1, it's a full house with 3 on a and 2 on b
# if type = 2, it's a 4oak with 4 on a and 1 on b
pieces = []

for i in range(0, 9):
    pieces.append((0, i, 0))

for a in range(0, 13):
    for b in range(0, 13):
        if a == b:
            continue
        pieces.append((1, a, b))
        pieces.append((2, a, b))

choose = [[0 for i in range(6)] for _ in range(322)]
for n in range(322):
    choose[n][0] = 1
    for k in range(1, 6):
        if k > n:
            continue
        choose[n][k] = choose[n-1][k-1] + choose[n-1][k]

def id_to_selection(num, id):
    