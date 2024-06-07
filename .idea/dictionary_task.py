# 1. car = { "brand": "Ford", "model": "Mustang", "year": 1964 } a. Add the key/value pair "color" : "red"
# to the car dictionary. b. Use the get method to print the value of the "model" key of the car dictionary.

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# car['color']="red"
# print(car)
#
# print(car.get('model'))
#
# # 2. Get the key of a minimum value from the following dictionary. mark = {'Physics': 82,'Math': 65,'history': 75
# mark = {'Physics': 82,'Math': 65,'history': 75}
# print(min(mark))

#3. Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample = {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},'emp3': {'name': 'Brad', 'salary': 500}}


sample['emp3']['salary']=8500
print(sample)