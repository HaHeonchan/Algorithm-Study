def getNum(number_array):
    string_array = map(str, number_array)
    combined_string = "".join(string_array)
    result = int(combined_string)
    return result
 
def swap(x, y):
    number_array[x], number_array[y] = number_array[y], number_array[x]


def change(chance):
    if(chance <= 0):
        return getNum(number_array)
    number = getNum(number_array)
    if ((chance, number) in note):
        return 0
    else:
        note.add((chance, number))
    
    max_num = -1
    for i in range(len(number_array)):
        for j in range(len(number_array)):
            if(j != i):
                swap(i, j)
                result_num = change(chance-1)
                if(result_num > max_num):
                    max_num = result_num
                swap(i, j)
    return max_num

global note
global number_array

testCase = int(input())
for i in range(testCase):
    note = set()
    inputData = list(map(str, input().split()))

    number_array = list(map(int, inputData[0]))
    chance = int(inputData[1])
    result = change(chance)
    
    print("#", i+1, " ", result, sep="")