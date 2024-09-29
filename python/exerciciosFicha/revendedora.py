#revendedora_de_carros
num_carrosVendidos= int(input("Quantos carros foram vendidos este mês?"))
total_vendas= float(input("Qual o valor total, em reais, das vendas dos carros?"))
salario=float(input("Qual é seu rendimento mensal?"))
comissao=float(input("Quanto é a comissão recebida pela venda de cada carro?"))

salario_final=salario + (comissao*num_carrosVendidos)+ (0.05*total_vendas)

print("O salário final é de: ", salario_final)
