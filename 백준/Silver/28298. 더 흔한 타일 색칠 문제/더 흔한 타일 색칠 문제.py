import sys

N, M, K = map(int, sys.stdin.readline().split())
tile_colors = [sys.stdin.readline().strip() for _ in range(N)]
result_colors = [list(row) for row in tile_colors]

total_painting = 0

for x in range(0, K):
    for y in range(0, K):
        total_colors = {}
    
        for i in range(0, N, K):
            for j in range(0, M, K):
                current_color = tile_colors[x+i][y+j]
                if current_color in total_colors:
                    total_colors[current_color] += 1
                else:
                    total_colors[current_color] = 1
        
        
        max_color = max(total_colors,key=total_colors.get)
        for i in range(0, N, K):
            for j in range(0, M, K):
                result_colors[x+i][y+j] = max_color
                if tile_colors[x+i][y+j] != max_color:
                    total_painting += 1
                    
print(total_painting)
for i in range(0, N):
    for j in range(0, M):
        print(result_colors[i][j],end = '')
    print('')