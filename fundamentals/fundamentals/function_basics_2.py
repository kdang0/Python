def countdown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list

print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))


def values_greater_than_second(list):
    array = []
    if(len(list) < 2):
        return False
    for x in list:
        if(x > list[1]):
            array.append(x)
    return array
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


def length_and_value(numOne, numTwo):
    array = []
    x=0
    while(x < numOne):
        array.append(numTwo)
        x+=1
    return array

print(length_and_value(4,7))
print(length_and_value(6,2))


