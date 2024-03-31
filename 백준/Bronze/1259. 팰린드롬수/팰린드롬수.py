while True:
    num = input()
    if(num=="0"):
        break
    ans = "yes"
    for i in range(0, int(len(num) / 2)):
        if num[i] != num[len(num) - i - 1]:
            ans = "no"
            break
    print(ans)
