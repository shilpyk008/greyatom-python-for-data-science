# --------------
# Code starts here

# Create the lists 

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
print(class_1)
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
print(class_2)

# Concatenate both the strings

new_class = class_1 + class_2 
print(new_class)

# Append the list

new_class.append('Peter Warden')
print(new_class)

new_class.remove('Carla Gentry')
print(new_class)

# Print updated list


# Remove the element from the list

# Print the list



# Create the Dictionary
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
Math =  courses['Math']
English =  courses['English']
History =  courses['History']
French =  courses['French']
Science =  courses['Science'] 

Total = Math + English + History + French + Science
print(Total)

percentage = (Total *100/500) 
print(percentage)
# Store the all the subject in one variable `Total`
# Print the total
# Insert percentage formula
# Print the percentage
# Create the Dictionary
 
mathematics = {'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70}
print(mathematics)

topper = max(mathematics, key = mathematics.get)
print(topper)

first_name = topper.split()[0]
print(first_name) 

last_name = topper.split()[1]
print(last_name)  

full_name = last_name + ' ' + first_name
print(full_name) 

certificate_name = full_name.upper()
print(certificate_name)




# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


