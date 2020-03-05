class User:
    
    nombre = "John Titor "
    genero = "Masculino "
    def nombre(self, namae) :
        print("Su nombre es " + namae)

    def genero(self, gene) :
        print("Su genero es " + gene)

    def cambiarNombre(self, gen) :
          self.genero=gen

objeto = User()
objeto.genero("furro")
objeto.nombre("John Titor")
