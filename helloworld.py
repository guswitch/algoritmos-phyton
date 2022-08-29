# Isso é um comentario 

lista = [10,20,30];
divisores = [];
print('Divisores comuns entre: ');
print(lista);
maiornumero = max(lista);
menornumero = min(lista);
for i in range (1,maiornumero):
    for item in lista:
        if(item%i == 0):
            divisores.append(i);
print(divisores);


"""
for i in range(1,10):
    if(i%2 == 0):
        print(str(i));
"""