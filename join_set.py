fruitSet = {"Banana", "Apple", "Cherry", "Orange"}
breakfastSet = {"Bread", "Egg", "Water", "Apple"}

# Using union function
unionSet = fruitSet.union(breakfastSet)
print(unionSet)

# Using update function
numberSet1 = {1, 2, 3, 4}
numberSet2 = {1, 5, 4, 10}
numberSet1.update(numberSet2)
print(numberSet1)
