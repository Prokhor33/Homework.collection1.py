text = 'Мажор, Игорь, Вика, Жека, закон, регулярно, отец, мать, периодически, инсценировка'
text = text.lower()
text = text.replace(" ","")
print(list(set(text)))