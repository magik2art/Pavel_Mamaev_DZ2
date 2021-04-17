x_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

i = 0
name1 = []
name2 = []
name3 = []
while i < len(x_list):
    name1.append(x_list[i].split())
    i += 1

i = 0
while i < len(x_list):
    name2.append(name1[i][-1])
    i += 1

i = 0
while i < len(x_list):
    name3.append(name2[i].capitalize())
    i += 1

i = 0
for text in name3:
    print("Привет - ", "".join(name3[i]) + "!")
    i += 1
