class Casa():

    def __init__(self, color, numero):
        self.color = color
        self.numero = numero

    def __str__(self):
        return "Color {}, {} número".format( self.color, self.numero )

class Hogar(Casa):

    def __init__(self, color, numero, superficie, precio):
        self.color = color
        self.numero = numero
        self.superficie = superficie
        self.precio = precio

    def __str__(self):
        return "color {}, {} m2,numero {} , {} €".format( self.color, self.superficie, self.numero, self.precio )


hogar = Hogar("azul", 150, 400, 120000)
print(hogar)
