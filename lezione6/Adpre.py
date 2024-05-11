from user import User
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin:
    def __init__(self, first_name, last_name, age, privileges):
        self.user = User(first_name, last_name, age)
        self.privileges = Privileges(privileges)
        
    def show_privileges(self):
        self.privileges.show_privileges()