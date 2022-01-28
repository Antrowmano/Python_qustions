#Write a program to generate numbers between 1 to 100 with below functions
#a. From 1 to 100, print “Fizz” if the number is divisible by 3 and 
#“Buzz” if the number is divisible by 5  and “Fizzbuzz” if both
#c.Print fibonacci series starting from the given number till 100
#d.Print prime numbers between 1 to 100


#def number():
#    for i in range(1,100):
#        if (i % 3 ==0) and (i % 5 ==0):
#            print(f"{i} Fizzbuzz")
#        elif(i % 3 ==0):
#            print(f"{i} Fizz")
#        elif(i % 5 ==0):
#            print(f"{i} Buzz")
            
#number()

#Write a function to remove duplicate items from a given list 
#Input : [1,1,2,5,5,5,6,7,7]
#Output : [1,2,5,6,7]



def duplicate():
    list1 =[1,1,2,5,5,5,6,7,7]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
#duplicate()


#Write a function to print True when the given string is palindrome
#	i) “otto” -> True  ii) “ottoman” -> False
#
#palindrome():

#    var = input("my input:")
#    if(var == var[::-1]):
#        print(var[::-1])
#        print(var)
#        print("this is palindrome")
#    else:
#       print(var)
#        print("not a palindrome")

#palindrome()

def palindrome():
    a = 'otto'
    b = 'ottoman'
    if(a == a[::-1]):
#        print(var[::-1])
#        print(var)
        print(f"this is otto {True} ")
    elif(b == b[::-1]):
        print (f"this is ottoman {True}")
    else:
#       print(var)
        print(f"not a palindrome {False}")

#palindrome()


# 2.Write a function which will return set of given list
#	Input : [2,3,5] 
#	Output : [4,9,25]

def num():
    numbers = [2,3,5] 
    for number in numbers:
        print(number ** 2)
        
#num()

#d.Print prime numbers between 1 to 100
def prime(first,second):
    for i in range(first,second):
        #print(f"hey you   {i}")
        for a in range(2,i):
        #    print(f"hey  {a}")
            if (i % a == 0):
                break
        else:
           print(i)
prime(2,30)