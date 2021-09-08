import pandas as pd

print(pd.__version__)

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings':[3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print("")

a = [1,7,2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar1 = pd.Series(calories)
print(myvar1)

myvar2 = pd.Series(calories, index = ["day1", "day2"])
print(myvar2)

data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}
myvar3 = pd.DataFrame(data)
print(myvar3)

