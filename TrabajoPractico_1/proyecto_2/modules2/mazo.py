from modules2.lista_doblemente import ListaDoblementeEnlazada

class DequeEmptyError(Exception):
    """Excepción lanzada cuando se intenta realizar una operación en un mazo vacío."""
    pass
class Mazo:
    def __init__(self):
        self._cartas = ListaDoblementeEnlazada()
    
    def poner_carta_arriba(self, carta):
        self._cartas.agregar_al_inicio(carta)
    
    def poner_carta_abajo(self, carta):
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar: bool = False):
        if self._cartas.esta_vacia():
            raise DequeEmptyError("no hay cartas para sacar: el mazo esta vacio")
        carta = self._cartas.extraer(0)
        if mostrar:
            carta.visible = True
        else:
            carta.visible = False
        return carta
    
    def sacar_carta_abajo(self, mostrar: bool = False):
        if self.esta_vacia():
            raise DequeEmptyError("no hay cartas para sacar: el mazo esta vacio")
        carta = self._cartas.extraer(-1)
        if mostrar:
            carta.visible = True
        else:
            carta.visible = False
        return carta
    
    def __len__(self):
        return len(self._cartas)
    
    def __str__(self):
        return str(self._cartas)
    
    def __iter__ (self):
        return iter(self._cartas)
