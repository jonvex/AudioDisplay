import clock
import time



c = clock.clock()
for i in range(5):
    for j in range(10):
        c.write_num(j,3 * i)
        time.sleep(3)
