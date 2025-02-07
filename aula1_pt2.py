print("Bem vindo à Lanchonete Vai No Lanche")

salgado = input("Informe o seu salgado:")

bebida = input("O que irá beber:")

# Formatted String (Python) = Template String (JavaScript)
print(f'O seu pedido foi {salgado} acompanhado de uma: {bebida}')

valor_salgado = int(input("O valor do salgado é:"))

valor_bebida = int(input("O valor da bebida é:"))

print(f'O total que irá pagar é R$:{valor_bebida + valor_salgado},00')

# Condicionais -> São as responsáveis pelo controle de fluxo da nossa aplicação, a partir delas podemos executar ou não uma ou várias ações baseadas na resposta do usuário.

#Condicional Simples

saldo = False
if saldo == False:
    print('Tá Lascado!')


# Condicional Composta

    idade = 26

    if idade >= 18:
        print('Você se quiser, pode mandar um pix para os seus instrutores!')
    else:
        print('Você ainda não pode mandar um pix para aos seus instrutores.')

# Condicional Aninhada

if idade >= 18 and saldo == True:
    print('Você pode mandar um pix aos seus instrutores.')
elif idade >= 18 and saldo == False:
    print('Você não pode mandar um pix aos seus instrutores ;(')
else:
    print('A sua presença em sala de aula, é o melhor presente <3 ')


# JavaScript --> &, ||, !
# Python --> and, or, not

# and (e) --> retorna um resultado verdadeiro, caso as duas perguntas sejam verdadeiras
# Eu quero sorvete e batata frita --> True/False

# or (ou) --> retorna um resultado verdadeiro, caso uma das duas perguntas seja verdadeira
# Eu quero sorvete ou batata frita --> True/False

# not (negação) --> inverte qualquer resultado, caso seja True retorna False, caso seja False retorna True

# Operadores de Comparação

# > -- Verifica se um valor é maior que outro
# < -- Verifica se um valor é menor que outro
# >= -- Verifica se um valor é maior ou igual a outro
# <= -- Verifica se um valor é menor ou igual a outro
# != -- Verifica se um valor é diferente de outro
# == -- Verifica se um valor é igual ao outro