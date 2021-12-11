def main():
    with open('AOCDay3Inputs.txt', 'r') as f:
        error = [line.strip() for line in f]
    testError = ["00100", "11110", "10110", "10111", "10101",
                 "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    print(error)
    #gamma, epsilon = getGE(testError)
    #print(gamma * epsilon)


'''
def binToDec(ge):
    counter = 1
    sum = 0
    for i in reversed(range(0, len(ge))):
        sum += counter if(ge[i] == "1") else 0
        counter *= 2
    return sum
'''

'''
def getGE(err):
    ga = 0
    ep = 0

    one = 0
    zero = 0
    counter = 1
    for i in reversed(range(0, len(err[0]))):
        for j in range(0, len(err)):
            if(err[j][i] == "1"):
                one += 1
            else:
                zero += 1
        ga += counter if(one > zero) else 0
        ep += 0 if(one > zero) else counter
        one = 0
        zero = 0
        counter *= 2
    return ga, ep

'''
main()
