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

suma =  round((1 + ((inflacja + (oprocentowanie))/1200)) * kredyt - rata, 2)

lastmonth = round(kredyt - suma, 2)

#print("Twoja pozostała kwota kredytu to ", str(suma),"to ", str(lastmonth), "mniej niż w poprzednim miesiacu")
print(f"Twoja pozostała kwota kredytu to {suma}, to {lastmonth} mniej niż w poprzednim miesiącu. \n")

inflacja = -0.453509101
suma_luty =  round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma - rata, 2)
lastmonth = round(suma - suma_luty, 2)
#print("Twoja pozostała kwota kredytu to ", str(suma_luty),"to ", str(lastmonth), "mniej niż w poprzednim miesiacu \n")
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_luty, lastmonth))

inflacja = 2.324671717
suma_marzec = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_luty - rata, 2)
lastmonth = round(suma_luty - suma_marzec, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_marzec, lastmonth))

inflacja = 1.261254407
suma_kwiecien = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_marzec - rata, 2)
lastmonth = round(suma_marzec - suma_kwiecien, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_kwiecien, lastmonth))

inflacja = 1.782526286
suma_maj = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_kwiecien - rata, 2)
lastmonth = round(suma_kwiecien - suma_maj, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_maj, lastmonth))

inflacja = 2.329384541
suma_czerwiec = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_maj - rata, 2)
lastmonth = round(suma_maj - suma_czerwiec, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_czerwiec, lastmonth))
