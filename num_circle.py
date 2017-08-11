import random

def numcircle(numlist, num):
    numlist = listconvert(numlist, num)
    flag = True
    while flag == True:
        flag = False
        count = 0
        while count < num:
            if numlist[count] != 0:
                new_count = numlist[count][-1][1]
                if new_count != count:
                    numlist[count].extend(numlist[new_count])
                    numlist[new_count] = 0
                    flag = True
            count += 1
    result = []
    for item in numlist:
        if item != 0:
            result.append(item)
    return result, len(result)


def listconvert(numlist, num):
    count = 0
    result = []
    while count < num:
        result.append([[count, numlist[count]]])
        count += 1
    return result


def main():
    num = 10000
    list = range(num)
    slice = random.sample(list, num)
    result, len = numcircle(slice, num)
    print(result)
    print(len)

if __name__ == '__main__':
    main()