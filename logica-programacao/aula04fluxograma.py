# Decisões-expressões
# var. jan,fev,mar,abr,m,s

jan = float (input ('Digite o valor total das vendas de janeiro: $'))
fev = float (input ('Digite o valor total das vendas de fevereiro: $'))
mar = float (input ('Digite o valor total das vendas de março: $'))
abr = float (input ('Digite o valor total das vendas de abril: $'))

s = jan+fev+mar+abr
m = s/4

print ('A sua média salarial foi de ${:.2f}' .format(m))

if (m >= 5000):
    print ('Parebêns! Você receberá um bônus salarial de 10%.')
else:
    print ('Não foi nesse mês.Não desista! Ainda assim você receberá um abono de 3%.')

