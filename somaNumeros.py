quantidade = 0
soma = 0
numero = str(input( 'Numero = '))
while numero.isnumeric(): 
  soma += float(numero)
  quantidade += 1
  print('\33[32mSoma = {}\33[m'.format(soma))
  numero = str(input( 'numero = '))
  
print('\nvoce somou {} numeros , resultando em: {}'.format(quantidade, soma))


