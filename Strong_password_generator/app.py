import random, time, string

def passgen(len):
  time.sleep(1.5)  
  print("Generating a strong password...")
  
  lower = string.ascii_lowercase
  time.sleep(1.5)
  print("Adding lowercase characters...")
  
  upper = string.ascii_uppercase
  time.sleep(1.5)
  print("Adding uppercase characters...")
  
  num = string.digits
  time.sleep(1.5)
  print("Adding symbols...")
  
  symbols = string.punctuation
  time.sleep(1.5)
  print("Shuffling the data to make password strong")
  
  combined = lower + upper + num + symbols
  temp = random.sample(combined,len)
  pd = "".join(temp)
  return pd
  
len = int(input("Enter length of the password you want : "))

password = passgen(len)
time.sleep(1)
print(f"\nYour strong password is : {password}")
