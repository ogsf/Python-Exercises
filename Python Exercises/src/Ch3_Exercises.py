'''
Created on May 26, 2013

@author: Kevin
'''
dairy_section = ["butter", "eggs", "cream", "milk"]

print "The list 'dairy_section' has %d items." % (len(dairy_section))
print "The first item is %s and the last item is %s." % (dairy_section[0], dairy_section[-1])

milk_expiration = {"month": 12, "day": 10, "year": 2005}
mx = milk_expiration  
print "This milk carton will expire on %d/%d/%d." % (mx["month"], mx["day"], mx["year"])
milk_carton = {}
milk_carton = {"expiration_date" : milk_expiration, "fl_oz" : 16, "Cost" : 3.25, "brand_name" : "Horizon"}
print milk_carton.values()
def milk_cost(quantity):
    return quantity * milk_carton["Cost"]
print "Six cartons cost $%.02f" % milk_cost(6)

cheeses = ["gouda", "camonbert", "cheddar", "Colby", "Jack", "Swiss"]
print dairy_section
dairy_section.extend(cheeses)
print dairy_section
dairy = len(dairy_section)
cheese = len(cheeses)
for i in range((dairy - cheese),dairy):
    dairy_section.pop(-1)
print dairy_section
print "Number of cheeses in the cheese list is %d" % (len(cheeses))
for i in range(0,5):
    print cheeses[0][i],

