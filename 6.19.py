#Палиндром или нет?
strin = str(input("Введите строку: "))
strin  = strin.lower()
strin = strin.split()
strin = ''.join(strin)
signs = [" ",",",".","!","?","-","ь","ъ","'"]
strin_pol = ''
for symbol in signs:
    strin= strin.replace(symbol, '')
for i in range(len(strin) // 2):
    if strin[i] != strin[-i - 1]:
        strin_pol = "Не палиндром"
    else:
        strin_pol = 'Палиндром'
print(strin_pol)