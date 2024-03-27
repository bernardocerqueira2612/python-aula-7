def soma (a, b):
    return a + b

def quadrado (a):
    return a**2

def hipotenusa (cateto1, cateto2):
    return soma(quadrado(cateto1), quadrado(cateto2))**(1/2)

def simples(nome):
            if nome == 'bernardo':
                return 'Acertou meu nome'

def medio(nome):
    if nome == 'bernardo':
        return 'ACERTOU meu nome'
    else :
        return 'voce nao conhece meu nome'


def completo(nome):
    if nome == 'bernardo':
        return 'Acertou meu nome'
    elif nome == 'sei la':
        return 'errou'
    else:
        return 'Voce nao sabe meu nome'


numeros = [1,2,3,4,5]

contador = 0
while contador < 10:
    print(contador)
    contador += 1

for i in range(10):
    print(i)

for item in [1,45,78,'a',[3,5]]:
    print(item)

for letra in 'minha string':
    print(letra)


      Piramide com n = 4

for i in range(4):
    print((i + 1) * "*")
    
            
