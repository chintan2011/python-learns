num = int(input("Enter Number:"))

reverse = 0

while(num > 0):
	d = num%10
	reverse = reverse*10+d
	num = num//10
print("Reversed Number:",reverse)
