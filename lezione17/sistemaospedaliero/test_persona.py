"""Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto 
funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono 
coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Persona
- Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi first_name, last_name e age.
  - Il funzionamento dei metodi setName, setLastName e setAge.

Test della Classe Dottore
- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Dottore.
  - Il funzionamento del metodo isValidDoctor con diverse età.

Test della Classe Paziente
- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Paziente.

Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista.
"""





import unittest
from persona import Persona
from dottore import Dottore
from pazziente import Paziente
from fattura import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")
    
    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Mario")
        self.assertEqual(self.persona.getLastName(), "Rossi")
        self.assertEqual(self.persona.getAge(), 0)
    
    def test_set_name(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.getName(), "Luigi")
    
    def test_set_last_name(self):
        self.persona.setLastname("Bianchi")
        self.assertEqual(self.persona.getLastName(), "Bianchi")
    
    def test_set_age(self):
        self.persona.setAge(25)
        self.assertEqual(self.persona.getAge(), 25)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Luigi", "Verdi", "Cardiologo", 150.0)
        self.dottore.setAge(45)
    
    def test_initialization(self):
        self.assertEqual(self.dottore.getName(), "Luigi")
        self.assertEqual(self.dottore.getLastName(), "Verdi")
        self.assertEqual(self.dottore.getAge(), 45)
        self.assertEqual(self.dottore.getSpecialization(), "Cardiologo")
        self.assertEqual(self.dottore.getParcel(), 150.0)
    
    def test_is_valid_doctor(self):
        self.dottore.setAge(31)
        self.assertTrue(self.dottore.getAge() > 30)
        self.dottore.setAge(29)
        self.assertFalse(self.dottore.getAge() > 30)

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Mario", "Rossi", "P001")
    
    def test_initialization(self):
        self.assertEqual(self.paziente.getName(), "Mario")
        self.assertEqual(self.paziente.getLastName(), "Rossi")
        self.assertEqual(self.paziente.getIdCode(), "P001")

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Luigi", "Verdi", "Cardiologo", 150.0)
        self.dottore.setAge(45)
        self.paziente1 = Paziente("Mario", "Rossi", "P001")
        self.paziente2 = Paziente("Luca", "Bianchi", "P002")
        self.fattura = Fattura([self.paziente1, self.paziente2], self.dottore)
    
    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 300.0)
    
    def test_add_patient(self):
        paziente3 = Paziente("Giulia", "Neri", "P003")
        self.fattura.addPatient(paziente3)
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 450.0)
    
    def test_remove_patient(self):
        self.fattura.removePatient("P002")
        self.assertEqual(self.fattura.getFatture(), 1)
        
        self.assertEqual(self.fattura.getSalary(), 150.0)

if __name__ == "__main__":
    unittest.main()
