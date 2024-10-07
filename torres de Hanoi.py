class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None
    
    def __str__(self):
        return str(self.items)


def mover_disco(origen, destino, nombre_origen, nombre_destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")


def torres_de_hanoi(n, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar):
    if n == 1:
        mover_disco(origen, destino, nombre_origen, nombre_destino)
    else:
        torres_de_hanoi(n-1, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino)
        mover_disco(origen, destino, nombre_origen, nombre_destino)
        torres_de_hanoi(n-1, auxiliar, destino, origen, nombre_auxiliar, nombre_destino, nombre_origen)

num_discos = int(input("Ingrese el número de discos: "))


origen = Pila()
auxiliar = Pila()
destino = Pila()


for disco in range(num_discos, 0, -1):
    origen.apilar(disco)

print(f"\nResolución del juego de las Torres de Hanoi para {num_discos} discos:")
torres_de_hanoi(num_discos, origen, destino, auxiliar, 'Origen', 'Destino', 'Auxiliar')
