class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")

class Admin(User,Privileges):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)  # Utilizza la classe Privileges come attributo
    
    def show_privileges(self):
        self.privileges.show_privileges()  # Chiama il metodo show_privileges() della classe Privileges