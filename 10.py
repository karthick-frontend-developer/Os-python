from multiprocessing import Process,Value,Array
def f(n,a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
if __name__ == '__main__':
    num = Value('d',0.0)
    arr = Array('i',range(10))
    arr1 = Array('i',range(1,20,2))
    print("\t\tIPC using Shared Memory")
    p1 = Process(target=f,args=(num,arr))
    p1.start()
    p1.join()
    p2=Process(target=f,args=(num,arr))
    p2.start()
    p2.join()
    print(num.value)
    print(arr[:])
    print(arr1[:])
