
valorBolo=float(input ("Qual o valor do bolo?"))

quanti_salgado1=(int(input("Quanto comprou do primeiro tipo de salgado?")))
quanti_salgado2=(int(input("Quanto comprou do segundo tipo de salgado?")))
quanti_salgado3=(int(input("Quanto comprou do terceiro tipo de salgado?")))


preçoUnitario1=(float(input("Qual o preço unitário do primeiro tipo de salgado?")))
preçoUnitario2=(float(input("Qual o preço unitário do segundo tipo de salgado?")))
preçoUnitario3=(float(input("Qual o preço unitário do terceiro tipo de salgado?")))
total= valorBolo + (quanti_salgado1*preçoUnitario1) + (quanti_salgado2*preçoUnitario2) + (quanti_salgado3*preçoUnitario3)



print("O valor total necessário para organizar a festa é de: ", total/11)
