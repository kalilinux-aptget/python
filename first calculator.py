import re
print("calculator program")
print("type quit to exit")
run= True
prev = 0
def operation():
     global prev
     global run
     if prev == 0:
       equation = input(" please enter values ")
     else:
         equation = input(str(prev))
     if equation == 'quit':
        run = False
     else:
        equation= re.sub('[a-zA-Z,.()" "]', '',equation)
        if prev==0:
            prev=eval(equation)
        else:
           prev=eval(str(prev)+ equation)
     print(prev)
while run:
    operation()
