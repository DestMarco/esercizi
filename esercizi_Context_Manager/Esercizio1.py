"""Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')"""


class FileManager:
    def __init__(self,filname,mode):
        self.filname=filname
        self.mode=mode
        self.file=None

    def __enter__(self):
        self.file=open(self.filname, self.mode)
        print("file aperto")
        return self.file
    
    def __exit__ (self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print("file Close")
        if exc_type is not None:
            print(f"Exception: {exc_type}, value : {exc_val}, Traceback{exc_tb}")
            return False 
    
with FileManager ('example.txt', 'w')as f:
    f.write("Hello,world")