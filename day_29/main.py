from password_generator import generate_password

print("#############################################")
print("#      Welcome to Password Generator        #")
print("#############################################\n\n")
print("You gonna have to provide the website where the authentication is for, "
      "email and password or one will me be generated for you")

website = input("Add the website: ").strip()
email = input("Your email: ").strip()
password = input("Your password: ").strip()

if len(password) == 0:
    password = generate_password()

with open("pwd.txt", mode="a") as file:
    file.write(f"{website};{email};{password}\n")

print("File generated successfully")
print(f"Website: {website}")
print(f"Email: {email}")
print(f"Password: {password}")