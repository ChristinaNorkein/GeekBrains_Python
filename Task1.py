import time
import itertools

class TrafficLight:
    __color = [["красный", 7], ["желтый", 2], ["зеленый", 5]]

    def running(self):
        for el in itertools.cycle(self.__color):
            print(f'\r\033[1m{el[0]}', end='')
            time.sleep(el[1])


signal = TrafficLight()
signal.running()
