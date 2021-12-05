def main():
    with open('AOCDay2Inputs.txt', 'r') as f:
        movement = [line.strip() for line in f]
    testMovement = ["forward 5", "down 5",
                    "forward 8", "up 3", "down 8", "forward 2"]
    h, d = calcMove(movement)
    print(h * d)
    #testH, testD = calcMove(testMovement)
    #print(testH * testD)


def calcMove(m):
    hPos = 0
    dPos = 0
    aim = 0
    for i in range(0, len(m)):
        move, distance = getMovement(m[i])
        if(move == 'f'):
            hPos += int(distance)
            dPos += int(distance) * aim
        if(move == 'd'):
            #dPos += int(distance)
            aim += int(distance)
        if(move == 'u'):
            #dPos -= int(distance)
            aim -= int(distance)
    return hPos, dPos


def getMovement(moves):
    m = moves[0]
    space = moves.find(" ")
    dist = moves[space:]
    distInt = int(dist)
    return m, dist


main()
