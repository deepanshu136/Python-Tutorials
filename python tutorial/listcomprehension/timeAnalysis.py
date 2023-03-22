import time

def for_loop(n):
    result=[]
    for i in range(n):
        result.append(i**2)

def list_compression(n):
    return [i**2 for i in range(n)]

begin = time.time()
for_loop(10**6)
end=time.time()
print("time taken by for loop:",round(end-begin,2))

begin = time.time()
list_compression(10**6)
end=time.time()
print('Time taken for list_comprehension:', round(end-begin, 2))

