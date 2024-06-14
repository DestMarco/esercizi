"""Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale 
metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor().
In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare
0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare
un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
    getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene 
calcolato moltiplicando la parcella del dottore per il numero di pazienti.
    getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) 
che ha il dottore e ritornare il suo valore.
    addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi
il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor 
cognome è stato aggiunto il paziente {codice_identificativo}"
    removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il 
codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo 
get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
"""

from pazziente import Paziente
from dottore import Dottore

class Fattura:
    def __init__(self, patients, doctor):
        if doctor.getAge() is not None and doctor.getAge() > 30:
            self.patients = patients
            self.doctor = doctor
            self.__fatture = len(patients)
            self.__salary = 0
        else:
            self.patients = None
            self.doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")
    
    def getSalary(self):
        if self.doctor is not None:
            self.__salary = self.__fatture * self.doctor.getParcel()
            return self.__salary
        return None
    
    def getFatture(self):
        if self.patients is not None:
            self.__fatture = len(self.patients)
            return self.__fatture
        return None
    
    def addPatient(self, newPatient):
        if self.patients is not None:
            self.patients.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode):
        if self.patients is not None:
            for patient in self.patients:
                if patient.getIdCode() == idCode:
                    self.patients.remove(patient)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato rimosso il paziente {idCode}")
                    return
            print(f"Il paziente con codice identificativo {idCode} non è stato trovato nella lista.")
        else:
            print("Non è possibile rimuovere il paziente poiché la lista dei pazienti non è valida.")
