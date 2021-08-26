import keyboard
import pyautogui
import time
import numpy
from os import system
import threading

def clicker(a, b, c, d):
	system(f'C:\\Users\\Antosser-PC\\Desktop\\python\\pvz\\pvz-ls-hack-clicker.exe 0 {a} {b} {c} {d}')

if 0:
	print('Waiting for input...')
	keyboard.wait('insert')
	print('1')
	topleft = pyautogui.position()
	while keyboard.is_pressed('insert'):
		pass
	keyboard.wait('insert')
	print('2')
	bottomright = pyautogui.position()
	xgap = round(abs(topleft[0] - bottomright[0]) / 7)
	ygap = round(abs(topleft[1] - bottomright[1]) / 5)
	print(f'{xgap=}, {ygap=}')
	system(f'C:\\Users\\Antosser-PC\\Desktop\\python\\pvz\\pvz-ls-hack-clicker.exe 2 0 0 0 {topleft[0]} {topleft[1]} {xgap} {ygap}')
	pyautogui.moveTo(topleft[0] + xgap * 3, topleft[1] + ygap * 5.8)
	time.sleep(.1)
	pyautogui.click()

	print('Waiting for input...')
	keyboard.wait('insert')
	print('3')
	left = pyautogui.position()
	while keyboard.is_pressed('insert'):
		pass
	keyboard.wait('insert')
	print('4')
	right = pyautogui.position()
	while keyboard.is_pressed('insert'):
		pass
	keyboard.wait('insert')
	print('5')
	topleft2 = pyautogui.position()
	while keyboard.is_pressed('insert'):
		pass
	keyboard.wait('insert')
	print('6')
	bottomright2 = pyautogui.position()
	xgap2 = round(abs(topleft2[0] - bottomright2[0]) / 8)
	ygap2 = round(abs(topleft2[1] - bottomright2[1]) / 5)
	gap = round(abs(left[0] - right[0]) / 7)
	p1 = (left[0] + gap * 0, left[1])
	p2 = (left[0] + gap * 1, left[1])
	p3 = (left[0] + gap * 2, left[1])
	p4 = (left[0] + gap * 3, left[1])
	while keyboard.is_pressed('insert'):
		pass
	print('Waiting for input...')
	keyboard.wait('insert')
	print('7')
	k1 = pyautogui.position()
	pyautogui.click()
	while keyboard.is_pressed('insert'):
		pass
	print('Waiting for input...')
	keyboard.wait('insert')
	print('8')
	k2 = pyautogui.position()
	pyautogui.click()
	while keyboard.is_pressed('insert'):
		pass
	print('Waiting for input...')
	keyboard.wait('insert')
	print('9')
	k3 = pyautogui.position()
	pyautogui.click()
	time.sleep(4.5)
	#print(f'{topleft=}, {bottomright=}, {topleft2=}, {bottomright2=}, {left=}, {right=}, {gap=}, {xgap=}, {ygap=}, {xgap2=}, {ygap2=}, {p1=}, {p2=}, {p3=}, {p4=}, {k1=}, {k2=}, {k3=}')
else:
	topleft=(323, 293)
	bottomright=(991, 915)
	topleft2=(384, 176)
	bottomright2=(1540, 972)
	left=(448, 81)
	right=(1131, 75)
	gap=98
	xgap=95
	ygap=124
	xgap2=144
	ygap2=159
	p1=(448, 81)
	p2=(546, 81)
	p3=(644, 81)
	p4=(742, 81)
	k1=(1579, 14)
	k2=(946, 637)
	k3=(747, 705)
	keyboard.wait('insert')
while True:
	system(f'C:\\Users\\Antosser-PC\\Desktop\\python\\pvz\\pvz-ls-hack-clicker.exe 2 0 0 0 {topleft[0]} {topleft[1]} {xgap} {ygap}')
	pyautogui.moveTo(topleft[0] + xgap * 3, topleft[1] + ygap * 5.8)
	#time.sleep(.1)
	pyautogui.click()
	time.sleep(2.3)
	system(f'C:\\Users\\Antosser-PC\\Desktop\\python\\pvz\\pvz-ls-hack-clicker.exe 1 {left[0]} {left[1]} {gap} {topleft2[0]} {topleft2[1]} {xgap2} {ygap2}')
	pyautogui.moveTo(topleft2[0] + xgap2 * 4, topleft2[1] + ygap2 * 5.5)
	#time.sleep(.1)
	pyautogui.click()
	threading.Thread(target=clicker, args=(topleft2[0], topleft2[1], bottomright2[0] - topleft2[0] + xgap2, bottomright2[1] - topleft2[1]),).start()
	time.sleep(100)
	system('taskkill /f /im pvz-ls-hack-clicker.exe')
	pyautogui.moveTo(k1)
	pyautogui.click()
	pyautogui.moveTo(k2)
	pyautogui.click()
	pyautogui.moveTo(k3)
	pyautogui.click()
	time.sleep(4.3)