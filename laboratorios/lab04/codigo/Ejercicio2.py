"""
    @clase Ejercicio 2
    Descripcion: Ejercicio2 lab 4
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""
def min(n, d, r, mañana, tarde):
    total_mañana   = total(mañana)
    total_tarde = total(tarde)
    limite = n*d
    hours = total_mañana + total_tarde
    return (hours - limite) * r
    
def total(horario):
    total = 0
    for i in horario:
        total += i
    return total

def convert_input(line):
    for i in range(len(line)):
        line[i] = int(line[i])
        
line = input()

while(line != '0 0 0'):
    line = line.split(' ')
    convert_input(line)
    
    if line[0] < 1 or line[1] < 1 or line[2] < 1 or line[0] > 100 or line[1] > 10000 or line[2] > 5:
        print('invalid input')
        break
    
    morning   = input().split(' ')
    afternoon = input().split(' ')
    convert_input(morning)
    convert_input(afternoon)
    
    print(min(line[0], line[1], line[2], morning, afternoon))
    line = input()
    