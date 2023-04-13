# If simples.

"""
email_aluno = input(" Informe o email do aluno ")
nota_semestral = input(" Informe a nota do semestre do aluno ")

nota_semestral = float (nota_semestral)

if nota_semestral > 8.5:

    print( " Enviando email para {}" .format(email_aluno)) """

# Condição de else para notar que quando o valor é exatamente igual o valor proposto o programa corresponde como invalido.

""" else:

    print( " Nota não correponde ao necessario para enviar um email para o aluno ") """

# If composto.

"""valor_compra = input( " Informe o valor da compra realizada ")
cupom = input( " Digite o cupom de desconto ")

valor_compra = float(valor_compra)

if cupom.upper() == "NIVER10":

# *upper() serve para deixar as letras maiusculas independente de como digitar.

    valor_final = float(valor_compra) * 0.9

else:

    valor_final = float(valor_compra)

    print( " Cupom invalido ")

print( " O valor final da compra {}".format(valor_final))"""

#Programação de Bhaskaras com if - else.

#Valores na variavel já convertidos em float.

import math

A = float(input( " Informe o valor A " ))
B = float(input( " Informe o valor B " ))
C = float(input( " Informe o valor C " ))

#Equação delta:

delta = B * B - 4 * A * C

if delta > 0.0:

    x1 = ( -B + math.sqrt(delta)) / (2 * A)
    x2 = ( -B - math.sqrt(delta)) / (2 * A)

    print( "Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(A,B,C,x1,x2))

else:

    if delta == 0:

        x = (-B + math.sqrt(delta)) / (2 * A)

        print( " Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {} ".format(A, B, C, x))

    else:

        print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(A, B, C))