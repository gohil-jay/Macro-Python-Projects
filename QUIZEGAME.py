print("Wlecome to my computer quiz!")

playing=input("Do you want to play?")

if playing.lower()!="yes":
    quit()
print("Okay! let's play:")

score=0

answer=input("what does CPU stand for?")
if answer.lower()=="central processing unit" :
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("what does GPU stand for?")
if answer.lower()=="graphics processing unit" :
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("what does RAM stand for?")
if answer.lower()=="random access memory" :
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("EEPROM stands for _______?")
if answer.lower()=="Electronic Erasable Programmable Read Only Memory" :
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("BCD is _______?")
if answer.lower()=="Binary Coded Decimal" :
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got"+str(score)+"question correct!")
print("you got"+str((score/4)*100)+"%")
