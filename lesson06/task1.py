import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        light_time = [7, 3, 5]
        idx = 0
        while idx < 3:
            for i in reversed(range(1, light_time[idx] + 1)):
                print(f'{TrafficLight.__color[idx]} свет : {i} сек')
                time.sleep(1)
            idx += 1


traffic_test = TrafficLight()
traffic_test.running()
