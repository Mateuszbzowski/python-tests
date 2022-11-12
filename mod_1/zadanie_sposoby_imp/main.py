from mod_1.zadanie_sposoby_imp.shop.orders import create_new_order


#zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości stworzy nowe zamówienie i doda je do listy zamówień.
# Zamówienie składa się z nazwy produktu, zamówionej ilości i łącznej ceny. Obydwa pliki umieść w pakiecie.
#
# Sklep uruchom poprzez plik main, w którym zaimportujesz funkcje do tworzenia zamówienia, wczytasz dane od użytkownika i wypiszesz łączny koszt zakupów.
# Zastosuj importowanie absolutne postaci from … import.
i = True
def run_shop(i):
    while i != "x":
        print("Witaj w sklepie!")
        product_name = input("Jaki towar chcesz kupic?")
        quantity = int(input(f"Podaj ilosc w kg/szt:"))

        result = create_new_order(product_name, quantity)
        if result is not None:
            total_price = result["total_price"]
            print (f"Twoja cena to {total_price} PLN")
        i = input("Dziękujemy za wybranie naszego sklepu, jeśli nie chcesz kupić więcej produktów wpisz 'x'")

if __name__ == "__main__":
    run_shop(i)


