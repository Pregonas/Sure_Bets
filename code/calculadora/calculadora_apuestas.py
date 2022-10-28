"""
Tenis o deportes 50%:
"""


def calculadora_tenis(A, B):
    if B > (A / (A - 1)):
        x = 50
        y_min = (x / (B - 1))
        y_max = ((A * x) - x)


        print("La cantidad mínima a apostar por el jugador B es: " + str(y_min))
        print("La cantidad máxima a apostar por el jugador B es: " + str(y_max))
        y = (y_max + y_min) / 2
        #while (1):
            #y = float(input("Introducir la cantidad a apostar por el jugador B: "))

            #if y > y_min and y < y_max or y == 0:
             #   break
            #else:
                #print("Introducir una cantidad válida entre máximo y mínimo.")

        Ganancia_x = str(A * x - (x + y))
        Ganancia_y = str(B * y - (x + y))

        print("En caso de victoria del jugador A, la ganancia será: " + str(Ganancia_x) + " €")
        print("En caso de victoria del jugador B, la ganancia será: " + str(Ganancia_y) + " €")
        rentable = True

        return rentable, x, y, Ganancia_x, Ganancia_y, y_max, y_min

    else:
        rentable = False

        return rentable, False, False, False, False, False, False

"""
Fútbol o deportes que permiten el empate:
"""
import math

"""
def calculadora_futbol():
    A = float(input("Introducir tasa más alta por victoria de un equipo: "))
    B = float(input("Introducir tasa por empate: "))
    C = float(input("Introducir tasa por victoria del otro equipo: "))

    if (A > 2.61803 and B > (A / (A - 1)) and C > ((A * B) / (A * B - A - B))):
        print("\n")
        print("La jugada es rentable.")

        x = float(input("introducir la cantidad a apostar por el equipo con menor tasa: "))

        y_min = ((A * x) / (A * B - A - B))
        y_max = ((C * x) / B)
        print("La cantidad mínima a apostar por empate es: " + str(y_min))
        print("La cantidad máxima a apostar por empate es: " + str(y_max))

        while (1):
            y = float(input("Introducir la cantidad a apostar por empate: "))
            if y > y_min and y < y_max:
                break
            else:
                print("Introducir una cantidad válida entre máximo y mínimo.")

        z_min = ((x + y) / (A - 1))
        z_max = ((B * y) - x - y)

        print("La cantidad mínima a apostar por el equipo con mayor tasa es: " + str(z_min))
        print("La cantidad máxima a apostar por el equipo con mayor tasa es: " + str(z_max))

        while (1):
            z = float(input("Introducir la cantidad a apostar por el equipo con mayor tasa: "))
            if z > z_min and z < z_max:
                break
            else:
                print("Introducir una cantidad válida entre máximo y mínimo.")

        Ganancia_x = (C * x - (x + y + z))
        Ganancia_y = (B * y - (x + y + z))
        Ganancia_z = (A * z - (x + y + z))

        print("En caso de victoria del equipo con mayor tasa, la ganancia será: " + str(Ganancia_x) + " €")
        print("En caso de empate, la ganancia será: " + str(Ganancia_y) + " €")
        print("En caso de victoria del equipo con menor tasa, la ganancia será: " + str(Ganancia_z) + " €")
        

    else:
        print("La jugada no es rentable.")

"""