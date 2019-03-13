from coroutil import coroutine

def simple_coroutine(a):
    print('-> coroutine started: a = ', a)
    b = yield a
    print('-> coroutine received: b = ', b)
    c = yield a+b
    print('-> Received: c = ', c)

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count