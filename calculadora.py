class Calculadora:

    def __init__(self):
        self.numero1, self.numero2 = 0.0, 0.0
    
    def restar(self, numero1=0.0, numero2=0.0):
        if not isinstance(numero1, (int, float, complex, bool)):
            numero1 = 0.0
        if not isinstance(numero2, (int, float, complex, bool)):
            numero2 = 0.0
        return numero1 - numero2
