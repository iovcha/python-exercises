#. Код Цезаря
phraze = input('введите фразу: ')
num = int(input('введите количество символов для сдвига: '))
new_phraze = ""
for i in phraze:
    if i >= "a" and i <= "z":# Обрабатываем букву в нижнем регистре, определяя ее позицию
        # в алфавите (0–25), вычисляя новую позицию и добавляя букву в сообщение
      pos = ord(i) - ord('a')
      pos = (pos + num) % 26
      new_char =chr(pos + ord('a'))
      new_phraze = new_phraze + new_char
    elif i >= "A" and i <= "Z":
      pos = ord(i) - ord('A')
      pos = (pos + num) % 26
      new_char = chr(pos + ord('A'))
      new_phraze = new_phraze + new_char
    else:
   # Если это не буква, просто сохраняем ее в сообщении
         new_phraze = new_phraze + i
print("Новое сообщение", new_phraze)


