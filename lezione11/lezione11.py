"""
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, 
ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e 
prenotare posti per un determinato spettacolo.

 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, 
posti prenotati.
Metodi:

    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce 
        un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
Metodi:

    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un 
        messaggio di stato.
Test case:
Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
Un cliente sceglie un film e prenota un certo numero di posti.
Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

class Film:
    def __init__(self, titolo, durata) :
        self.titolo=titolo
        self.durata=durata
class Sala:
    def __init__(self, numeri, film, posti_totali) :
        self.numeri=numeri
        self.film=film
        self.posti_totali=posti_totali
        self.posti_prenotati=0
        
    def prenota_posti(self, num_posti):
        if self.posti_prenotati + num_posti <= self.posti_totali:
            self.posti_prenotati += num_posti
            return f"prenotazione effetuta per {num_posti} per la sala {self.numeri} per il fil {self.film.titolo}"
        else:
            return "Posti non disponibbili per questa prenotazione"
        
    def posti_disponibbili(self):
        return self.posti_totali -self.posti_prenotati
class Cinema:
    def __init__(self):
        self.sale=[]
    
    def aggiungi_sale(self,sala):
        self.sale.append(sala)
        
    def prenota_film(self,titolo_film,num_posti):
        a:int=0
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                msg = sala.prenota_posti(num_posti)
                return msg
                           

    
cinema=Cinema()
    
sala1 = Sala(1, Film("Il padrino", 180), 100)
sala2 = Sala(2, Film("Interstellar", 169), 80)
sala3 = Sala(3, Film("La La Land", 128), 120)


cinema.aggiungi_sale(sala1)
cinema.aggiungi_sale(sala2)
cinema.aggiungi_sale(sala3)



print(cinema.prenota_film("Interstellar", 3))  
print(cinema.prenota_film("Interstellar", 90))
print(cinema.prenota_film("Inception", 2))




print("---------------------------------------------------------------------------------------------------")

"""
Scrivi un programma in Python che gestisca un magazzino. Il programma
deve permettere di aggiungere prodotti al magazzino,
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:
Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente,
aggiunge i prodotti al magazzino.

Il sistema cerca un prodotto per verificare se esiste nell'inventario.
Il sistema verifica la disponibilità dei prodotti in inventario.
Last modified: Wednesday, 29 May 2024, 8:04 PM"""


class Products:
    def __init__(self, name:str, quantity:str):
        self.name=name
        self.quantity=quantity
        
    def __repr__(self) -> str:
        return f"Product(name={self.name}, quantity={self.quantity})"
    
class Warehouse:
    def __init__(self):
        self.Products={}
        
    def add_merchandise(self,product: Products):
        if product.name in self.Products:
            self.Products[product.name].quantity += product.quantity
        else:
            self.Products[product.name]=product
            
    def search_product (self, name: str):
        return self.Products.get(name, None)
    
    def check_availability(self, name:str) -> Products:
        pt=self.search_product(name)
        if pt and pt.quantity >0:
            return f"The product '{name}' is available in quantities of {pt.quantity} units."
        else:
            return f"The product '{name}' is not available in stock."
# Test cases
if __name__ == "__main__":
    # Creation of the warehouse
    warehouse = Warehouse()

    # Creation of products
    product1 = Products("Laptop", 10)
    product2 = Products("Smartphone", 5)
    product3 = Products("Tablet", 2)

    # Adding products to the warehouse
    warehouse.add_merchandise(product1)
    warehouse.add_merchandise(product2)
    warehouse.add_merchandise(product3)

    # Adding additional quantities of an already existing product
    product4 = Products("Laptop", 5)
    warehouse.add_merchandise(product4)

    # Search for a product
    product_searched = warehouse.search_product("Smartphone")
    print(f"Product searched for: {product_searched}")

    # Check product availability
    availability_laptop = warehouse.check_availability("Laptop")
    smartphone_availability = warehouse.check_availability("Smartphone")
    tablet_availability = warehouse.check_availability("Tablet")
    availability_smartwatch = warehouse.check_availability("Smartwatch")

    print( availability_laptop )
    print(smartphone_availability)
    print(tablet_availability)
    print( availability_smartwatch)
    
    
    