class Restaurant:
    def __init__(self, ristorante: str, cucina: str, num: int = 0) -> None:
        self.ris = ristorante
        self.cuc = cucina
        self.num_served = num
    
    def describe_restaurant(self):
        print(f"Nome ristorante: {self.ris}, cucina di tipo {self.cuc}\n")
    
    def open_restaurant(self):
        print(f"Il nuovo ristorante {self.ris} è aperto!")
    
    def set_num_served(self, new_number_served: int):
        self.num_served = new_number_served 
    
    def increment_number(self):
        self.num_served += 1
    
    def increment_number_served(self, increment: int):
        self.num_served += increment
