def main():
    with open('AOCDay2Inputs.txt', 'r') as f:
        movement = [line.strip() for line in f]
    h, d = calcMove(movement)
    print(h * d)


def calcMove(m):
    hPos = 0
    dPos = 0
    for i in range(0, len(m) - 1):
        move, distance = getMovement(m[i])
        if(move == 'f'):
            hPos += int(distance)
        if(move == 'd'):
            dPos += int(distance)
        if(move == 'u'):
            dPos -= int(distance)
    return hPos, dPos


def getMovement(moves):
    m = moves[0]
    space = moves.find(" ")
    dist = moves[space:]
    distInt = int(dist)
    return m, dist


main()
