# Program to find reverse of a string

def rev(str):
	return str[::-1] # function to reverse the string

def isPallindrome(str):
	revStr = rev(str) # reversing the string
	if(str == revStr): # if string == reversed string then its pallindrome
		return True
	return False


# Driver code
testString = "racecar"

print(isPallindrome(testString))
