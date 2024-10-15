class OperacionesAritmeticas:

    def suma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def division(self,dividendo, divisor):
        try:
            return dividendo / divisor
        except ZeroDivisionError:
            print("El divisor debe ser mayor que cero")
            raise ZeroDivisionError
        except TypeError:
            print("Los parametros deben ser numericos")
            raise TypeError

    def division(self,dividendo, divisor):
        if divisor == 0:
            raise ZeroDivisionError
        elif not (isinstance(dividendo, (float, int)) and isinstance(divisor, (float, int))):
            raise TypeError
        else:
            return dividendo / divisor
        #try:
            #return dividendo / divisor
        #except ZeroDivisionError:
            #print("El divisor debe ser mayor que cero")
            #raise ZeroDivisionError
        #except TypeError:
            #print("Los parametros deben ser numericos")
            #raise TypeError
