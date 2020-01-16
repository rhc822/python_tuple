# 2 Makin' a tuple...and seeing it
zoo = ("snake", "bug", "tiger", "lion", "cheetah", "rhinoceros", "pig", "monkey", "gibbon", "meerkat")
print(zoo.index("pig"))

# 3 Locatin' an item in a tuple
animal_to_find = "pig"
if animal_to_find in zoo:
    print("It's there!!")
else:
    print ("It's like not there dude!")


# 4 Assignin' variables to items in tuple
(a, b, c, d, e, f, g, h, i, j) = zoo
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j, "\n")

# 5 Changin' a tuple to a list
zooList = list(zoo)
print("Tuple to List: ", zooList, "\n")

#6 Use extend() to add three more animals to your zoo.
moreAnimals = ["bee", "wasp", "hornet"]
zooList.extend(moreAnimals)
print("Added stuff to List: ", zooList, "\n")

# Convert the list back into a tuple.
zoo = tuple(zooList)
print("List to Tuple: ", zoo, "\n")