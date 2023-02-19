#5-6 stages of life 
#python crash course
#day 2 of 100 day challenge. 

age = 4

if age < 2:
    message = 'your but a wee baby'
elif age >= 2 and age < 4:
    message = 'you a toddler'
elif age >= 4 and age <13:
    message = 'you a lil kid'
elif age >= 13 and age < 20:
    message = 'you are a teenager'
elif age >= 20 and age < 65:
    message = 'you are an adult'
else:
    message = 'you are an elder'

print(message)
