#Basic
for x in range(151):
    print(x)

#Multiples of Five
for x in range(5,10001,5):
    print(x)

#Counting, the Dojo Way
for x in range(1, 101):
    if(x%10 == 0):
        print("Coding Dojo")
    elif(x%5 == 0):
        print("Coding")

#Whoa. That Sucker's Huge
sum = 0
for x in range(500001):
    sum += x 

print(sum)

#Countdown by Fours
for x in range(2018,0,-4):
    if(x % 2 ==0):
        print(x)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if(x % mult == 0):
        print(x)