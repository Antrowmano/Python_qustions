#Write a program to generate numbers between 1 to 100 with below functions
#a. From 1 to 100, print “Fizz” if the number is divisible by 3 and 
#“Buzz” if the number is divisible by 5  and “Fizzbuzz” if both
#c.Print fibonacci series starting from the given number till 100
#d.Print prime numbers between 1 to 100


def num():
    for i in range(1,100+1):
        if (i % 3 == 0) and (i % 5 ==0):
            print(f"{i}fizzBuzz")
        elif (i % 3 == 0):
            print(f"{i}FIZZ")
        elif(i % 5 ==0):
            print(f"{i}BUZZ")
#num()

#Write a function to remove duplicate items from a given list 
#Input : [1,1,2,5,5,5,6,7,7]
#Output : [1,2,5,6,7]

def dub(data):
    data2=[]
    for i in data:
        if i not in data2:
            data2.append(i)
    print(data2)
        

dub([1,1,2,5,5,5,6,7,7])