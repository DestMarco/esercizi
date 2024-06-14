class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione *= (1 + self.tasso_crescita / 100)

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 1
        max_anni = 1000

        while self.popolazione <= altra_specie.popolazione and anni < max_anni:
            self.cresci()
            altra_specie.cresci()
            anni += 1

        return anni if anni < max_anni else -1

    def getDensita(self, area_kmq: float) -> int:
        anni = 0

        while self.popolazione / area_kmq <= 4:
            self.cresci()
            anni += 1

        return anni


class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)


class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)


bufalo_klingon = BufaloKlingon(100, 15)
elefante = Elefante(10, 35)

anni_necessari = elefante.anni_per_superare(bufalo_klingon)
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

anni_densita = bufalo_klingon.getDensita(1500)
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")