salario=float(input("Informe seu salário mensal: "))
comissao=int(input("Qual a comissão recebida por cada venda?"))
valor_totalVendas=float(input("Qual a quantidade de vendas realizadas esse mês?"))
salariofinal=salario+((comissao/100)*valor_totalVendas)

print("O salário final é ", salariofinal)