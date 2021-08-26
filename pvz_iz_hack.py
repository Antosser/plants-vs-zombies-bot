import mss
import numpy
import pyautogui
import keyboard
from math import *
import time

mss = mss.mss()
size = pyautogui.size()

print('Waiting for input...')
keyboard.wait('insert')
topleft = pyautogui.position()
while keyboard.is_pressed('insert'):
	pass
keyboard.wait('insert')
bottomright = pyautogui.position()
xgap = round(abs(topleft[0] - bottomright[0]) / 3)
ygap = round(abs(topleft[1] - bottomright[1]) / 4)
print(f'{xgap=}, {ygap=}')
time.sleep(1)

grid = numpy.arange(20).reshape(5, 4).tolist()
print(grid)
print('Taking screenshot...')
shot = mss.grab({"left": 0, "top": 0, "width": size[0], "height": size[1]}).pixels

#print(numpy.array(shot.pixels).shape)
print('-----')
for j in range(5):
	for i in range(4):
		difsum = []
		for y in range(40):
			for x in range(40):
				pos = (topleft[0] + xgap * i - 20 + x, topleft[1] + ygap * j - 20 + y)
				#print(pos)
				difsum.append(shot[pos[1]][pos[0]])
		color = [0, 0, 0]
		for k in difsum:
			color[0] += k[0]
			color[1] += k[1]
			color[2] += k[2]
		color[0] /= len(difsum)
		color[1] /= len(difsum)
		color[2] /= len(difsum)
		color[0] = int(color[0])
		color[1] = int(color[1])
		color[2] = int(color[2])
		print(color)
		dif = []
		#su, sp, pe, sn
		dif.append(list(numpy.subtract((118, 85, 18), color)))
		dif.append(list(numpy.subtract((38, 71, 73), color)))
		dif.append(list(numpy.subtract((90, 117, 31), color)))
		dif.append(list(numpy.subtract((75, 121, 91), color)))
		print(f'{dif=}')
		for k in range(4):
			for l in range(3):
				dif[k][l] = abs(dif[k][l])
			dif[k] = sum(dif[k])

		print(f'{dif=}')
		bestmatch = 0
		bestnumber = 9999
		for k in range(4):
			if dif[k] < bestnumber:
				bestnumber = dif[k]
				bestmatch = k
		bestword = '-'
		if bestmatch == 0:
			bestword = 'su'
		if bestmatch == 1:
			bestword = 'sp'
		if bestmatch == 2:
			bestword = 'pe'
		if bestmatch == 3:
			bestword = 'sn'
		print(bestword)
		print(f'{j=}, {i=}')
		grid[j][i] = bestword
		print(grid)
		print('-----')
	print('-------')
print(grid)