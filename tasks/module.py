# module.py

a =10
def get_a():
    global _a
    print('get a')
    return _a

def set_a(value):
    global _a
    print('set value')
    if value < 0:
        raise ValueError('must be positive')
    _a = value