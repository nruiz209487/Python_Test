import random

class Ahorcado:
   #Variableses taticas
    Palabras =  ["humanidad","persona","hombre","mujer","individuo","cuerpo","pierna","cabeza","brazo","familia"]
    NUMINTENTOS = 7
   #Variableses no taticas
    def __init__(self):
        self.palabraSecreta = ""
        self.palabraPista = ""
        self.noAcertadas =[""]

   
    def  generaPalabra(self):
        numero = random.randint(0, len(Ahorcado.Palabras)-1)
        self.palabraSecreta = Ahorcado.Palabras[numero]

        
    def  compruebaLetra(self,letra):
        letra=letra.lower()

        if (letra not in  self.palabraSecreta):
            self.noAcertadas.append(letra)



    def  compruebaPalabra(self,palabraIntento):
        palabraIntento=palabraIntento.lower()
        if(palabraIntento in Ahorcado.Palabras):
             self.palabraPista=palabraIntento

        