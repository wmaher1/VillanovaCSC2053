alist = [10, 20, 30, 40, 50]
alist.append(5)
alist.append(6)
alist.append(7)
print(alist)

# remove function works with a value
# pop function works with index

alist.remove(50)
print(alist)
alist.pop(1)
print(alist)
alist.pop()
print(alist)

empty = []
for value in alist:
    if value >= 6 and value <=30:
        empty.append(value)
print(empty)
empty.sort()
print(empty)

# create empty array with 10 zeroes
empty = [0] * 10
#empty[8] = 10

dog = "dog"
dogs = dog * 3
print(dogs)

squares = []
for i in range(1000):
    squares.append(i*i)
print(squares) 

squares_copy = [value for value in squares]
print(squares_copy)

large_squares = [val for val in squares if val >= 10000]
print(large_squares)

squares = [i*i for i in range(1000)]
print(squares)

# Set
aset = {1,2,3}
print(aset)

# refer to this for hw 2
dups = [1,2,2,3,3,4,4,700,700,1,5,5]
no_dups = set(dups) # changing list to a set
print(no_dups)
do_dups = list(dups)
print(do_dups)

# Dictionaries
    # empty dictionaries use {} like a set
fav_foods = {"kathleen" : "pizza", "abby" : "hamburger", 
             "caroline" : "chicken tenders", "dominic" : "sushi"}
caroline_ff = fav_foods["caroline"]
print(caroline_ff)

for key in fav_foods:
    print(key, "favorite food is", fav_foods[key])
for key, value in fav_foods.items():
    print(key, "fav food is", value)

if "kim" in fav_foods:
    kim = fav_foods["kim"]
else: 
    fav_foods["kim"] = "cereal"













