#Obliczanie aktualnej wartości kredytu
#message = ("Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.")
#=(1 + ((B10+3(oprocentowanie)/1200)) * C9 - 200

print ("Podaj wartość początkową kredytu")
kredyt = float(input())

print("Podaj oprocentowanie kredytu")
oprocentowanie = input()

print("Podaj kwotę raty")
rata = float(input())
inflacja = 1.592824484
#suma = (1 + ((inflacja + oprocentowanie)//1200) * kredyt - rata

suma =  round((1 + ((inflacja + float(oprocentowanie))/1200)) * kredyt - rata, 2)
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

inflacja = 1.502229842
suma_lipiec = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_czerwiec - rata, 2)
lastmonth = round(suma_czerwiec - suma_lipiec, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_lipiec, lastmonth))

inflacja = 1.782526286
suma_sierpien = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_lipiec - rata, 2)
lastmonth = round(suma_lipiec - suma_sierpien, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_sierpien, lastmonth))

inflacja = 2.328848994
suma_wrzesien = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_sierpien - rata, 2)
lastmonth = round(suma_sierpien - suma_wrzesien, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_wrzesien, lastmonth))

inflacja = 0.616921348
suma_pazdziernik = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_wrzesien - rata, 2)
lastmonth = round(suma_wrzesien - suma_pazdziernik, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_pazdziernik, lastmonth))

inflacja = 2.352295886
suma_listopad = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_pazdziernik - rata, 2)
lastmonth = round(suma_pazdziernik - suma_listopad, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_listopad, lastmonth))

inflacja = 0.337779545
suma_gru = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_listopad - rata, 2)
lastmonth = round(suma_listopad - suma_gru, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_gru, lastmonth))

print("------Nowy rok------ \n")

inflacja = 1.577035247
suma_sty =  round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_gru - rata, 2)
lastmonth = round(suma_gru - suma_sty, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_sty, lastmonth))

inflacja = -0.292781443
suma_luty =  round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_sty - rata, 2)
lastmonth = round(suma_sty - suma_luty, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_luty, lastmonth))

inflacja = 2.48619659
suma_marzec = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_luty - rata, 2)
lastmonth = round(suma_luty - suma_marzec, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_marzec, lastmonth))

inflacja = 0.267110318
suma_kwiecien = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_marzec - rata, 2)
lastmonth = round(suma_marzec - suma_kwiecien, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_kwiecien, lastmonth))

inflacja = 1.417952672
suma_maj = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_kwiecien - rata, 2)
lastmonth = round(suma_kwiecien - suma_maj, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_maj, lastmonth))

inflacja = 1.054243267
suma_czerwiec = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_maj - rata, 2)
lastmonth = round(suma_maj - suma_czerwiec, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_czerwiec, lastmonth))

inflacja = 1.480520104
suma_lipiec = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_czerwiec - rata, 2)
lastmonth = round(suma_czerwiec - suma_lipiec, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_lipiec, lastmonth))

inflacja = 1.577035247
suma_sierpien = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_lipiec - rata, 2)
lastmonth = round(suma_lipiec - suma_sierpien, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_sierpien, lastmonth))

inflacja = -0.07742069
suma_wrzesien = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_sierpien - rata, 2)
lastmonth = round(suma_sierpien - suma_wrzesien, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_wrzesien, lastmonth))

inflacja = 1.165733399
suma_pazdziernik = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_wrzesien - rata, 2)
lastmonth = round(suma_wrzesien - suma_pazdziernik, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_pazdziernik, lastmonth))

inflacja = -0.404186718
suma_listopad = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_pazdziernik - rata, 2)
lastmonth = round(suma_pazdziernik - suma_listopad, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_listopad, lastmonth))

inflacja = 1.499708521
suma_gru = round((1 + ((inflacja + float(oprocentowanie))/1200)) * suma_listopad - rata, 2)
lastmonth = round(suma_listopad - suma_gru, 2)
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiąciu. \n".format(suma_gru, lastmonth))
