'''
Created on May 26, 2013

@author: Kevin
'''

for i in range(0,5):
    if i == True:
        print "%d is True" % (i)
    else:
        print "%d is False" % (i)

def inclusive(number):
    if number >= 0 and number <= 9:
        print "%d is between 0 and 9 inclusive." % (number)
    else:
        print "%d is not between 0 and 9 inclusive." % (number)

inclusive(0)
inclusive(9)
inclusive(-1)
inclusive(10)

def position(number):
    my_list = [1,2,3]
    print my_list
    if number == my_list[0] or number == my_list[1]:
        print "%d is in the first two elements of my_list" % (number)
    elif number == my_list[0] or number == my_list[1]:
        print "%d is in the first two elements of my_list" % (number)
    else:
        print "%d is not in the first two elements of my_list"  % (number)
    
position(1)
position(2)
position(3)

fridge = {"milk":"White wet stuff",
          "cheese":"Yellow firm stuff",
          "mushrooms":"Taupe squishy stuff",
          "jam":"Red sticky stuff"}
fridge_list = fridge.keys()  #Create a list of keys in 'fridge'
food_sought = "mushrooms"
for key in fridge_list:  #Iterate through list of keys in 'fridge'
    if key == food_sought:  #On each iteration test the key against 'food_sought'
        print "Key is %s and value is %s" % (key, fridge[key]) #key & value assigned to that key
        break #Break out of 'if' when key matches 'food_sought'
    else:
        print "%s was not found in the fridge." % (food_sought)
        
print fridge_list
item_count = len(fridge_list)
current_key = fridge_list.pop(0)
while fridge.__contains__(current_key) == True and item_count > 0:
    print "%s is in the fridge." % (current_key)
    current_key = fridge_list.pop(0)
    item_count = len(fridge_list)
else:
    print "%s was not found in the fridge." % (current_key)

#This comment is to record a change for git

#This is another comment to verify commits to github


    
    
    
    
    
    
    
    
    
    
    



