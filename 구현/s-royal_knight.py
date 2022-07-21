loc = input()

col = ['a','b','c','d','e','f','g','h']
row = ['1', '2', '3', '4', '5', '6', '7', '8']
x, y = -1, -1

for i in range(len(row)):
    if row[i] in loc:
        x = i
    if col[i] in loc:
        y = i
    if x != -1 and y != -1:
        break
# 현재 위치 찾기

double_moves = [-2, 2]
once_moves = [-1, 1]
dx, dy, count = 0, 0, 0

for double_move in double_moves:
    for once_move in once_moves:
        dx = x + once_move
        dy = y + double_move
        if dx < 0 or dy < 0 or dx > 7 or dy > 7:
            continue
        
        count += 1 

for double_move in double_moves:
    for once_move in once_moves:
        dy = y + once_move
        dx = x + double_move
        if dx < 0 or dy < 0 or dx > 7 or dy > 7:
            continue
        count += 1 
print(count)