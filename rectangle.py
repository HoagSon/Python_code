from decimal import Decimal
def compute_area(length, width):
    return length*width

def compute_perimeter(length, width):
    return (length+width)*2

def menu():
    length = float(input('Enter the length:   '))
    width = float(input('Enter the width:    '))
    print ('============================')
    print ('Area =              {}'.format(compute_area(length, width)))
    print ('Perimeter =         {}'.format(compute_perimeter(length, width)))
    print ('============================')
    print ('Thanks for using this program!')
    return 0

if __name__ ==  '__main__':
    menu()
