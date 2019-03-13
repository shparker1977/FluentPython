class DemoException(Exception):
    """An exception type for the demo."""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except(DemoException):
            print('*** DemoException handled.  Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    
        finally:
            print('-> coroutine ending')