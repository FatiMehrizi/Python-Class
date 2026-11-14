#print("Hello python")
#print("*********")
#print("a"*10)
#print("hi")
#x =  1 
#print(x)
#student_count = 30
#is_publish = True
#print(course_name)
##print(student_count)
#message = """hello fati
 #print(message)

#course = "python programming"
#len(course )
#print(len(course ))

#print(course[0])
#print(course[-1])
#print(course[0:3])
#print(course[0:-2])

#\"       \'       \\     \n    \t
#course = 'python \" programming'
#print(course)
#course = "python \" programming"
#print(course)
#course = 'python \' programming'
#print(course)
#course = "python \\ programming"
#print(course)
#course = "python \n programming"
#print(course)
#course = "python \t programming"
#print(course)

#first = "coding"
#seperator = " "
#last = 'is cool'
#full = first + last 
#print(full)
#full = first +" " +last 
#print(full)
#full = first +seperator + last 
#print(full)
#full = f"{first} {last} neon"
#print(full)

#course = "    pythoN programming  "

#print( course.upper())
#or
#course_capital = course.upper()
#print(course_capital)

#print( course.lower())

#print( course.title())

#print( course.strip())
#print( course.rstrip())
#print( course.lstrip())

#print( course.find("h"))
#print( course.find("pyt"))
#print( course.find("f"))

#print( course.replace("p","z"))
#print( course.replace("pyt","z"))

#upperator:
#print("pyt" in course)
#print("z" not in course)

#print(10 + 3)
#print(10 - 3)
#print(10 * 3)
#print(10 / 3)
#print(10 // 3)
#print(10 % 3)
#print(10 ** 3)
#  *=    +=  -=  
#x = 10
#x = x + 3
#or
#x +=3
#print(x)

#round(2.9)
#print(round(2.9))
#print(round(2.3))

#abs(-2)
#print(abs(-2))

#import math
#print(math.ceil(2.2))
#print(math.floor(2.2))

#x = input("x : ")
#print(type(x))
#x = int(x)
#print(type(x))

#x = input("x : ")
#x = int(x)
#y = x + 1
#or
#y = int(x) + 1
#print(y)

#x = input("x : ")
#y = int(x) + 1
#print(f"x : {x} , y = {y}")

#print(10 > 3) 
#print(10 < 3) 
#print(3 <= 3) 
#print(3 > 3) 
#print(3 == 3) 
#print(4 == 3) 
#print(3 != 3) 
#print(4 != 3) 
#print(3 == "3") 

#print("ali" > "mohammad") 
#print(ord("a"))
#print(ord("m"))

#print("ali" > "ALI") 
#print(ord("a"))
#print(ord("A"))

#-------------------------------------------------------------------------------------------
#temprature = 35
#if temprature > 30:
#    print("its warm")
#    print("drink water")
#print("test")

#temprature = 15
#if temprature > 30:
#    print("its warm")
#    print("drink water")
#print("test")

#temprature = 10
#if temprature > 30:
#    print("its warm")
#    print("drink water")
#elif temprature > 20:
#    print("its nice")
#else:
#    print("its cold")

#temprature = 22
#if temprature > 30:
#    print("its warm")
#    print("drink water")
#elif temprature > 20:
#    print("its nice")

#age = 22
#f age >= 18:
#    print("Eligible")
#else: 
#    print("not Eligible ")

#age = 19
#if age >= 18:
#    message = "Eligible"
#else: 
#    message = "not Eligible "
#print(message)
#or
#age = 15
#message  =  "Eligible" if age >= 18 else "not Eligible "
#print(message)

#--------------------------------------------------------------------------------------
#high_income = True
#good_credit = True

#if high_income == True:
#    print('Eligible')
#else:
#    print('not Eligible')

#or

#if high_income :
#    print('Eligible')
#else:
#    print('not Eligible')

#or

#if high_income and good_credit:
#    print('Eligible')
##    print('not Eligible')


#high_income = True
#good_credit = True
#student = True

#if not student and ( high_income or good_credit):
#    print('Eligible')
#else:
#    print('not Eligible')


#if  student and high_income and good_credit:
#    print('Eligible')
#else:
#    print('not Eligible')

#if  student or high_income or good_credit:
#    print('Eligible')
#else:
#    print('not Eligible')

#------------------------------------------------------------------------
#age should be between 18 and 65 

#age = 22
#if age >=18 and age < 65:
#    print('Eligible')
#or
#if 18 <= age < 65:
#    print('Eligible')

#-----------------------------------------------------------------------
#for
#for number in range(4):
#    print('message')
#    print(number)

#for number in range(4):
#    print(number+1)

#for number in range(4):
#    print((number+1) * ".")

#for number in range(1 , 4):
#    print(number)

#for number in range(1 ,10 , 2):
#    print(number)
#----------------------------------------------------------------------
#for_else

#successful = True
#for number in range(3):
#    print("attempt")
#    if successful:
#        print("successful")
#        break


#successful = False
#for number in range(3):
#    print("attempt")
#    if successful:
#        print("successful")
#        break
#else:
#    print("attempted 3 times and failed")
#---------------------------------------------------------------------
#for x in range(4):
#    for y in range(2):
#        print(f"({x},{y})")
#--------------------------------------------------------------------

#print(type(5))
#print(type('jjjjjjj'))
#print(type(range(5)))

#for x in "python":
#    print(x)

#----------------------------------------------------------------------
#lists
#numbers = [1,2,3,4]
#print(numbers)
      
#for x in [1,2,3,4]:
#    print(x)

#------------------------------------------------------------------
#while
#number = 100
#while number > 0:
#    print(number)
#    number = number // 2 # => or (number //= 2)
#print('Done')

#command = ""
#while command != "exit":
#    command = input(">>>")
#    print(command)

#command = ""
#while command.lower() != "exit":
#    command = input(">>>")
#    print(command)


#command = ""
#while True:
#    command = input(">>>")
#    print(command)
#    if command.lower() == "exit":
#        break
#print('Done')

#-----------------------------------------------------------------------------
#def greet():
#    print("hi everyone")


#greet()


#def greet(first_name):
#    print(f"hi {first_name}")


#greet("fati")

#def greet(first_name , last_name):
#    print(f"hi {first_name} {last_name}")


#greet("fati","mehrizi")

#---------------------------------------------------------------------------------
#def greet(first_name):
#    print(f"hi {first_name}")

#def get_greeting(first_name):
#    return (f"hi {first_name}")

#message = get_greeting("neon")
#print(message)


#def get_greeting(first_name):
#    return (f"hi {first_name}")

#message = get_greeting("neon")

#file = open("content.txt", "w")
#file.write(message)

#def greet(first_name):
#    print(f"hi {first_name}")

#print(greet("neon"))
#---------------------------------------------------------------------------
#def increment(number , by):
#    return number + by

#print(increment(2,1))

#def increment(number , by):
#    return number + by

#print(increment(number=2,by=1))

#def increment(number , by=2):
#    return number + by

#print(increment(1))

#def increment(number , by=2 , another):
#    return number + by

#print(increment(1))

#-----------------------------------------------------------------------
#def multiply(x , y):
#    return x* y

#print(multiply(2,4))

#def multiply(* numbers):
#    return (numbers)

#print(multiply(2,4))


#def multiply(* numbers):
#    for number in numbers:
#        print(number)

#multiply(2,4,5)

#def multiply(* numbers):
#    total = 1
#    for number in numbers:
#        total *= number
#    return total
    
#print(multiply( 2, 4, 5 , 6 , 9))

#---------------------------------------------------------------------
#def save_user(**user):
#    print(user)

#save_user(id=1 , name="fati" , age = 32)

#def save_user(**user):
#    print(user["id"])

#save_user(id=1 , name="fati" , age = 32)
#---------------------------------------------------------------------
#message = "z"

#def greet(name):

#    message = "a"

#def send_email(name):
#    message = "b"

##greet("neon")
#print(message)

#message = "a"
#def greet(name):
#    message = "b"

#greet("neon")
#print(message)

#message = "a"
#def greet(name):
#   global message            #مناسب نیست انجام بدیم
#    message = "b"

#greet("neon")
#print(message)

#---------------------------------------------------------------------------
#def multiply(* numbers):
#    total = 1
#    for number in numbers:
#        total *= number
#       return total     #=>باید جزو بلاک فور باشه ینی بره عقب تر
    
#print("start")
#print(multiply(2,3,4))

#---------------------------------------------------------------------------
#list
#letters = ["a" , "b" , "c"]
#matrix = [[0,1],[2,3]]

#print(letters[0])

##یک لیست با صد صفر
#zeros = [0] * 100
#print(zeros)

##ترکیب دو لیست
#letters = ["a" , "b" , "c"]
#zeros = [0] * 100
#combined = letters + zeros
#print(combined)

##یک لیست که اعدا یک تا بیست هست
#numbers = list(range(21))
#print(numbers)

#chars = list("hello world")
#print(chars)
#chars = list("hello world")
#print(len(chars))

#letters = ["a" , "b" , "c"]
#print(letters[0])
#print(letters[-2])

#letters[0] = 2
#print(letters)

#print(letters[0:2])
#print(letters[::2])

#numbers = list(range(20))
#print(numbers[::2])
#print(numbers[::-1])
#print(numbers[::-2])
#----------------------------------------------------------------------------------
#numbers = [1,2,3]
#first = numbers[0]
#second = numbers[1]
#third = numbers[2]
#print(first , second , third)

#numbers = [1,2,3]
#first , second , third = numbers
#print(first , second , third)

#numbers = [1,2,3,4,5,6]

#first , second ,*other = numbers
#print(first , second , other)

#numbers = [1,2,3,4,5,6]

#first , *other , last = numbers
#print(first ,other , last)
#---------------------------------------------------------------------------------
#letters = ["a" , "b" , "c"]

#for letter in letters:
#    print(letter)

#for letter in enumerate(letters):
#    print(letter)

#for letter in enumerate(letters):
#    print(letter[0], letter[1])

#for index ,letter in enumerate(letters):
#    print(letter)
#    print(index)
#---------------------------------------------------------------------------------
#letters = ["a" , "b" , "c"]

#letters.append("d")
#print(letters)

#letters.insert(1,"d")
#print(letters)

#letters.pop()
#print(letters)

#result = letters.pop()
#print(result)

#letters.pop(1)
#print(letters)

#letters.remove("a")
#print(letters)

#if "z" in letters:
#    letters.remove("a")
#print(letters)

#letters = ["a" , "b" , "c" ,"b"]

#letters.remove("b")
#print(letters)

#del letters[0:3]
#print(letters)

#letters.clear()
#print(letters)
#---------------------------------------------------------------------------------------

#letters = ["a" , "b" , "c" , ]

#print(letters.index("b"))

#if "z" in letters:
#    print(letters.index("z"))

#if "c" in letters:
#    print(letters.index("c"))

#print(letters.count("b"))
#print(letters.count("x"))
#--------------------------------------------------------------------------------
#numbers = [3,20,1,7,4]

#numbers.sort()
#print(numbers)

#numbers.sort(reverse=True)
#print(numbers)

#print(sorted(numbers))
#print(numbers)
#------------------------------------------------------
#items = [
#    ("product1",10),
#    ("product2",9),
#   ("product3",12)
#]

##items.sort()
##print(items)

#def sort_item(item):
#    return item[1]
#items.sort(key = sort_item)
#print(items)


#def sort_item(item):
#    return item[1]
#items.sort(key = lambda item: item[1])
#print(items)
#-------------------------------------------------------------------

#تبدیل لیست تاپل به لیست نامبر
#items = [
#    ("product1",10),
#    ("product2",9),
#   ("product3",12)
#]

#prices = []

#for item in items :
#    prices.append(item[1])

#print(prices)


#or

#x = map(lambda item: item[1] , items)

#for item in x :
#    print(item)

#or

#prices = list(map(lambda item: item[1] , items))
#print(prices)

#prices = list(map(lambda item: item[1]*2, items))
#print(prices)
#----------------------------------------------------------------------------------
#فیلتر کردن لیست

#items = [
#    ("product1",10),
#    ("product2",9),
#   ("product3",12)
#]

#x = filter(lambda item: item[1] >= 10 , items)
#for item in x :
 #   print(item)

#x = list(filter(lambda item: item[1] >= 10 , items))
#print(x)
#----------------------------------------------------------------------------
#list comperhenssion

#items = [
#    ("product1",10),
#    ("product2",9),
#    ("product3",12)
#]

#prices = list(map(lambda item: item[1] , items))

#prices = [item[1] for item in items]
#print(prices)

#x = list(filter(lambda item: item[1] >= 10 , items))
#x = [item for item in items if item[1]>= 10]
#print(x)
#------------------------------------------------------------------------
#zip
#list1 = [1,2,3]
#list2 = [10,20,30]

#print(list(zip( list1, list2 , "abc")))

#-------------------------------------------------------------------------
#stack
#browsing = []
#browsing.append(1)
#browsing.append(2)
#browsing.append(3)

#browsing.pop()
#print("redirect",browsing[-1])

#if not []:
#    print("disable")

#if not browsing:
#    print("disable")

#print(browsing)
#-------------------------------------------------------------------
#queue








