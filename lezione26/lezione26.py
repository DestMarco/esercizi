"""" 
Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto 
codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), 
dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il 
costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni lettera
 del testo sia spostata dal valore contenuto in chiave.
Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' 
sarà sostituita da 'f' e così via.

     Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c 
     da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il 
costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio 
sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna
 delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza 
 del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo
      cifrato da usare nel metodo codifica(testoInChiaro).


Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al 
    metodo sposta_carattere().

    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al
      metodo combinazione().


Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per 
entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato."""


from abc import ABC , abstractmethod

class CodificatoreMesaggi(ABC):
    def codifica(self, testoInChiaro):
       pass 

class DecodificaMesaggi(ABC):
    def decofica(self, testoCodificato):
        pass





class CifratoreAscorrimento(CodificatoreMesaggi,DecodificaMesaggi):

    def __init__(self,chiave):
        self.chiave=chiave

    def sposta_carattere(self, c, shift):
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - start + shift) % 26 + start)
        return c

    def codifica(self, testoInChiaro):
        return ''.join(self.sposta_carattere(c, self.chiave) for c in testoInChiaro)

    def decodifica(self, testoCodificato):
        return ''.join(self.sposta_carattere(c, -self.chiave) for c in testoCodificato)


class CifratoreACombinazione(CodificatoreMesaggi,DecodificaMesaggi):

    def __init__(self, n):
        self.n = n

    def combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        prima_metà = testo[:metà]
        seconda_metà = testo[metà:]
        combinato = []
        for i in range(metà):
            combinato.append(prima_metà[i])
            if i < len(seconda_metà):
                combinato.append(seconda_metà[i])
        return ''.join(combinato)

    def decodifica_combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        prima_metà = testo[::2]
        seconda_metà = testo[1::2]
        return prima_metà + seconda_metà

    def codifica(self, testoInChiaro):
        for _ in range(self.n):
            testoInChiaro = self.combinazione(testoInChiaro)
        return testoInChiaro

    def decodifica(self, testoCodificato):
        for _ in range(self.n):
            testoCodificato = self.decodifica_combinazione(testoCodificato)
        return testoCodificato


