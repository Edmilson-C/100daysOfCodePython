from password_generator import generate_password
from store import update_file

print("##############################################")
print("#  Welcome to Password Generator using JSON  #")
print("##############################################\n\n")
print("You gonna have to provide the website where the authentication is for, "
      "email and password or one will me be generated for you")

website = input("Add the website: ").strip()
email = input("Your email: ").strip()
password = input("Your password: ").strip()

if len(password) == 0:
    password = generate_password()

data = {
    website: {
        email: email,
        password: password
    }
}

update_file(data, "pwd.json")

print(f"Website: {website}")
print(f"Email: {email}")
print(f"Password: {password}")
# print(f"You have {pwd_saved} passwords saved")
