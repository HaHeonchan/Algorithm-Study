def __main__():
    for _ in range(10):
        result = 0
        chance = int(input())
        boxes_str = str(input()).strip()
        boxes = list(map(int, boxes_str.split(" ")))
        for i in range(chance):
            lmin, lmax = boxes[0], boxes[0]
            for j in range(len(boxes)):
                if(boxes[lmin] > boxes[j]):
                    lmin = j
                if(boxes[lmax] < boxes[j]):
                    lmax = j
            boxes[lmin] += 1
            boxes[lmax] -= 1

        print("#", _+1, " ", max(boxes)-min(boxes), sep="")

__main__()