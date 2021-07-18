#Define a variable of type bool
b = True


#create a function to sum 2 value ,
#return the result
def add(num1,num2):
    return num1 + num2

''''
write a simple example to show the differences
between print & return
'''
def concatWord(word, letter):
    return word + letter

def concatWordAndPrint(word, letter):
    print(word + letter)


name = concatWord("Ahme", "d")
print(name)
concatWordAndPrint("ahme","d")


'''
write a function that multiplies any count
of numbers
'''
def multiply(num,*args):
    result = num
    for item in args:
        result *= item

    return result

print(multiply(1,2,3,4))

#range example
def printRange():
    start = int(input("please enter start: "))
    end = int(input("pleas enter end: "))
    for number in list(range(start,end)):
        print(number)

printRange()

#zip exmaple
a = [1,2,3,4]
b = ["ahmed", "ali", "mohamed"]
print(list(zip(a,b)))

#filter exmaple
def getEvenNumbers(n):
    if n %2 == 0:
        return True
    else:
        return False

print(list(filter(getEvenNumbers, a)))

#map example
def add2(n):
    return 2 + n

print(list(map(add2, a)))
    
