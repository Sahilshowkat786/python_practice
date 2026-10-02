import time
print(time.time())
print(time.ctime())
time.sleep(1)
print(time.localtime())

current=time.localtime()
print(time.strftime("%d/%m/%y  %H:%M:%S",current))


start=time.perf_counter()
for i in range(100000000):
    pass
end =time.perf_counter()
print(f"execution time : {end-start} seconds")