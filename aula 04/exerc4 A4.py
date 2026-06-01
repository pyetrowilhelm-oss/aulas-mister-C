#exercicio 4
class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Erro: temperatura fora do limite do sensor")

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

sensor1 = Sensor(25)
print(sensor1.get_temperatura(), sensor1.status())

sensor1.set_temperatura(95)
print(sensor1.get_temperatura(), sensor1.status())

sensor1.set_temperatura(130)
print(sensor1.get_temperatura(), sensor1.status())

sensor1.set_temperatura(200)
