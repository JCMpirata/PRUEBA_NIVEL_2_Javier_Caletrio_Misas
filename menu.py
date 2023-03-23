import Figura
import Punto
import math


def menu():

    while True:

        print("1. Crear punto")
        print("2. Cuadrante de un punto")
        print("3. Vector entre dos puntos")
        print("4. Modulo de un vector")
        print("5. Distancia entre dos puntos")
        print("6. Punto mas lejano")
        print("7. Crear rectangulo")
        print("8. Base de un rectangulo")
        print("9. Altura de un rectangulo")
        print("10. Area de un rectangulo")
        print("11. Perimetro de un rectangulo")
        print("12. Diagonal de un rectangulo")
        print("13. Salir")

        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            x = int(input("Introduce la coordenada x: "))
            y = int(input("Introduce la coordenada y: "))
            punto = Punto.Punto(x, y)
            print(punto)

        elif opcion == 2:
            x = int(input("Introduce la coordenada x: "))
            y = int(input("Introduce la coordenada y: "))
            punto = Punto.Punto(x, y)
            print(punto.cuadrante())

        elif opcion == 3:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            print("Vector AB: ", punto1.vector(punto2))
            print("Vector BA: ", punto2.vector(punto1))

        elif opcion == 4:
            x = int(input("Introduce la coordenada x: "))
            y = int(input("Introduce la coordenada y: "))
            punto = Punto.Punto(x, y)
            print("Modulo de A: ", punto.modulo())

        elif opcion == 5:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            print("Distancia entre A y B: ", punto1.distancia(punto2))
            print("Distancia entre B y A: ", punto2.distancia(punto1))

        elif opcion == 6:
            lista = []
            for i in range(4):
                x = int(input("Introduce la coordenada x del punto {}: ".format(i+1)))
                y = int(input("Introduce la coordenada y del punto {}: ".format(i+1)))
                punto = Punto.Punto(x, y)
                lista.append(punto)
            print("Punto mas lejano: ", Punto.Punto.punto_mas_lejano(lista))

        elif opcion == 7:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            rectangulo = Figura.Rectangulo(punto1, punto2)
            print(rectangulo)

        elif opcion == 8:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            rectangulo = Figura.Rectangulo(punto1, punto2)
            print("Base: ", rectangulo.base())

        elif opcion == 9:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            rectangulo = Figura.Rectangulo(punto1, punto2)
            print("Altura: ", rectangulo.altura())

        elif opcion == 10:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            rectangulo = Figura.Rectangulo(punto1, punto2)
            print("Area: ", rectangulo.area())

        elif opcion == 11:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            rectangulo = Figura.Rectangulo(punto1, punto2)
            print("Perimetro: ", rectangulo.perimetro())

        elif opcion == 12:
            x1 = int(input("Introduce la coordenada x del primer punto: "))
            y1 = int(input("Introduce la coordenada y del primer punto: "))
            x2 = int(input("Introduce la coordenada x del segundo punto: "))
            y2 = int(input("Introduce la coordenada y del segundo punto: "))
            punto1 = Punto.Punto(x1, y1)
            punto2 = Punto.Punto(x2, y2)
            rectangulo = Figura.Rectangulo(punto1, punto2)
            print("Diagonal: ", rectangulo.diagonal())

        elif opcion == 13:
            print("Fin del programa")
            break
        







