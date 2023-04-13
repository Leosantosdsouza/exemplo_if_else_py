#Condição if com else normal

pontuacao = input(" Coloque a pontuação do cliente ")
pontuacao = int(pontuacao)

"""

if pontuacao >= 1000:

    print(" O cliente receberá um bonus de 3gb de internet ")

else:

    if pontuacao >= 500:

        print(" O cliente receberá um bonus de 2 gb de internet ")

    else:

        if pontuacao >= 200:

            print(" O cliente recebera um bonus de 500mb de internet")


        else:

            print( " O cliente não tem direito a bonus ") """

#Condição Elif

#Condição que simplifica a condição de if e else.

if pontuacao >= 1000:

    print(" O cliente receberá um bonus de 3gb de internet ")

elif pontuacao >= 500:

    print(" O cliente receberá um bonus de 2 gb de internet ")

elif pontuacao >= 200:

    print(" O cliente recebera um bonus de 500mb de internet")

else:

    print(" O cliente não tem direito a bonus ")

