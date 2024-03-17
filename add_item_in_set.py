"""
Two ways to add item in a set
1. using add function
2. using update function
also add any iterable item that means set accepted list, tuple, dictionary
"""
fruitSet = {"Banana", "Apple", "Cherry", "Orange"}
print("Before adding value: ", fruitSet)

# Using add function
fruitSet.add("Juice")
print("After adding value: ", fruitSet)

# Using update function
breakfastSet = {"Bread", "Egg", "Water"}
print("Before updating: ", breakfastSet)
breakfastSet.update(fruitSet)
print("After updating: ", breakfastSet)

# Example of iterable
numberSet = {1, 32, 3, 5}
tupleSet = ("Hamim", "Leon")
listSet = ["Orange", "Apple"]
numberSet.update(tupleSet)
print(numberSet)
numberSet.update(listSet)
print(numberSet)
