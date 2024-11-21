from Parchis import *

def main():
    nomJ1 = input("Ingrese el nombre del jugador 1: ")
    nomJ2 = input("Ingrese el nombre del jugador 2: ")
    juego = Parchis(nomJ1, nomJ2)
    turno = 1
    
    while (juego.esGanador()!=juego.nomJ1 and  juego.esGanador()!=juego.nomJ2) :
        input("Presione Enter para continuar...")
        print(f"Turno del jugador {turno}: {juego.nomJ1 if turno == 1 else juego.nomJ2}")
        suma_dados = juego.tirarDados()
        print(juego.estadoCarrera())
        print(f"Dados: {Parchis.dado1} y {Parchis.dado2} (Suma: {suma_dados})")
        if (turno==1):
            juego.avanzaPosiciones(juego.nomJ1)
        else:
            juego.avanzaPosiciones(juego.nomJ2)
        print(juego.pintaTablero())
        if Parchis.dado1 != Parchis.dado2:
            turno = 2 if turno == 1 else 1
    print( "Ha ganao " +juego.esGanador())

if __name__ == "__main__":
    main()
