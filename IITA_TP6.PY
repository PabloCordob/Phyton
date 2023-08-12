#1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
#del rectángulo.

class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        self.area = self.base*self.altura
    
    def pedir(self):
        print("El area del rectangulo es:",self.area)
rectan=rectangulo(2,2)
rectan.pedir()

#2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
#como miembros:
#o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
#o Un atributo para el estado (lleno o vacío).
#o Un atributo n, que indica la cantidad máxima de cebadas.
#o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
#excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
#o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
#debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
#o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
#de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
#Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

class mate:
    def __init__(self,cebada,estado,n):
        self.cebada = cebada
        self.estado = estado
        self.n = n
        self.num=0
    def cebar(self):
      if self.num < self.n:
        self.n += 1
        if self.estado == "lleno":
            print("¡Cuidado! ¡Te quemaste!")
        elif self.estado == "vacio":
            self.estado = "lleno"
            print("El mate esta lleno")
            if self.cebada == 0:
                print("el mate esta lavado.")
                self.cebada=0
            else:
                self.cebada-=1
      elif self.num == self.n:
          print("cantidad maxima de veces para cebar alcanzada")

    def beber(self):
        if self.cebada > 0:
            if self.estado == "lleno":
                self.estado == "vacio"
                print("Haz bebido el mate")
            elif self.estado == "vacio":
                print("¡El mate está vacío!")
        if self.cebada == 0:
            print("Advertencia: el mate está lavado.")
        
termo = mate(0,"vacio",1)
termo.cebar()
termo.beber()

#3) Botella y Sacacorchos
# Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
# Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
#destapada.
# Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
#una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
#sacacorchos ya contiene un corcho.
# Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
#un corcho
class corcho:
    def __init__(self,bodega):
        self.bodega = bodega
    
    def __str__(self):
        return self.bodega
class botella:
    def __init__(self,corcho:corcho):
        self.corchodebotella = corcho
    def guardarcorcho(self):
        guardado = self.corchodebotella
        self.corchodebotella = None
        return guardado
class sacacorchos:
    def __init__(self):
        self.sacacorcho = None

    def destapar(self,botella:botella):
        if self.sacacorcho == None:
            if botella.corchodebotella != None:
                self.sacacorcho = botella.guardarcorcho()
                print("se destapo la botella")
            else:
                print("La botella esta destapada")
        else:
            print("El sacacorcho tiene un corcho, se tiene que limpiar")
    def limpiar(self):
        if self.sacacorcho==None:
            print("El sacacorcho esta limpio")
        else:
            self.sacacorchos=None
            print("Se limpio el sacacorcho")
# Crear una instancia de la clase 'corcho'
mi_corcho = corcho("Corcho de prueba")

# Crear una instancia de la clase 'botella' y pasarle la instancia de 'corcho' creada anteriormente
mi_botella = botella(mi_corcho)

# Crear una instancia de la clase 'sacacorchos'
mi_sacacorchos = sacacorchos()

# Llamar al método 'destapar' en la instancia de 'sacacorchos' pasándole la instancia de 'botella'
mi_sacacorchos.destapar(mi_botella)

# Llamar al método 'limpiar' en la instancia de 'sacacorchos'
mi_sacacorchos.limpiar()

class Corcho:
    def __init__(self, Bodega):
        self.Bodega=Bodega
    
    def __str__(self):
        return self.Bodega

class Botella:
    def __init__(self, Corcho:Corcho):
        self.CorchoDeBotella=Corcho
    
    def PerderCorcho(self):
        temporal=self.CorchoDeBotella
        self.CorchoDeBotella=None
        return temporal

class Sacacorcho:
    def __init__(self):
        self.CorchoSacacorcho=None
    
    def Destapar(self,Botella:Botella):
        if self.CorchoSacacorcho==None:
            if Botella.CorchoDeBotella!=None:
                self.CorchoSacacorcho=Botella.PerderCorcho()
                print("Botella destapada")
            else:
                print("La botella ya esta destapada")
        else:
             print("El sacacorchos ya tiene un corcho, primero hay que limpiarlo")

    def Limpiar(self):
        if self.CorchoSacacorcho==None:
            print("El sacacorchos ya esta limpio")
        else:
            self.CorchoSacacorcho=None
            print("Sacacorcho limpiado")
