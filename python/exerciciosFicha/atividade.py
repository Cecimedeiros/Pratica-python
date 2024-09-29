temp=int(input("Informe a temperatura ambiente atual: "))

if (temp>=25 and temp<=30):
    print("O clima está agradável")
elif(temp>=31 and temp<=35):
    print("O clima está quente e recomendamos hidratação adequada.")
else: 
    print("Calor intenso, evite sair de casa.")
