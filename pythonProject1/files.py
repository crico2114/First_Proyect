#1

file = open('file1.txt')
print(file.read())
file.close()

file = open('file1.txt')
print(file.readline())
print(file.readline())
file.close()

file = open('file1.txt')
print(file.readlines())
file.close()

#2
file = open('file2a.txt', 'a')
file.write('hola')
file.close()

file = open('file2a.txt', 'a')
file.write('hi')
file.close()

#3
file = open('file1.txt', 'rb')
print(file.read())
file.close()

#4

file = open('file2.txt', 'w')
file.write('hola')
file.close()

file = None
try:
    file = open('file2.txt', 'r')
    print(file.read())
except Exception as ex:
    print(ex.args)
finally:
    if file is not None:
        file.close()
#5
file = None
a = 1
b = 0
try:
    file = open('file2.txt', 'r')
    print(file.read())
    num = a / b
except FileNotFoundError as ex:
    print(ex.filename, ex.args)
    #raise FileNotFoundError(ex.filename)
except ZeroDivisionError as ex:
    print(ex.args)
except Exception as ex:
    print(ex.args)
finally:
    if file is not None:
        file.close()
#6
def open_file(filep):
    file = None
    a = 1
    b = 1
    try:
        file = open(filep, 'r')
        print(file.read())
        num = a / b
    except FileNotFoundError as ex:
        print(ex.filename, ex.args)
        raise FileNotFoundError(ex.filename, ' en la mala')
    except ZeroDivisionError as ex:
        print(ex.args)
    except Exception as ex:
        print(ex.args)
    finally:
        if file is not None:
            file.close()

#7
try:
    open_file('file3.txt')
except FileNotFoundError as ex:
    print(ex.args)

class MyEmptyFileError(Exception):
    def __init__(self, message):
        self.message = message


def open_file_empty(filename):
    file = None
    try:
        file = open(filename, 'r')
        data = file.read()
        print(data)
        if data == '':
            raise MyEmptyFileError('the file is empty!')
    except FileNotFoundError as ex:
        print(ex.args)
    finally:
        if file is not None:
            file.close()

try:
    open_file_empty('file4.txt')
except MyEmptyFileError as ex:
    print(ex.message)

print('all is fine!')

#8
with open('init2.txt', 'a') as file:
    file.write('Hola!\n')
    print(file.read())