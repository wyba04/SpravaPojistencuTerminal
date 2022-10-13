from menu import Menu
from kontroly import Kontroly
from pojistenec import Pojistenec


class Evidence:
    """
       Evidence pojištěných
    """
    _pojistenci = []
    _width = 60
    _delka_text = 15
    _delka_vek = 3
    _delka_tel = 15
    _min_delka_tel = 9
    _pocet_polozek_menu = 4
    _vek_limit = 150


    def beh_programu(self):
        """
        Samotný běh programu evidence
        """
        pokracovat = True
        while pokracovat:
            volba = Menu.volba_akce_menu(self, self._pocet_polozek_menu, self._width)
            if volba == 1:  # přidání pojištěnce
                self.sber_dat_pojistenec(self._width, self._delka_text, self._delka_tel, self._min_delka_tel)
            elif volba == 2:  # výpis všech pojištěnců
                self.vypis_komplet(self._width, self._delka_text, self._delka_vek, self._delka_tel)
            elif volba == 3:  # vyhledání pojištěnce
                self.vyhledat(self._width, self._delka_text, self._delka_vek, self._delka_tel)
            elif volba == 4:
                pokracovat = False
                print("Ukončuji aplikaci, děkuji za její použití.")
                input("Pro ukončení stikni ENTER")
            else:
                pass

    def vyhledat(self, width, delka_text, delka_vek, delka_tel):
        """
        Funkce pro vyhledávání v seznamu pojištěnců,
        zajištěná velikost vstupu písma převedením vstupu na capitalize - stejný format jako v uloženém seznamu
        """
        pokracovat = True
        while pokracovat:
            Menu._vycisti_obrazovku(self)
            Menu.vypis_hlavicky_volby(self, "Vyhledávání pojištěnce:", width)
            self.jmeno = str(input("Zadej jméno hledaného pojištěnce:\n")).capitalize()
            self.prijmeni = str(input("Zadej příjmení hledaného pojištěnce:\n")).capitalize()
            pocet_shod = 0
            for i in range(len(self._pojistenci)):
                if self._pojistenci[i][0] == self.jmeno.strip() and self._pojistenci[i][1] == self.prijmeni.strip():
                    jmeno = Kontroly.uprava_delka_text(self, self._pojistenci[i][0], delka_text)
                    prijmeni = Kontroly.uprava_delka_text(self, self._pojistenci[i][1], delka_text)
                    vek = Kontroly.uprava_delka_text(self, self._pojistenci[i][2], delka_vek)
                    tel = Kontroly.uprava_delka_text(self, self._pojistenci[i][3], delka_tel)
                    print(Pojistenec(jmeno, prijmeni, vek, tel))
                    """
                    print(Pojistenec(Kontroly.uprava_delka_text(self, self._pojistenci[i][0], delka_text),
                               Kontroly.uprava_delka_text(self, self._pojistenci[i][1], delka_text),
                               Kontroly.uprava_delka_text(self, self._pojistenci[i][2], delka_vek),
                               Kontroly.uprava_delka_text(self, self._pojistenci[i][3], delka_tel)))
                    """
                    pocet_shod += 1
            if pocet_shod == 0:
                print(f"Hledaný {self.jmeno.strip()} {self.prijmeni.strip()} není v evidenci")
            if Menu.volba_pokracovat_akce(self):
                pokracovat = True
                pocet_shod = 0
            else:
                pokracovat = False

    def sber_dat_pojistenec(self, width, delka_text, delka_tel, min_delka_tel):
        """
        Metodat pro sběr dat pro vložení zaměstnance
        Jméno a příjmení po vstupu převedeno na capitalize u důvodu správné
        čitelnosti dat při výpisu, velikost písmen ve vstupu nemá vliv
        """
        Menu._vycisti_obrazovku(self)
        Menu.vypis_hlavicky_volby(self, "Zadání nového pojištěnce", width)
        temp_list = []
        temp_list.append(str(Kontroly.kontrola_delka_vstup(self, "Zadej Jmeno:\n", delka_text)).capitalize())
        temp_list.append(str(Kontroly.kontrola_delka_vstup(self, "Zadej příjmení:\n", delka_text)).capitalize())
        temp_list.append(Kontroly.kontrola_vek(self, "Zadej věk pojištěnce:\n", Evidence._vek_limit, "Zadaná hodnota není číslo."))
        temp_list.append(Kontroly.kontrola_tel_cislo_delka(self, "Zadej tel. číslo:\n", min_delka_tel, "Zadaná hodnota není číslo.", "Příliš krátké tel. číslo: ", delka_tel, "Zadané číslo je příliš dlouhé."))
        self.pridani_dat_do_seznamu(temp_list)

    def pridani_dat_do_seznamu(self, novy_pojistenec):
        """
        Vložení dat do seznamu pojištěnců
        """
        self._pojistenci.append(novy_pojistenec)

    def vypis_komplet(self, width, delka_text, delka_vek, delka_tel):
        """
        Kompletní výpis pojištěnců
        Texto postaven na pevné délky zobrazení pro konstatní přehled
        """
        # přidat hlavičku (jméno, příjmení, věk, tel. č.)
        Menu._vycisti_obrazovku(self)
        Menu.vypis_hlavicky_volby(self, "Výpis všech pojištěnců:", width)

        for i in range(len(Evidence._pojistenci)):
            jmeno = Kontroly.uprava_delka_text(self, self._pojistenci[i][0], delka_text)
            prijmeni = Kontroly.uprava_delka_text(self, self._pojistenci[i][1], delka_text)
            vek = Kontroly.uprava_delka_text(self, self._pojistenci[i][2], delka_vek)
            tel = Kontroly.uprava_delka_text(self, self._pojistenci[i][3], delka_tel)
            print(Pojistenec(jmeno, prijmeni, vek, tel))
            #print(f"{jmeno}  {prijmeni}  Věk:{vek} Tel:{tel}")
        if len(self._pojistenci) == 0:
            print("Evidence neobsahuje žádné pojištěnce.")
        print("-" * self._width)
        input("Stiskem ENTER přejdete do menu.")

