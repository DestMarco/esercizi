"""


1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat,
 health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali.
 I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un nome, 
un cognome, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo.
 L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width)
 vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo.
 Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia
   è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale)
 con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) 
 ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.
"""

#I create a class for animal
class Animal:
# I define values ​​for the object for the class animal
    def __init__(self,name:str, species:str, age:int, height:float, width:float, preferred_habitat:str,
 health:float):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.health=health
        
        self.reci=None

#I create a class for fence 
class Fence:
# I define values ​​for the object for the class fence
    def __init__(self,animal:list[Animal], area:float, temperature:float, habitat:str):
        self.animal=animal
        self.area=area
        self.temperature=temperature
        self.habitat=habitat

#I create a class for zookeeper
class ZooKeeper:
# I define values ​​for the object for the class zookeeper
    def __init__(self,nome:str, cognome:str, id:str) :
        self.nome=nome
        self.cognome=cognome
        self.id=id
    # i create a function that allows the zookeeper to add an animal and allows him to calculate the area occupied by an animal 
    def add_animal(self,animal:Animal,fence:Fence):
        
        if animal.preferred_habitat != fence.habitat and fence.area < animal.width*animal.height:
            pass    
        else:
            fence.animal.append(animal.name)
            
            animal.reci=fence

            fence.area=fence.area-(animal.height*animal.height)

    
    # i create a function that allows the zookeeper to remove an animal from a fance and to calculate the area that the animal was occuping 
    def remove_animal(self,animal:Animal,fence:Fence):
        fence.animal.remove(animal)
       

        fence.area=fence.area+(animal.height*animal.width)
    def feed(self, animal: Animal):
        # Check if there is enough space in the enclosure for the enlarged animal
        if  animal.reci.area  >= (animal.height * 1.02) * (animal.width * 1.02):
            # Increase the animal's health by 1%
            animal.health *= 1.01
            # Increase the dimensions of the animal by 2%
            animal.height *= 1.02
            animal.width *= 1.02
        

#I create a class for zoo
class zoo:
# I define values ​​for the object for the class zoo
    def __init__(self, fences :list[Fence], zoo_keeper: list[ZooKeeper] ) -> None:
        self.fences=fences
        self.zoo_keeper=zoo_keeper
   
        

        
  


