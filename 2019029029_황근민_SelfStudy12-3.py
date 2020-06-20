# Self Study 12-3
import threading
import time


class Sum:
    value = 0
    sum_number = 0

    def __init__(self, value1, value2):
        self.value = value1
        self.total = value2

    def sum_number(self):
        for i in range(0, self.value+1, 1):
            self.total += i
        print("1+2+3+. . . + %d = %d" % (self.value, self.total))
        time.sleep(0.1)


Sum1000 = Sum(1000, 0)
Sum100000 = Sum(100000, 0)
Sum10000000 = Sum(10000000, 0)

th1 = threading.Thread(target=Sum1000.sum_number)
th2 = threading.Thread(target=Sum100000.sum_number)
th3 = threading.Thread(target=Sum10000000.sum_number)

th1.start()
th2.start()
th3.start()

