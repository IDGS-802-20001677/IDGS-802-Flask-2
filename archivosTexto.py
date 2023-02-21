'''f = open('alumnos.txt', 'r/w')
#nombres = f.read()
#print(nombres)

nombres2=f.readlines()
print(nombres2)
f.close
#f.seek(0)

for items in nombres2:
    print(items, end='')
    '''

alumno={'Matrícula':12345, 
        'Nombre':'Mario',
        'Apellidos':'Lopez',
        'correo':'ivanhk815@gmail.com'}

f=open('alumnos.txt', 'a')
for item in alumno:
    f.write(item)
f.write('\n' + 'Mario')
f.write('\n' + 'Pedro')
f.write('\n' + alumno)
f.close()