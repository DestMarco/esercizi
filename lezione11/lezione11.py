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
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name={self.name}, quantity={self.quantity})"

class Warehouse:
    def __init__(self):
        self.products = {}

    def add_merchandise(self, product: Products):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def search_product(self, name: str):
        return self.products.get(name, None)

    def check_availability(self, name: str) -> str:
        pt = self.search_product(name)
        if pt and pt.quantity > 0:
            return f"The product '{name}' is available in quantities of {pt.quantity} units."
        else:
            return f"The product '{name}' is not available in stock."

warehouse = Warehouse()


product1 = Products("Laptop", 10)
product2 = Products("Smartphone", 5)
product3 = Products("Tablet", 2)


warehouse.add_merchandise(product1)
warehouse.add_merchandise(product2)
warehouse.add_merchandise(product3)


product4 = Products("Laptop", 5)
warehouse.add_merchandise(product4)


product_searched = warehouse.search_product("Smartphone")
print(f"Product searched for: {product_searched}")

availability_laptop = warehouse.check_availability("Laptop")
smartphone_availability = warehouse.check_availability("Smartphone")
tablet_availability = warehouse.check_availability("Tablet")
availability_smartwatch = warehouse.check_availability("Smartwatch")

print(availability_laptop)
print(smartphone_availability)
print(tablet_availability)
print(availability_smartwatch)
    
print("---------------------------------------------------------------------------------------------------------------")

"""
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri 
e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo,
prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile.
    Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, 
    restituisce un messaggio di errore.
    
    Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
    """



class Libro:
    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo
        self.autore = autore
        self.prestato = False  # Il libro è inizialmente disponibile

    def __repr__(self):
        stato = "Disponibile" if not self.prestato else "Prestato"
        return f"Libro(titolo='{self.titolo}', autore='{self.autore}', stato='{stato}')"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def aggiungi_libro(self, libro: Libro):
        if libro.titolo in self.catalogo:
            return f"Il libro '{libro.titolo}' è già presente in catalogo."
        else:
            self.catalogo[libro.titolo] = libro
            return f"Libro '{libro.titolo}' aggiunto al catalogo."

    def presta_libro(self, titolo: str):
        if titolo in self.catalogo:
            libro = self.catalogo[titolo]
            if libro.prestato:
                return f"Il libro '{titolo}' è già stato prestato."
            else:
                libro.prestato = True
                return f"Il libro '{titolo}' è stato prestato con successo."
        else:
            return f"Il libro '{titolo}' non è presente in catalogo."

    def restituisci_libro(self, titolo: str):
        if titolo in self.catalogo:
            libro = self.catalogo[titolo]
            if libro.prestato:
                libro.prestato = False
                return f"Il libro '{titolo}' è stato restituito con successo."
            else:
                return f"Il libro '{titolo}' non era prestato."
        else:
            return f"Il libro '{titolo}' non è presente in catalogo."

    def mostra_libri_disponibili(self):
        libri_disponibili = [libro.titolo for libro in self.catalogo.values() if not libro.prestato]
        if libri_disponibili:
            return f"Libri disponibili: {', '.join(libri_disponibili)}"
        else:
            return "Nessun libro disponibile in questo momento."


biblioteca = Biblioteca()

libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Il Nome della Rosa", "Umberto Eco")

print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.aggiungi_libro(libro3))

print(biblioteca.presta_libro("1984"))

print(biblioteca.presta_libro("1984"))


print(biblioteca.restituisci_libro("1984"))

print(biblioteca.restituisci_libro("Il Signore degli Anelli"))

print(biblioteca.mostra_libri_disponibili())


print(biblioteca.presta_libro("Il Nome della Rosa"))

print(biblioteca.mostra_libri_disponibili())

print("---------------------------------------------------------------------------------------------------------------")

"""
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere,
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo.
    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista.
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo.
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se 
    nessun film contiene la parola cercata nel titolo.
"""




class MovieCatalog:
    def __init__(self):
        self.catalog = {}
    
    def add_movie(self, director_name, movies):
        if director_name in self.catalog:
            self.catalog[director_name].extend(movies)
        else:
            self.catalog[director_name] = movies
    
    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:  
                    del self.catalog[director_name]
            else:
                print(f"Il film '{movie_name}' non esiste nel catalogo del regista '{director_name}'.")
        else:
            print(f"Il regista '{director_name}' non esiste nel catalogo.")
    
    def list_directors(self):
        return list(self.catalog.keys())
    
    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return f"Il regista '{director_name}' non è presente nel catalogo."
    
    def search_movies_by_title(self, title):
        result = {}
        for director, movies in self.catalog.items():
            matching_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matching_movies:
                result[director] = matching_movies
        if result:
            return result
        else:
            return f"Nessun film contiene la parola '{title}' nel titolo."


catalog = MovieCatalog()
catalog.add_movie("Steven Spielberg", ["Jurassic Park", "E.T."])
catalog.add_movie("Christopher Nolan", ["Inception", "Interstellar"])
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill"])

print(catalog.list_directors())
print(catalog.get_movies_by_director("Christopher Nolan"))
print(catalog.search_movies_by_title("Inception"))
catalog.remove_movie("Steven Spielberg", "E.T.")
print(catalog.get_movies_by_director("Steven Spielberg"))