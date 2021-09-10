def encrypt(message, num):
    result = ""
    for i in range( len(message) ):
        char = message[i]
        if (char.isupper()):
            result += chr((ord(char) + num-65) % 26 + 65) 
        else:
            result += chr((ord(char) + num-97) % 26 + 97)
 
    return result

message = input("Enter the message : ")
print("\n")
num = int(input("Enter ciper shift : "))
print("\n")

en = encrypt(message, num)

print("The encrypted message is : ", en)
