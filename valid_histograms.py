
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

completed = 0

def tree_search(rem: int, lineup: list[int]) -> None:
    global completed
    if rem == 0: # found a valid selection
        if completed % 100000 == 0:
            print(completed)
        completed += 1
        return
    
    for piece in pieces:
        piece_type, a, b = piece
        # straights
        if piece_type == 0:
            for i in range(a, a+5):
                lineup[i] += 1
            flag = True
            for i in range(a, a+5):
                if lineup[i] > 4:
                    flag = False
            if flag:
                tree_search(rem-1, lineup)
            for i in range(a, a+5):
                lineup[i] -= 1
        # full houses
        if piece_type == 1:
            lineup[a] += 3
            lineup[b] += 2
            flag = (lineup[a] <= 4 and lineup[b] <= 4)
            if flag:
                tree_search(rem-1, lineup)
            lineup[a] -= 3
            lineup[b] -= 2
        # 4oak
        if piece_type == 2:
            lineup[a] += 4
            lineup[b] += 1
            flag = (lineup[a] <= 4 and lineup[b] <= 4)
            if flag:
                tree_search(rem-1, lineup)
            lineup[a] -= 4
            lineup[b] -= 1

blank_lineup = [0 for i in range(13)]
tree_search(5, blank_lineup)