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
            return f"prenotazione effetuta per {num_posti} per la sala {self.numero} per il fil {self.film.titolo}"
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
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                
                return f"il film {titolo_film} è stato trovato " 
            else:
                return f"il film {titolo_film} non è stato trovato"

    
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