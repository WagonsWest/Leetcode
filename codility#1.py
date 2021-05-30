# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    str_N = str(N)
    list1=[]
    list1=list(str_N)
    if list1[0] != '-':
        for i in range(len(list1)):
            if 5 >= int(list1[i]):
                list1.insert(i, '5')
                new_N = int(''.join(list1))
                return new_N
            list1.append('5')
            new_N = int(''.join(list1))
            return new_N
    else:
        for i in range(len(list1)):
            if 5 <= int(list1[i+1]):
                list1.insert(i+1, '5')
                new_N = int(''.join(list1))
                return new_N
            list1.append('5')
            new_N = int(''.join(list1))
            return new_N
