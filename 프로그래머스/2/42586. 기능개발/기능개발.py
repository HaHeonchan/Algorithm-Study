def solution(progresses, speeds):
    days = 0
    lastUpdate = 0
    answer = []
    while(len(progresses) > 0):
        days += 1
        if(len(progresses) > 0 and (progresses[0] + (speeds[0] * days) >= 100)):
            lastUpdate = 0
            while(len(progresses) > 0 and progresses[0] + speeds[0] * days >= 100):
                del progresses[0]
                del speeds[0]
                lastUpdate += 1
            answer.append(lastUpdate)

    return answer