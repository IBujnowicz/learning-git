def is_it_Palindrom(x):
    x = x.lower().replace(" ", "") #zmiana liter na male i pozbycie się spacji
    n = len(x) #zmienna pomocnicza przechowujaca dlugosc slowa
    for i in range(n-1):
        if x[i] != x[n-1-i]: #jezeli znak po przeciwnej stronie (w tej samej kolejnosci od końca) nie bedzie taki sam, to słowo jest palindromem
         return False #zwroc false
        return True #jezeli zgadza się, zwroc true
print("Program sprawdzajacy czy slowo jest palindromem")
print("kajak")
s1 = input() #pobieramy slowo
print("kajak " + ("jest " if(is_it_Palindrom(s1)) else "nie jest ") + "palindromem ")