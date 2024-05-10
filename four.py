import json

class contactManager:

    def __init__(self,path="-"):
        self.contact_list=[]
        
        if path !="-":
            with open(path,"r") as con:
                data=con.read()
                self.contact_list=json.loads(data)
            
    def add(self,**person):
        self.contact_list.append(person)

    # def add(self ,name,tell):
    #     self.contact_list.append({
    #         "fname":name,
    #         "tell":tell})

    def search(self,name='',tell=0):
        self.search_list=[]

        if name != '':
            for i in self.contact_list:
                if name.lower() in i["fname"].lower():
                    self.search_list.append(i) 
                
        elif tell !=0 :
            for i in self.contact_list:
                if i["tell"]==tell:
                    self.search_list.append(i)
                
        if len(self.search_list)==0:
            return "no contact"
        else:
            return self.search_list   
   
    def show(self):
        for i in self.contact_list:
            print(f"{i}")

        with open("./project/contact.json","w")as con:
            con.write(json.dumps(self.contact_list))
            self.contact_list.clear()


    def backup(self):
        with open("./project/backup.json","w")as BU:
            BU.write(json.dumps(self.contact_list)+"\n")


l={"fname":"fatemeh","lname":"fati","tell":244}
k={"fname":"fati","lname":"fati","tell":244}
x={"fname":"fati","lname":"fati","tell":255}

c=contactManager(path="./project/contact.json")

c.add(**l)
c.add(**k)
c.add(**x)

# c.add("ali",222)
# c.add("amin",258)

# print(c.search("fatic"))
# print(c.search("fati"))
# print(c.search(tell=244))

c.backup()
c.show()






# with open("./scon.json","w")as con:
#     con.write(json.dumps(l))
# with open('./con.json','r')as con:
#     json.load(con)
