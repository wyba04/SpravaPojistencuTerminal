
class Pojistenec:
    """
    Třída reprezentující pojištěnce
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """
        Výpis pojištěnce
        """
        return f"{self.jmeno}  {self.prijmeni}  Věk:{self.vek} Tel:{self.telefon}"


