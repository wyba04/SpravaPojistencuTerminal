import sys as _sys
import subprocess as _subprocess
from kontroly import Kontroly


class Menu:

    def _vycisti_obrazovku(self):
        """
        Vyčištění obrazovky po zadání hodnoty
        """
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    def volba_akce_menu(self, pocet_polozek_menu, width):
        """
        Výpis menu a výběr z nabídky
        vrací číslo vybrané nabídky
        """
        Menu._vycisti_obrazovku(self)
        Menu.vypis_hlavicky_menu(self, width)
        zadane_cislo = Kontroly.kontrola_vstup_cislo(self, "Zadej číslo akce, kterou chceš pokračovat:\n")
        if zadane_cislo in range(1, pocet_polozek_menu + 1):
            return zadane_cislo
        else:
            return 0

    def vypis_hlavicky_menu(self, width):
        """
        Vypis menu pro výpis možných voleb
        """
        Menu.vypis_hlavicky_volby(self, "Vyber si akci:", width)
        print(" 1 - Pridat nového pojistníka\n" +
              " 2 - Vypsat všechny pojištěné\n" +
              " 3 - Vyhledat pojištěného\n" +
              " 4 - Ukončení aplikace\n" + "-" * width)

    def vypis_hlavicky_volby(self, nazev_volby, width):
        """
        Pevná struktura hlavičky pro všechny volání volby z menu s přidáním doplňkového textu
        """
        print("=" * width + "\n" + " Evidence pojištěných\n" + " " + nazev_volby + "\n" + "=" * width)

    def volba_pokracovat_akce(self):
        """
        Vyvolení kontroly zda pokračovat ve vybrané volbě
        """
        dotaz = input("Chcete pokračovat ve vyhledávání? (ano = Y, ne = N:)\n")
        if dotaz.lower() == "y":
            return True
        else:
            return False

