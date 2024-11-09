# Make and print a list called things with these three strings as elements: 
# "mozzarella, "cinderella ", "salmonella". 

things = ["mozzarella", "cinderella", "salmonella"] 
print(things) 
# Capitalize the element in thigs that refers to a person and then print the list. Did it change the element in the list 

#This is Capitalizes the word but doesen't change it in the list:
things[1].capitalize()
'Cinderella' 
print(things) 

#If you want to change it in the list, you need to assign it back: 
things[1] = things[1].capitalize()
print(things) 

# Make the cheesy element of things all uppercase and then print the list. 
things[0] = things[0].upper() 

# Delete the disease element, collect your Nobel Prize, and then print the list. 

# this remove it by value: 
things.remove("salmonella") 
print(things)

#Becasuse it was last in the list, the following would have worked also: 
del things[-1] 

#And you could have deleted by offset from the beginning: 
del things[2]