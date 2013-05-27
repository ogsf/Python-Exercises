'''
Created on May 25, 2013

@author: Kevin
'''
filler = ("String", "filled", "by", "a tuple")
print "A %s %s %s %s" % filler

a = ("first", "second", "third")
print "The first element of the tuple is %s" % (a[0])
print "The second element of the tuple is %s" % (a[1])
print "The third element of the tuple is %s" % (a[2])

print "Use 'len' to return the number of elements in a tuple"
print "So I type 'print %d' %% len(a)' and I see:"
print "%d" % len(a)

breakfast = ["pot of coffee", "pot of tea", "slice of toast", "egg"]
count = 0
a = "a"
for count in range(len(breakfast)):
    if breakfast[count][0] == "e":
        a = "an"
    print "Today's breakfast includes %s %s" % (a, breakfast[count])
    a = "a"
breakfast.append("waffle")
print "Today's breakfast also includes %s %s" % (a, breakfast[4]) + "."

# print "Breakfast includes a",
# for element in breakfast:
#     print element + ", ",
#     #print element + ", ".join(map(str,breakfast)) + ".",

punctuation = ", "
count = 0
#print len(breakfast)
print "Breakfast includes a",
for item in breakfast:
    count = count + 1
#    print count
    if count == len(breakfast):
        punctuation = "."
    print item + punctuation,



