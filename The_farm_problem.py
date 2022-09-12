chickens = int(input("How many chickens?: "))
cows = int(input("How many cows?: "))
pigs = int(input("How many pigs?: "))

animals = (2*chickens,4*cows,4*pigs)
sum_animals = sum(animals)
print("animals%s = %.0f" % (animals, sum_animals))