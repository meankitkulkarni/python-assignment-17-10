# Mutability
import numbers

numbers = [10, 20, 30]
numbers[0] =99
numbers.append(40)
print(numbers)

word = "python"
word ="p" + word[1:]
print(word)

point = (4,5)
print(point)