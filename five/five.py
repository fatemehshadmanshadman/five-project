#password generation

from cryptography.fernet import Fernet

# def key_generat():
#     key=Fernet.generate_key()
#     with open("./five/mykey.key","wb") as f:
#         f.write(key)
# key_generat()

def key_load():
    with open("./five/mykey.key","rb") as f:
        return f.read()
    
def view():
    with open("./five/pass.txt","r")as file:
        for item in file:
            item=item.rstrip()
            user,encrypt =item.split("|")
            password= keys.decrypt(encrypt).decode()
            print(f"username : {user} - password: {password}")

def add(username,password):
    with open("./five/pass.txt","a") as file:
        encrypt=keys.encrypt(password.encode()).decode()
        file.write(f"{username}|{encrypt}\n")
        print("added")


key=key_load()
keys=Fernet(key)

while True:
    mode=input("select mode (v:view  a:add  q:quit) : ")
    
    if mode=="v":
        view()

    elif mode=="a":
        username=input("enter username: ")
        password=input("enter password: ")
        add(username,password)
        
    elif mode=="q":
        break    
    
    else:
        print("wrong mode")