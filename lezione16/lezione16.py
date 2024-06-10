"""
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

"""

class Media:
    def __init__(self):
        self.title=None
        self.reviews=[]

    def set_title(self,title):
        self.title=title

    def get_title(self):
        return self.title
    def aggiungiValutazione(self,voto:int):
        if 1<= voto <=5:
            self.reviews.append(voto)
        else:
            print("il voto deve essere compreso tra 1 a 5")

    def getMedia (self):
        if self.reviews:
            return sum (self.reviews)/len (self.reviews)
        return 0
    
    def getRate(self):
        media=self.getMedia()
        if media >=4.5:
            return"Grandioso"
        elif media >= 3.5:
            return "Bello"
        elif media >= 2.5:
            return "Normale"
        elif media >= 1.5:
            return "Brutto"
        else:
            return "Terribbile"
    
    def getPercentage(self, voto):
        total_reviews = len(self.reviews)
        count = self.reviews.count(voto)
        return (count / total_reviews) * 100 if total_reviews > 0 else 0

    def ratePercentage(self):
        print(f"Titolo del Media: {self.get_title()}")
        print(f"Voto medio: {self.getMedia():.2f}")
        print(f"Giudizio: {self.getRate()}")
        for i in range(1, 6):
            percentage = self.getPercentage(i)
            if i == 1:
                print(f"Terribile: {percentage:.2f}%")
            elif i == 2:
                print(f"Brutto: {percentage:.2f}%")
            elif i == 3:
                print(f"Normale: {percentage:.2f}%")
            elif i == 4:
                print(f"Bello: {percentage:.2f}%")
            elif i == 5:
                print(f"Grandioso: {percentage:.2f}%")


class Film(Media):
    def __init__(self):
        super().__init__()


film1 = Film()
film1.set_title("Matrix")
film2 = Film()
film2.set_title("The Lord of the Rings")
           
ratings_film1=[5,2,1,5,4,1,2,5,5,4,2,1,1,1] 
ratings_film2=[5,2,1,5,4,3,2,5,5,4,2,3,5,5] 

for rating in ratings_film1:
    film1.aggiungiValutazione(rating)

for rating in ratings_film2:
    film2.aggiungiValutazione(rating)


film1.ratePercentage()
print()
film2.ratePercentage()

           
print("-------------------------------------------------------------------------------------")

class Contatore:
    def __init__(self):
        self.conteggio = 0

    def setZero(self):
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1

    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")

    def get(self):
        return self.conteggio

    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")

# Test examples
c = Contatore()  
c.add1() 
c.mostra()

c = Contatore()  
c.sub1()  
c.mostra()

c = Contatore() 
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()  
c.add1()
c.add1()
z  = c.get()
print(z)



print("---------------------------------------------------------------------------------------------")

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def create_recipe(self, name, ingredients):
        if name in self.recipes:
            return f"Errore: La ricetta '{name}' esiste già."
        self.recipes[name] = ingredients
        return {name: ingredients}

    def add_ingredient(self, r_n, ingredient):
        if r_n not in self.recipes:
            return f"Errore: La ricetta '{r_n}' non esiste."
        if ingredient in self.recipes[r_n]:
            return f"Errore: L'ingrediente '{ingredient}' esiste già nella ricetta '{r_n}'."
        self.recipes[r_n].append(ingredient)
        return {r_n: self.recipes[r_n]}

    def remove_ingredient(self, r_n, ingredient):
        if r_n not in self.recipes:
            return f"Errore: La ricetta '{r_n}' non esiste."
        if ingredient not in self.recipes[r_n]:
            return f"Errore: L'ingrediente '{ingredient}' non è presente nella ricetta '{r_n}'."
        self.recipes[r_n].remove(ingredient)
        return {r_n: self.recipes[r_n]}

    def update_ingredient(self, r_n, o_ing, new_ing):
        if r_n not in self.recipes:
            return f"Errore: La ricetta '{r_n}' non esiste."
        if o_ing not in self.recipes[r_n]:
            return f"Errore: L'ingrediente '{o_ing}' non è presente nella ricetta '{r_n}'."
        index = self.recipes[r_n].index(o_ing)
        self.recipes[r_n][index] = new_ing
        return {r_n: self.recipes[r_n]}

    def list_recipes(self):
        return list(self.recipes.keys())

    def list_ingredients(self, r_n):
        if r_n not in self.recipes:
            return f"Errore: La ricetta '{r_n}' non esiste."
        return self.recipes[r_n]

    def search_recipe_by_ingredient(self, ingredient):
        found_recipes = [name for name, ingredients in self.recipes.items() if ingredient in ingredients]
        if not found_recipes:
            return f"Errore: Nessuna ricetta contiene l'ingrediente '{ingredient}'."
        return found_recipes

# Test examples
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
print(manager.list_recipes())
print(manager.search_recipe_by_ingredient("Pomodoro"))
print(manager.search_recipe_by_ingredient("Peperoni"))



print("------------------------------------------------------------------------------------------------------------")


class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

# Esempio di utilizzo:
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo()
auto.descrivi_veicolo()
moto.descrivi_veicolo()
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
            


        


