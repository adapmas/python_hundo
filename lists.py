fruits= ["apple", "banana", "cherry"]
print(fruits[0]) #apple
fruits[0]="pear"
print(fruits[0]) #pear
print(fruits) #['pear', 'banana', 'cherry']
fruits.append("mango")
print(fruits) #['pear', 'banana', 'cherry', 'mango']
fruits.extend(["melon", "berries"])
print(fruits) #['pear', 'banana', 'cherry', 'mango', 'melon', 'berries']
