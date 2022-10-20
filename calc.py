uruchomienie = "t"
while uruchomienie == "t":
    liczba1 = int(input("Podaj pierwsza liczbe "))
    liczba2 = int(input("Podaj druga liczbe "))
    dzialanie = input("jakie dzialanie chcesz wykonac: 1 - mnozenie, 2 - dzielenie, 3 - dodawanie, 4 -odejmowanie, 5 - potegowanie")

    if dzialanie == '1':
            print(liczba1*liczba2)
    elif dzialanie == '2':
        if liczba2 == 0:
            print("nie dzielimy przez zero")
            while liczba2 == 0:
                    print("podaj inna licznbe2 ")
                    liczba2 = int(input('podaj liczbe numer 2 jedszcze raz'))
            print(liczba1 / liczba2)
    elif dzialanie == '3':
            print(liczba1+liczba2)
    elif dzialanie == '4':
            print(liczba1-liczba2)
    elif dzialanie == '5':
        print(liczba1**liczba2)
    else:
            print("podales zly operator")
    uruchomienie = input("czy chcesz uruchomic program jeszcze raz wybierz t, jezeli chcesz zakonczyc nacisnij n ")



