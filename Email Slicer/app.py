email = input("Enter the Email : ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print("")
print("Username :", username)
print("Domain :", domain)
