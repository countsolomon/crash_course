#2nd day of 100 day
#crash course
#exercise 5-11 ordinal numbers. 
#page 89

# a program that takes the list 1-9 and prints them as ordinal numbers. 
# nested if statements within a for loop. 
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in list:
    if num == '1':
        print(num + 'st')
    elif num == '2':
        print(num + 'nd')
    elif num == '3':
        print(num + 'rd')
    else: 
        print(num + 'th')

