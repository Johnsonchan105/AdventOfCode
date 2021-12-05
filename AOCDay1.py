def main():
    f = open('AOCDay1Inputs.txt', 'r')
    contents = []
    with open("AOCDay1Inputs.txt") as f:
        depth = f.read()
        depth_ints = [int(x) for x in depth.split()]
        contents.append(depth_ints)
    f.close()
    newContent = []

    # print(newContent)
    countIncrease2(threeMeasure(contents, newContent))

    testContent = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    countIncrease2(testContent)


def threeMeasure(contents, newContents):
    newContents = []
    i = 0
    while(i < len(contents[0]) - 2):
        sum = contents[0][i] + contents[0][i+1] + contents[0][i+2]
        newContents.append(sum)
        i += 1
    return newContents


def countIncrease(depth):
    increase = 0
    i = 0
    while(i < len(depth[0]) - 1):
        if(depth[0][i + 1] > depth[0][i]):
            increase += 1
        i += 1
    return increase


def countIncrease2(depth):
    increase = 0
    i = 0
    while(i < len(depth) - 1):
        if(depth[i + 1] > depth[i]):
            increase += 1
        i += 1
    print(increase)


main()
