colors =[ "red" , "blue", "green"]

print (colors [0])
print (colors [1])
print (colors [2])
print (colors [-1])
print (len(colors))

colors.append("yellow")
colors.remove("green")

for color in colors:
      print("i like ", color)


marks = [56,84,88,95,105]

for mark in marks:
    print("student marks:" , mark)

print ("First student Marks are:" , marks [0])
print ("First student Marks are:" , marks [-5])
print ("Fifth student Marks are:" , marks [-1])
print (("total students:") , len(marks))
marks.append(98)
for mark in marks:
    print("student marks:" , mark)
marks.remove(88)
for mark in marks:
    print("student marks:" , mark)

print ("THE SUM OF THE LIST IS:",   sum(marks))
print ("THE MAXIMUM OF THE LIST IS:",   max(marks))