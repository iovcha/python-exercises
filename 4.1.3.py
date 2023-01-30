#Действительный номерной знак машины?
plate = str(input("номерной знак машины : "))
if len(plate) == 6 and \
 plate[0] >= "A" and plate[0] <= "Z" and \
 plate[1] >= "A" and plate[1] <= "Z" and \
 plate[2] >= "A" and plate[2] <= "Z" and \
 plate[3] >= "0" and plate[3] <= "9" and \
 plate[4] >= "0" and plate[4] <= "9" and \
 plate[5] >= "0" and plate[5] <= "9":
 print("Это номерной знак старого образца.")
elif len(plate) == 7 and \
 plate[0] >= "0" and plate[0] <= "9" and \
 plate[1] >= "0" and plate[1] <= "9" and \
 plate[2] >= "0" and plate[2] <= "9" and \
 plate[3] >= "0" and plate[3] <= "9" and \
 plate[4] >= "A" and plate[4] <= "Z" and \
 plate[5] >= "A" and plate[5] <= "Z" and \
 plate[6] >= "A" and plate[6] <= "Z":
 print("Это номерной знак нового образца.")
else:
 print("Неверный номерной знак.")