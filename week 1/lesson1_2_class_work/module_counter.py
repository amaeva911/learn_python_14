from collections import Counter

phones = ['iphone', 'samsung', 'samsung', 'LG', 'LG']
count = Counter(phones)
print(count)
print(count['LG'])

text = 'В стране Ксанад благословенной дворец  построил  Кубла Хан, где Альф бежит, поток священный, сквозь мглу пещер гигантских, пенный,впадает  в сонный океан.'
count = Counter(text.lower().replace(' ',''))
print(count)