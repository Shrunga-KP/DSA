import random

# 1.	Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

def exchange_values( val1, val2):
	val1, val2 = val2, val1
	return val1, val2


# 2.	Python Program to Check Whether a Number is Positive or Negative.
def isPositiveNumber(num):
	return num > -1

# 3.	Python Program to Print all Numbers in a Range Divisible by a Given Number.
def divisibleNumbers(limits, num):
	num_list = []
	for number in range(1, limits + 1):		
		if number % num == 0:
			num_list.append(number)
	return num_list

# 4.	Python Program to Read Two Numbers and Print Their Quotient and Remainder
def quotient_reminder (num1, num2):
	return (num1//num2, num1 % num2)

#Program to print odd numbers
def oddNumbers(n):
	a=[]
	for i in range(n+1):
		if(i%2!=0):
			a.append(i)
	
	return a

# 5.	Python Program to Print Odd Numbers Within a Given Range.
def oddNumbers(limits):
	odd_list = []
	for num in range(limits):
		if num % 2 != 0:
			odd_list.append(num)
	return odd_list

#6.Python Program to Find the Sum of Digits in a Number.
def sumOfDegits(n):
	sum=0
	while(int(n)>0):
		sum=sum+n%10
		n=int(n/10)
	return sum

#7. Program to find smallest divisor of a number
def findSmallestDivisor(n):
	for i in range(2,n):
		if(n%i==0):
			return i
			

#8. Program to read a number n and then find sum of n+nn+nnn+...
def sumOfSeries(n,k):
	sum=0
	digit=n
	while(k>0):
		sum=sum+n
		n=n*10+digit
		k=k-1
	return sum

#9. Program to Reverse a Given Number.
def reverse(n):
	reverse=0
	while(int(n)>0):
		reverse=reverse*10+n%10
		n=int(n/10)
	return reverse

#10. Program to Calculate the Average of Numbers in a Given List.
def average(a):
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]
		average=sum/len(a)
	return average

#11. Program to Count the Number of Digits in a Number.
def count(n):
	c=0
	while(int(n)>0):
		c=c+1
		#print(c)
		n=int(n/10)
	return c

#12. Program to Check if a Number is a Palindrome.
def palindrome(n):
	number=n
	reverse=0
	while(n>0):
		reverse=reverse*10+n%10
		n=int(n/10)
	return (reverse==number)

#13. Program to print the number of occurrence of a sub string in a given string.
def ifSubStringFound(a,b):
	c=0
	for i in range(len(a)):
		if(a[i:i+len(b)]==b):
			c=c+1
	return c

#14. program to print the lowest index in the string where substring sub is found within the string.
def indexSubStringFound(a,b):
	for i in range(len(a)-len(b)+1):
		if(a[i:i+len(b)]==b):
			break
	return i

#15. Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False
def checkForCharacters(a):
	for i in range(len(a)):
		f=0
		if(96<ord(a[i])<123 or 64<ord(a[i])<92):
			f=0
		else:
			f=1
			break
	if(f==1):
		return False
	else:
		return True
			
		
#16. Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replace(a):
	a_list=list(a)
	for i in range(len(a_list)):
		if(a_list[i]=='a'):
			a_list[i]='$'
	return ''.join(a_list)

#17. PPython Program to Count the Number of Vowels in a String.
def countVowels(n):
	c=0
	for i in range(len(n)):
		if(n[i] in ['a','e','i','o','u','A','E','I','O','U']):
			c+=1
	return c

#18. Program to Take in a String and Replace Every Blank Space with Hyphen.
def replaceBlankSpace(a):
	a_list=list(a)
	for i in range(len(a_list)):
		if(a_list[i]==' '):
			a_list[i]='-'
	return ''.join(a_list)

#19. Program to find the length of string without using any built-in functions.
def findLength(a):
	if(a==''):
		return 0
	else:
		return 1+findLength(a[1:])
	
#20. Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
def findLargerString(a,b):
	n=findLength(a)
	m=findLength(b)
	if(n>m):
		return a
	elif(m>n):
		return b
	else:
		return "Equal"

#21. Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
def countOfUpperLower(a):
	u=0
	l=0
	for i in range(len(a)):
		if(64<ord(a[i])<91):
			u+=1
		elif(96<ord(a[i])<123):
			l+=1
		else:
			"Nothing"
	return u,l

#22.  Program to Calculate the Number of Digits and Letters in a String.
def checkDigitORLetter(b):
	if(64<ord(b)<91 or 96<ord(b)<123):
		return True
	else:
		return False
def countCharsDigits(a):
	c=0
	d=0
	for i in range(len(a)):
		if(checkDigitORLetter(a[i])):
			c+=1
		else:
			d+=1
	return c,d


#23.  Program to check whether a full pattern (not sub string) is present in the given sentence.
def fullPattern(a,b):
	if(b in a):
		return True
	else:
		return False
	

#24.  Write a function cumulative_sum() to compute cumulative sum of a list
def cumulative_Sum(a):
	b=[]
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]
		b.append(sum)
	return b

#25. Program to generate 10 random integers
def tenRandomNumbers():
	a=[]
	for i in range(10):
		a.append(random.random())
	return a


#26. program to generate 10 random integers between 1 to 20 
def tenRandomNumbersRange():
	a=[]
	for i in range(10):
		a.append(random.randint(1,20))
	return a

#27. program to generate 5 random integers between 1 to 20 such that numbers should be unique.
def uniqueRandomNumbers():
	a=set()
	for i in range(6):
		a.add(random.randint(1,20))
	return a

#28.  program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc
a=[]
def randomNumbers():
	n=1
	while(n<101):
		a.append(random.randint(n,n+10))
		n=n+10
	return a

	
