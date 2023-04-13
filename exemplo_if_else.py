#variaveis + inicio

#Aqui o individuo vai adicionar sua idade nas variaveis, input para adicionar um valor na variavel.

rm = input(" Insira sua RM ")
idade = input(" Insira sua idade ")
autorizado = input(" Escreve se tem autorização, apenas Sim ou Não ")

#condição if simples

#Apenas uma condição de If.

""" if <condição>:
    <ação a ser realizada se a condição for verdadeira> """

if int(idade) >= 18:

#Mostrar na tela se a condição se for verdadeira.

    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")

#Condição composta (Else).

#Mostrar na tela se a condição for falsa.

else:

# Condição Encadeado

# Aplica mais uma condição de if e else no problema, pois acrecentou mais uma condição dentro da variavel.

    if autorizado == 'S':

        print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
        print("Mais informações serão enviadas para o email dos responsaveis")

    else:

        print("Sua participação não foi autorizada por causa da sua idade")

#Sempre lembrar dos espaçamentos, pois o mesmo define a condição de cada if e else