#Obliczanie aktualnej wartości kredytu
#message = ("Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.")
#=(1 + ((B10+3(oprocentowanie)/1200)) * C9 - 200

print ("Podaj wartość początkową kredytu")

kredyt = float(input())

print("Podaj oprocentowanie kredytu")

oprocentowanie = float(input())

print("Podaj kwotę raty")

rata = float(input())

inflacja = 1.592824484
#suma = (1 + ((inflacja + oprocentowanie)//1200) * kredyt - rata

suma =  (1 + ((inflacja + (oprocentowanie))/1200)) * kredyt - rata

lastmonth = kredyt - suma

print("Twoja pozostała kwota kredytu to ", str(suma),"to ", str(lastmonth), "mniej niż w poprzednim miesiacu \n")

inflacja = -0.453509101

suma_luty =  (1 + ((inflacja + float(oprocentowanie))/1200)) * suma - rata

lastmonth = suma - suma_luty

print("Twoja pozostała kwota kredytu to " + str(suma_luty))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiacu \n")

inflacja = 2.324671717

suma_marzec = (1 + ((inflacja + float(oprocentowanie))/1200)) * suma_luty - rata

lastmonth = suma_luty - suma_marzec

print("twoja pozostała kwota kredytu to " + str(suma_marzec))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiącu \n")

inflacja = 1.261254407

suma_kwiecien = (1 + ((inflacja + float(oprocentowanie))/1200)) * suma_marzec - rata

lastmonth = suma_marzec - suma_kwiecien

print("twoja pozostała kwota kredytu to " + str(suma_kwiecien))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiącu \n")

inflacja = 1.782526286

suma_maj = (1 + ((inflacja + float(oprocentowanie))/1200)) * suma_kwiecien - rata

lastmonth = suma_kwiecien - suma_maj

print("twoja pozostała kwota kredytu to " + str(suma_maj))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiącu \n")

inflacja = 2.329384541

suma_czerwiec = (1 + ((inflacja + float(oprocentowanie))/1200)) * suma_maj - rata

lastmonth = suma_maj - suma_czerwiec

print("twoja pozostała kwota kredytu to " + str(suma_czerwiec))
print("to " + str(lastmonth))
print("mniej niż w poprzednim miesiącu \n")

