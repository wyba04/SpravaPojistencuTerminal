class Kontroly:

    def kontrola_vstup_cislo(self, text_dotaz="Zadej číslo:\n", text_chyba="Vaše zadání není číslo, opakuj zadání:"):
        """
        Vyhodnocení správnosti zadání vstupu čísla
        Kontrola, zda je vstup číslo, Ze vstupu odstraněny mezery pro potřeby sjednocení čitelnosti pro výpis
        """
        spatne = True
        while spatne:
            try:
                cislo_vstup = str(input(text_dotaz))
                # vymazání prázdných znaků ze vstupu
                cislo = int("".join(cislo_vstup.split(" ")))
            except ValueError:
                print(text_chyba)
            else:
                return cislo

    def kontrola_vek(self, text_dotaz, vek_limit, text_chyba_cislo):
        """
        Vyhodnocení správnosti zadání čísla
        Kontrola na délku čísla na max 3 čísla + max věk
        """
        znovu = True
        while znovu:
            cislo_vstup = str(input(text_dotaz))
            if Kontroly.__kontrola_cislo(self, cislo_vstup):  # nejdříve kontrola vstupu, že jde o číslo
                if int(cislo_vstup) > vek_limit:
                    print(f"Chybná hodnota věk:\"{cislo_vstup}\".\nTak starý nemůže být.")
                    znovu = True
                else:
                    znovu = False
                    return cislo_vstup
            else:
                print(f"Chybná hodnota věk:\"{cislo_vstup}\".\n{text_chyba_cislo}")
                znovu = True

    def kontrola_tel_cislo_delka(self, text_dotaz, min_delka, text_chyba_cislo, text_chyba_delka, max_delka, text_chyba_max_delka):
        """
        Vyhodnocení správnosti zadání tel. čísla, min délka, max délka, jestli je zadáno číslo
        """
        znovu = True
        while znovu:
            cislo_vstup = str(input(text_dotaz))
            if Kontroly.__kontrola_cislo(self, cislo_vstup):  # nejdříve kontrola vstupu, že jde o číslo
                if len(str(cislo_vstup)) < int(min_delka):  # poté kontrola délky vstupu
                    print(f"Chybná hodnota \"{cislo_vstup}\".\n{text_chyba_delka}! Min. délka {min_delka} znaků.")
                    znovu = True
                else:
                    if len(str(cislo_vstup)) > int(max_delka):
                        print(f"Chybná hodnota \"{cislo_vstup}\".\n{text_chyba_max_delka}! Min. délka {max_delka} znaků.")
                        znovu = True
                    else:
                        znovu = False
                        return cislo_vstup
            else:
                print(f"Chybná hodnota \"{cislo_vstup}\".\n{text_chyba_cislo}")
                znovu = True

    def __kontrola_cislo(self, cislo_vstup):
        """
        Kontrola, že vstupní hodnota je číslo,
        vrací True nebo False
        """
        try:
            # vymazání prázdných znaků ze vstupu
            cislo = int("".join(cislo_vstup.split(" ")))
        except ValueError:
            return False
        else:
            return True


    def uprava_delka_text(self, text, max_delka):
        """
        Funkce pro úpravu délky vstupu z input
        """
        self.text = str(text)
        self.max_delka = max_delka
        if len(self.text) > max_delka:
            return self.text[:max_delka]
        else:
            return self.text + (" " * (max_delka - len(self.text)))

    def kontrola_delka_vstup(self, text_dotaz, max_delka):
        """
        Funkce pro kontrolu délky vstupu ze vstupu
        """
        znovu = True
        while znovu:
            text_vstup = str(input(text_dotaz))
            if len(text_vstup) > max_delka:
                print(f"Zadána příliš dlouhá hodnota.")
                znovu = True
            else:
                znovu = False
                return text_vstup

