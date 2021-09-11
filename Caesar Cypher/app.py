def encrypt(message, num):
    result = ""
    for i in range( len(message) ):
        char = message[i]
        if (char.isupper()):
            result += chr((ord(char) + num-65) % 26 + 65) 
        else:
            result += chr((ord(char) + num-97) % 26 + 97)
 
    return result

def decrypt(message, num):
    result = ""
    for i in range( len(message) ):
        char = message[i]
        if (char.isupper()):
            result += chr((ord(char) - num-65) % 26 + 65) 
        else:
            result += chr((ord(char) - num-97) % 26 + 97)
 
    return result

message = input("Enter the message : ")
print("\n")
num = int(input("Enter ciper shift : "))
print("\n")

message1 = encrypt(message, num)
message2 = decrypt(message1, num)

print("The encrypted message is : ", message1)
print("The decrypted message is : ", message2)
