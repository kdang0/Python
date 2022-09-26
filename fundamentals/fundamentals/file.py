num1 = 42 #variable declaration, initialize numbers
num2 = 2.3 #variable declaration, initialize numbers
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #log statement, type check tuple
print(pizza_toppings[1]) #log statement, list access value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #log statement, dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #log statement, list access value



if num1 > 45:           #if statement is greater than    
    print("It's greater") #log statement
else:                   #else statement
    print("It's lower")     #log statement

if len(string) < 5:     #if statement length check
    print("It's a short word!") #log statement
elif len(string) > 15:  #else if statement length check
    print("It's a long word!")  #log statement
else:       #else statement
    print("Just right!")    #log statement

for x in range(5):  #for loop start
    print(x)        #log statement
for x in range(2,5):    #for loop start
    print(x)    #log statement
for x in range(2,10,3):     #for loop start
    print(x)    #log statement
x = 0
while(x < 5): #while loop
    print(x)    #log statement
    x += 1  #increment

pizza_toppings.pop()    #list, delete value
pizza_toppings.pop(1)   #list, delete second value

print(person)   #log statement
person.pop('eye_color') #dictionary, delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':  #if statement
        continue    #continue
    print('After 1st if statement') 
    if topping == 'Olives': #if statement
        break   #break

def print_hello_ten_times(): #function
    for num in range(10):   #for loop
        print('Hello')  #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function
    for num in range(x):    #for loop
        print('Hello')  #log statement

print_hello_x_times(4) #function call

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call 
print_hello_x_or_ten_times(4)   #function call


"""
Bonus section
"""

# print(num3) #NameError
# num3 = 72   #variable declaration, initialize numbers
# fruit[0] = 'cranberry' #TypeError
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError
# print(boolean)  #log statement
# fruit.append('raspberry')  #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'