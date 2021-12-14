#Obliczanie aktualnej wartości kredytu

print ("Podaj wartość początkową kredytu")

kredyt = int(input())

print("Podaj oprocentowanie kredytu")

oprocentowanie = input()

print ("Podaj kwotę raty")

rata = int(input())

#=(1 + ((B10+3(oprocentowanie)/1200)) * C9 - 200

message = ("Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.")
inflacja = 1.592824484
#suma = (1 + ((inflacja + oprocentowanie)//1200) * kredyt - rata

suma =  (1 + ((inflacja + float(oprocentowanie))/1200)) * kredyt - rata

lastmonth = kredyt - suma

print("Twoja pozostała kwota kredytu to " + str(suma))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiacu \n")

inflacja = -0.453509101

suma_luty =  (1 + ((inflacja + float(oprocentowanie))/1200)) * suma - rata

lastmonth = suma - suma_luty

print("Twoja pozostała kwota kredytu to " + str(suma_luty))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiacu")