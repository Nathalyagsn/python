N = str(input('Digite seu nome: '))
dividido = N.split()
NSE = N.replace(" ", "")
NDL = len(NSE)
PN = len(dividido[0])
NM = N.upper()
Nm = N.lower()
print('O nome completo tem', NDL, 'letras')
print('A quantidade de letras do primeiro nome é:', PN, )
print('O nome maiusculo fica:', NM, )
print('O nome minusculo fica:', Nm, )
print('O nome sem espaços fica:', NSE, )