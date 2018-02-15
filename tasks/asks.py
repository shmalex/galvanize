
def ask_yes_no(msg="y/n", repeat_value='Could you please reapeat?'):
    repeat = ''
    while True:
        x = input(repeat + msg + ':').lower()
        if x == 'y':
            return True
        elif x == 'n':
            return False
        repeat = repeat_value


def ask_number(msg="Enter numebr"):
    while True:
        x = input(msg + ':').strip()
        try:
            x = int(x)
            return x
        except ValueError as err:
            print("Please try again because we " + str(err))


def ask_one_othe(options, pre_msg=' Choose one of the :'):
    ask = ', '.join(options) + ':'
    while True:
        inp = input(pre_msg + ask).strip()
        if inp in options:
            return inp
