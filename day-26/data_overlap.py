with open("file1.txt") as file1:
    list1 = [int(num.strip()) for num in file1]
with open("file2.txt") as file2:
    list2 = [int(num.strip()) for num in file2]

result = [num for num in list1 if num in list2]

# Write your code above 👆

print(result)
