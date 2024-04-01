#Heterogeneous or Homogeneous

list = ["John", "Paul", 43, "Beatles", 1984, "Liverpool", "London"]

print(type(list))   # --> <class 'list'>

print(list[2])      # --> 43

print(len(list))    # --> 3

list[2] = 567       # overwrite

print(list[0:3])    # --> ['John', 'Paul', 567]
print(list[ :3])    # --> ['John', 'Paul', 567]
print(list[3: ])    # --> ['Beatles', 1984, 'Liverpool', 'London']
print(list[-1])    # --> London
print(list[-3: -1])    # --> [1984, 'Liverpool']
print(list[-3: ])    # --> [1984, 'Liverpool', 'London']

list.append("Ringo") # --> ['John', 'Paul', 567, 'Beatles', 1984, 'Liverpool', 'London', 'Ringo']
list.insert(1, "George")    # --> ['John', 'George', 'Paul', 567, 'Beatles', 1984, 'Liverpool', 'London', 'Ringo']

# Methods
list.count("Ringo")  #--> 1   case sensitive
list.index("Ringo")  #--> 8   if repeated, returns the first one index

list2 = [3, 2, 5, 8, 1]
list2.sort()  #--> [1, 2, 3, 5, 8]

list2.reverse()     #--> [8, 5, 3, 2, 1]
list[0].lower()     #--> john
list.pop()          #--> Ringo
list.remove("Paul") #-->['John', 'George', 567, 'Beatles', 1984, 'Liverpool', 'London']

# Arithmetic Operators
print(list + list2)  #--> ['John', 'George', 567, 'Beatles', 1984, 'Liverpool', 'London', 8, 5, 3, 2, 1]