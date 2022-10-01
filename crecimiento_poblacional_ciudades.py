# Crecimiento poblacional :calcule e imprima en que año la población de la ciudad A es mayor que la de la ciudad B. 
print("________________________________________________")
print("|AÑO EN EL QUE LA CUIDAD A SUPERA A LA CUIDAD B |")
print("|_______________________________________________|")
print("")
print("la ciudad A tenia 3.5 millones de habitantes, y tasa de crecimiento de 7% anual en 1980.")
print("")
print("la ciudad B tenia 5 millones y una tasa de crecimiento de 5% anual en 1980.")
print("")
A = int(3500000)
A1 = A
B = int(5000000)
B1 = B
a = 1980

#process
while A1 <= B1: 
    A1 = A1 + A1 * 0.07
    B1 = B1 + B1 * 0.05
    a = a + 1 
else:
    print("En el año",a,",la cuidad A supera con",int(A1)," de habitantes a la cuidad B con",int(B1)," de habitantes")