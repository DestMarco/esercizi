class user:
    def __init__ (self, first_name:str, last_name:str, age:int, cf:int, email:str):
        self.sirst_name=first_name
        self.last_name=last_name
        self.age=age
        self.cf=cf
        self.email=email

    def greet_user(self):
        print(f"Hello {self.sirst_name}. come va?")
    def __str__(self) ->str:
        return f"User(name={self.sirst_name})"\
        +f"username={ self.last_name}"
user1= user(first_name="Lorenzo",
            age=22, last_name="Maggi",
            email="lorenzo.maggi@gmail.com",
            cf="MGGLNZ01L07H50IL")
print(user)

print("------------------------------------------------------------------------------------")
