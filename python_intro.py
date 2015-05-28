if 3 > 2:
	print('hell yeah!')
if 7 > 5:
	print('duh')
else:
	print('no shit')
name = 'Kayla'
if name == 'Elf':
	print('Hey elf!')
elif name == 'Kayla':
	print('sup Kaylala')
else:
	print('who the hell are you')

def hi(name):
	print('Hi' + name + '!')
hi(" Rachel")

girls = ['Kayla', 'Hannah', 'Carey', 'Phoebe', 'Emma']
for name in girls:
	hi(name)
	print('Next girl')
for i in range(1, 6):
	print(i)