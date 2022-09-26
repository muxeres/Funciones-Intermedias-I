#1-Actualiza valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#1.1-Cambio
print('********** 1.1-Cambio **********')
x[1][0]=15
print(x)

#1.2-Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print('********** 1.2-Cambia el "apellido” del primer alumno de Jordan'  'Bryant' **********')
estudiantes[0]["last_name"]="Bryant"
print(estudiantes)

#1.3-En el directorio_deportes, cambia "Messi" por "Andrés".
print('********** 1.3-En el directorio_deportes, cambia "Messi" por "Andrés". **********')
directorio_deportes['football'][0]='Andres'
print(directorio_deportes)

#1.4-Cambia el valor 20 en z a 30.
print('********** 1.4-Cambia el valor 20 en z a 30. **********')
z[0]['y']=30
print(z)

#2-2. Itera a través de una lista de diccionarios
print('********** 2. Itera a través de una lista de diccionarios **********')
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ]

def iterateDictionary(some_list):
     newstring = ''
     for i in some_list:
          newstring +='first_name - %s, last_name %s \n' %(i['first_name'],i['last_name'])
     return newstring

result = iterateDictionary(estudiantes)
print(result)

#3-Obtén valores de una lista de diccionarios
print('********** 3 -Obtén valores de una lista de diccionarios **********')
def iterateDictionary2(key_name, some_list):
     newstring=''     
     for i in some_list:
          newstring += '%s \n'%(i[key_name])
     return newstring
result1 = iterateDictionary2('first_name', estudiantes)
print(result1)
result2 =iterateDictionary2('last_name', estudiantes)
print(result2)

#4. Itera a través de un diccionario con valores de lista
print('********** 4. Itera a través de un diccionario con valores de lista **********')
dojo = {
'locations' : [ 'San Jose' , 'Seattle' , 'Dallas' , 'Chicago' , 'Tulsa' , 'DC' , 'Burbank' ],
'instructors' : [ 'Michael' , 'Amy' , 'Edward' , 'Josh' , 'Graham' , 'Patrick' , 'Minh' , 'Devon' ]
}
def printInfo(dojo):
     newstring=''
     for i in dojo: 
          newstring += f'\n{len(dojo[i])} {i.upper()} \n'
          for i in dojo[i]:
               newstring +=f'{i} \n'
     return newstring

print(printInfo(dojo))
  salida: 
 7 LOCATIONS
 Saint Joseph
 Seattle
 Dallas
 Chicago
 Tulsa
 DC
 Burbank

 8 INSTRUCTORS
 Michael
 Amy
 Eduardo
 Josh
 Graham
 Patrick
 bright
 Devon
