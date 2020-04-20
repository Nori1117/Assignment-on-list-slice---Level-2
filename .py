#Write a python program to find and display the number of circular primes less than the given limit.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.



def check_prime(number):
    #remove pass and write your logic here. if the number is prime return true, else return false
    return all(number% i for i in range(2, number))

def rotations(num):
     #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
	list = []
	m = str(num)
	conter = 0
	while conter < len(str(num)):
	    m=m[1:] + m[0]
	    list.append(int(m))
	    conter+=1
    list1=sorted(list, key=int)
    return list1
    

def get_circular_prime_count(limit):
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    conter = 0 
    
    for i in range(2, limit+1):
        a=rotation(i)
        for j in a:
            if j == prime(j):
                conter+=1
    
    return conter

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
