numbers = [1,2,3,4,5]
numbers.append(6)
numbers.insert(0, -1)
print(numbers)

# removes item at idx 3
numbers.remove(3)

# numbers.clear() clears the list

print(1 in numbers)
print(10 in numbers)

# size of list
print(len(numbers))