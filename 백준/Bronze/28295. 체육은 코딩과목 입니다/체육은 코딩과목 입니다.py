import sys
nesw = ["N", "E", "S", "W"]
result = 0
for i in range(10):    
    i = int(sys.stdin.readline())
    if(i == 1):
        result += 90
    elif(i == 2):
        result -= 180
    elif(i == 3):
        result -= 90
        
result %= 360
if(result < 0):
    result += 360
print(nesw[result//90])
