


# Question 1
def getOnlyEvents(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            result.append(arr[i])

    
    print(result)


# Test 1
getOnlyEvents([1, 2, 3, 6, 4, 8])  

# Test 2
getOnlyEvents([0, 1, 2, 3, 4])  



# questoion 2

def reverseCompare(num):
    reverse = int(str(num)[::-1])
    if num > reverse:
        print("ok")

    else:
        print("not ok")
reverseCompare(72) 
reverseCompare(23)

# Question 3
def returnFactorial(num):
    fact = 1 # initialize factorial 
    for i in range(1, num + 1):
        fact = fact * i
    return fact  

print(returnFactorial(5))  
print(returnFactorial(6))  
print(returnFactorial(0))  

# Question 4
def checkMeera(arr):
    for n in arr:
        if n * 2 in arr:
            print("I am not meera array")
            return  
    print("I am a meera array")

checkMeera([10, 4, 0, 5])       
checkMeera([7, 4, 9])          
checkMeera([1, -6, 4, -3])    

#Question 5 dual array
def isDual(arr):
    for n in arr:
        if arr.count(n) != 2:
            return 0  

    return 1
print(isDual([1, 2, 1, 3, 3, 2]))  
print(isDual([2, 5, 2, 5, 5]))     
print(isDual([3, 1, 1, 2, 2]))    

#Question 6
def digitalClock(seconds):
    hours = (seconds // 3600) % 24
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"

print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))