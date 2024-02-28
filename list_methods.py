numbers = [1, 2, 3, 4, 5]
## to add value at the end
numbers.append(6)
print(numbers)

## to add value to a specific index
numbers.insert(0, "s")
print(numbers)

## to remove specified value
numbers.remove(3)
print(numbers)

## method to find a value in a list (true or false)
print(6 in numbers)

## to check the list length
print(len(numbers))

## to remove everything
numbers.clear()
print(numbers)