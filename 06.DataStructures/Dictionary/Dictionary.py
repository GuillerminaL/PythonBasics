from datetime import datetime

data = {"User": "nvjsabvj", "Password": "jhe283hd"}

print(type(data))   #--> <class 'dict'>
print("Dictionary keys: {}".format(data.keys()))
print("Dictionary values: {}".format(data.values()))
print("User: {}".format(data["User"]))

''' Insert with prompt:
newField = input("Add a new key: ").capitalize()
newValue = input("Add a value for the new key ")
data[newField] = newValue
print(data)
'''

# Methods
data["Email"] = "jdsb@mail.com"          # Insert
print(data.get("Email"))                 # Get

data.setdefault("Date", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))     # Set Default
print("Data with default value in key 'Date': {}".format(data))
'''
The .setdefault() method will return the value of a dictionary entry for a specified key. 
If the specified key does not exist in the dictionary, it will create an entry for it with 
the specified value
'''

data2 = {"Name": "John", "Date": "today now"}
data.update(data2)
print("Data updated: {}".format(data) )  # Update - equivalent to join

data.pop("Email")       # Remove Key value
data.clear()            # Clear structure

data.copy()