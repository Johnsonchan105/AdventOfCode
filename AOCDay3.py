def main():
    with open("AOCDay3Inputs.txt", "r") as tf:
        error = [line.strip() for line in tf]
    tf.close()
    testError = ["00100", "11110", "10110", "10111", "10101",
                 "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    gamma, epsilon = getGE(error)
    O2Num, CO2Num = getOC(testError)
    print(gamma * epsilon)
    print(O2Num)
    print(CO2Num)


def delUncommon(arr, OneOrZero, loc, com):
    if(len(arr) == 1):
        return arr
    report = []
    for i in range(0, len(arr)):
        # if 1 > 0, true
        # if 1 < 0, false
        if(len(arr) == 2):
            # if true that means most common
            # if false means least common
            if(com):
                report.append(arr[i] if(arr[i][loc] == "1") else arr[i+1])
                break
            else:
                report.append(arr[i] if(arr[i][loc] == "0") else arr[i+1])
                break
        if(OneOrZero):
            if(arr[i][loc] == "1"):
                report.append(arr[i])
        else:
            if(arr[i][loc] == "0"):
                report.append(arr[i])
    return report


def getOC(err):
    O2 = err
    CO2 = err
    for i in range(0, len(err[0])):
        one = 0
        zero = 0

        tempO = []
        tempC = []
        for j in range(0, len(err)):
            if(err[j][i] == "1"):
                one += 1
            else:
                zero += 1
        OneOrZero = one > zero
        if(len(O2) != 1):
            tempO = delUncommon(O2, OneOrZero, i, True)
            O2 = tempO
        if(len(CO2) != 1):
            tempC = delUncommon(CO2, not OneOrZero, i, False)
            CO2 = tempC
    return O2, CO2


def getGE(err):
    ga = 0
    ep = 0

    counter = 1
    for i in reversed(range(0, len(err[0]))):
        one = 0
        zero = 0
        for j in range(0, len(err)):
            if(err[j][i] == "1"):
                one += 1
            else:
                zero += 1
        OneOrZero = one > zero
        if(OneOrZero):
            ga += counter
        else:
            ep += counter

        counter *= 2
    return ga, ep


main()
