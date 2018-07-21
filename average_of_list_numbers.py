numbers = int(input("Enter the numbers of elements to be inserted: "))
arr = []

for i in range(0,numbers):
	el = int(input("Enter Element:"))
	arr.append(el)
	avg = sum(arr)/numbers

print("Average of elements in the list",round(avg,2))
