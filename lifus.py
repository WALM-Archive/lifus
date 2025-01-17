from tkinter import *
from tkinter import ttk, messagebox
import os
from tkinter import filedialog
import pygame
import sys
import time
import getfs
import getos
import getdow
from pathlib import Path

#твой гребаный юзернейм
os.system('whoami > username.txt')
username = open('username.txt', 'r')
user = username.readline()
userbyte = len(user)
usercheck = userbyte - 1
username.close()
username = open('username.txt', 'r')
user = username.readline(usercheck)

#и ваши девайсы
if Path(f'/run/media/{user}/').is_dir():
    os.system(f'ls /run/media/{user} > devices.txt')
    devices_name = open('devices.txt')
    devies_ex = devices_name.readlines()
elif Path(f'/media/{user}/').is_dir():
    os.system(f'ls /media/{user} > devices.txt')
    devices_name = open('devices.txt')
    devies_ex = devices_name.readlines()

iso_file = False

donest = 0

devicename = ''
 
pygame.mixer.init()

version = 'alfa 0.6'

color = 0

des = Tk()

def download_iso():
	global color
	downdes = Toplevel()
	if color == 0:
		downdes['bg'] = 'black'
	elif color == 1:
		downdes['bg'] = 'white'
	downdes.title('Download')
	downdes.geometry('250x250')
	downdes.resizable(width=0, height=0)

	def download_dis():
		if dis_st_combo.get() == '':
			contin()
		else:
			getdow.download(dis = dis_st_combo.get())


	def contin():
		if dis_combo.get() == 'debian':
			dis_st_combo['values'] = ('ubuntu', 'linux_mint_cinnamon', 'linux_mint-mate', 'linux_mint_xfce', 'mx', 'linux_lite', 'kde_neon', 'lubuntu', 'xubuntu',
			 'kubuntu', 'ubuntu_mate', 'ubuntu_budgie',  'debian_base')
		elif dis_combo.get() == 'arch':
			dis_st_combo['values'] = ('manjaro_gnome', 'manjaro_xfce', 'manjaro_kde', 'manjaro_cinnamon', 'manjaro_mate', 'endeavouros', 'arch_base')
		elif dis_combo.get() == 'fedora':
			dis_st_combo['values'] = ('fedora_xfce', 'fedora_kde', 'fedora_base')
		start_btn.config(text = 'start',command = download_dis)

	if color == 0:
		base_dis = Label(downdes, text = 'Change base\ndistributions', font = ('Nunito', 13), bg = 'black', fg = 'white')
		base_dis.place(x = 60 , y = 5)

		base_dis = Label(downdes, text = 'Change\ndistributions', font = ('Nunito', 13), bg = 'black', fg = 'white')
		base_dis.place(x = 60 , y = 80)

		start_btn = Button(downdes, text = 'search', font = ('Nunito', 16), bg = 'black', fg = 'white', command = contin)
		start_btn.place(x = 65, y = 190)
	elif color == 1:
		base_dis = Label(downdes, text = 'Change base\ndistributions', font = ('Nunito', 13), bg = 'white', fg = 'black')
		base_dis.place(x = 60 , y = 5)

		base_dis = Label(downdes, text = 'Change\ndistributions', font = ('Nunito', 13), bg = 'white', fg = 'black')
		base_dis.place(x = 60 , y = 80)
		start_btn = Button(downdes, text = 'search', font = ('Nunito', 16), bg = 'white', fg = 'black', command = contin)
		start_btn.place(x = 65, y = 190)

	dis_combo = ttk.Combobox(downdes, font = ('Nunito', 10), width = 25,  state = 'readonly', values = ('fedora', 'arch', 'debian'))
	dis_combo.place(x = 20, y = 60)

	dis_st_combo = ttk.Combobox(downdes, font = ('Nunito', 10), width = 25,  state = 'readonly')
	dis_st_combo.place(x = 20, y = 130)

	downdes.mainloop()


def about():
	global version
	global color
	print(f'Lifus: version {version}')
	aboutdes = Tk()
	aboutdes.title('About Lifus')
	aboutdes.geometry('500x250')
	aboutdes.resizable(width = False, height = False)
	about_can = Canvas(aboutdes, width = 500, height = 250, bg = 'black')
	about_can.pack()

	if color == 0:
		about_can['bg'] = 'black'

		about_label = Label(about_can, text = f'   Lifus\nversion {version}\n\n\n\nMade by WebMast', bg = '#000', fg = '#fff', font = ('Nunito', 16))
		about_label.place(x = 300, y = 50)

		about_can.create_line(60, 45, 60, 250, fill = '#fff')
		about_can.create_line(60, 45, 150, 45, fill = '#fff')
		about_can.create_line(150, 45, 150, 65, fill = '#fff')
		about_can.create_line(80, 65, 150, 65, fill = '#fff')
		about_can.create_line(80, 65, 80, 125, fill = '#fff')
		about_can.create_line(80, 125, 150, 125, fill = '#fff')
		about_can.create_line(150, 125, 150, 145, fill = '#fff')
		about_can.create_line(80, 145, 150, 145, fill = '#fff')
		about_can.create_line(80, 145, 80, 250, fill = '#fff')

		about_can.create_line(25, 45, 25, 250, fill = '#fff')
		about_can.create_line(45, 45, 45, 250, fill = '#fff')
		about_can.create_line(25, 45, 45, 45, fill = '#fff')
	elif color == 1:
		about_can['bg'] = 'white'

		about_label = Label(about_can, text = f'   Lifus\nversion {version}\n\n\n\nMade by WebMast', bg = '#fff', fg = '#000', font = ('Nunito', 16))
		about_label.place(x = 300, y = 50)

		about_can.create_line(60, 45, 60, 250, fill = '#000')
		about_can.create_line(60, 45, 150, 45, fill = '#000')
		about_can.create_line(150, 45, 150, 65, fill = '#000')
		about_can.create_line(80, 65, 150, 65, fill = '#000')
		about_can.create_line(80, 65, 80, 125, fill = '#000')
		about_can.create_line(80, 125, 150, 125, fill = '#000')
		about_can.create_line(150, 125, 150, 145, fill = '#000')
		about_can.create_line(80, 145, 150, 145, fill = '#000')
		about_can.create_line(80, 145, 80, 250, fill = '#000')

		about_can.create_line(25, 45, 25, 250, fill = '#000')
		about_can.create_line(45, 45, 45, 250, fill = '#000')
		about_can.create_line(25, 45, 45, 45, fill = '#000')


	aboutdes.mainloop()

def device_update():
	global devices_name
	devices_name.close()
	os.remove('devices.txt')
	if Path(f'/run/media/{user}/').is_dir():
		os.system(f'ls /run/media/{user} > devices.txt')
		devices_name = open('devices.txt')
		devies_ex = devices_name.readlines()
	elif Path(f'/media/{user}/').is_dir():
		os.system(f'ls /media/{user} > devices.txt')
		devices_name = open('devices.txt')
		devies_ex = devices_name.readlines()

	devices_combo['values'] = devies_ex

def change_iso():
	global iso_file
	print('Lifus: change iso')
	iso_file = filedialog.askopenfilename(initialdir =  ("/", "/run/media", "/home"),title = "search iso",filetypes = (("ISO Files","*.iso"),))
	if iso_file == '':
		pass
	else:
		print(f'Lifus: Changed {os.path.basename(iso_file)}')
		header_label.config(text = f'Changed {os.path.basename(iso_file)}')

def start():
	global iso_file
	global devices_combo
	global format_combo
	global donest
	global user
	global devicename
	devicename = devicename_entry.get()
	cdevices = devices_combo.get()
	cdevices = cdevices.split('\n')
	device_changer = cdevices[0]
	print(device_changer)
	status_label.config(text = 'verification of parametrs')
	pb_start.config(value = 1)
	des.update()
	if format_combo.get() == '':
			print('Lifus: No Changed of Type format')
			messagebox.showerror('Lifus', 'No Changed of Type format')
			donest += 0
	elif format_combo.get() == 'not formating':
			print('Lifus: formating: use not formating ')
			donest += 1
			getfs.search(device = device_changer, user = user)
			dev_block = open('dev_device.txt', 'r+')
			ddev = dev_block.read()
			os.system(f'sudo umount {ddev}')
			os.system('sudo mkdir /mnt/usb')

			os.system(f'sudo mount {ddev} /mnt/usb')
	elif format_combo.get() == 'fat32':
			print('Lifus: formating: use fat32 format')
			donest += 1
			status_label.place(x = 202, y = 265)
			status_label.config(text = 'formating FAT32')
			getfs.search(device = device_changer)
			time.sleep(5)
			dev_block = open('dev_device.txt')
			ddev = dev_block.read()
			os.system(f'sudo umount {ddev}')
			if devicename == '':
				os.system(f'sudo mkfs -t vfat -n lifus_drive {ddev}')
			else:
				os.system(f'sudo mkfs -t vfat -n {devicename} {ddev}')
			os.system('sudo mkdir /mnt/iso/')
			os.system('sudo mkdir /mnt/usb/')
			os.system(f'sudo mount {ddev} /mnt/usb/')
	elif format_combo.get() == 'ntfs':
			print('Lifus: formating: use ntfs format')
			donest += 1
			status_label.place(x = 202, y = 265)
			status_label.config(text = 'formating NTFS')
			getfs.search(device = device_changer)
			dev_block = open('dev_device.txt')
			ddev = dev_block.read()
			time.sleep(5)
			os.system(f'sudo umount {ddev}')
			if devicename == '':
				os.system(f'sudo mkfs -t vfat -n lifus_drive {ddev}')
			else:
				os.system(f'sudo mkfs -t vfat -n {devicename} {ddev}')
			os.system('sudo mkdir /mnt/iso')
			os.system(f'sudo mount {ddev} /mnt/usb/')
	if devices_combo.get() == '':
			donest += 0
			print('Lifus: not changed flash drive')
			messagebox.showerror('Lifus', 'Not changed flash drive')
	else:
			print(f'Use {device_changer} flash drive')
			donest += 1
	if iso_file == False or iso_file == '':
		donest +=0
		print('Lifus: not changed ISO file')
		messagebox.showerror('Lifus', 'Not changed ISO file')
	else:
		donest += 1
	if donest == 3:
		status_label.config(text = 'flash: coping files')
		pb_start.config(value = 2)
		des.update()
		if format_combo.get() == 'fat32' or format_combo.get() == 'ntfs':
			os.system('sudo mkdir /mnt/iso')
			os.system(f"sudo mount '{iso_file}' /mnt/iso/ ")
			getos.search_os()
			os.system(f'sudo cp -rp /mnt/iso/* /mnt/usb/')
			os.system(f"sudo umount '{iso_file}' ")
			os.system(f'sudo umount {ddev}')
			os.system(f'sudo mount {ddev} /run/media/{user}')
			os.system(f'sudo umount {ddev}')
		elif format_combo.get() == 'not formating':
			os.system('sudo mkdir /mnt/iso')
			os.system(f"sudo mount '{iso_file}' /mnt/iso/ ")
			getos.search_os()
			os.system(f'sudo cp -rp /mnt/iso/* /mnt/usb/')
			os.system(f'sudo umount {ddev}')
			os.system(f"sudo umount '{iso_file}' ")
		status_label.config(text = 'please wait...')
		pb_start.config(value = 3)
		status_label.place(x = 302, y = 265)
		des.update()
		time.sleep(10)
		messagebox.showinfo('Lifus', 'Done')
		donest = 0
		dev_block.close()
		os.remove('dev_device.txt')
		device_update()
		status_label.config(text = 'Done')
		pb_start.config(value = 0)
		des.update()
	else:
		print('Lifus: error in parametrs')
		messagebox.showerror('Lifus','Error in parametrs')
		donest = 0
		status_label.config(text = 'Error')
		pb_start.config(value = 0)
		des.update()


def close_security():
	print('Lifus: closing')
	username.close()
	os.remove('username.txt')
	devices_name.close()
	os.remove('devices.txt')
	sys.exit()

def music_load():
	global music
	print('Lifus: load music')
	music = filedialog.askopenfilename(initialdir =  ("/", "/run/media", "/home"),title = "Get search of track",filetypes = (("mp3 Music Files","*.mp3"),))

def play():
		global music
		pygame.mixer.music.load(music)
		print('Lifus: play music')
		pygame.mixer.music.play(loops = 1000)


def bg_black():
	global color
	color = 0
	print('Lifus: get black background')
	btn_icon_loon.place_forget()
	can["bg"] = "black"
	print('Lifus: get lines is black')
	can.create_line(0, 316, 653, 316, fill = '#fff')
	can.create_line(0,100, 653, 100, fill = '#fff')
	can.create_line(0, 260, 653, 260, fill = '#fff')
	print('Lifus: get labels is black')
	header_label.config(bg = '#000', fg = '#fff')
	music_label.config(bg = '#000', fg = '#fff')
	format_label.config(bg = '#000', fg = '#fff')
	devicename_label.config(bg = '#000', fg = '#fff')
	status_label.config(bg = '#000', fg = '#fff')
	changedevice_label.config(bg = '#000', fg = '#fff')
	print('Lifus: get buttons is black')
	btn_change.config(bg = 'black', fg = 'white')
	btn_change_music.config(bg = 'black', fg = 'white')
	btn_play_music.config(bg = 'black', fg = 'white')
	btn_download.config(bg = 'black', fg = 'white')
	btn_start.config(bg = 'black', fg = 'white')
	btn_about.config(bg = 'black', fg = 'white')
	btn_update_list_device.config(bg = 'black', fg = 'white')
	btn_icon_sun.place(x = 593, y = 326)

def bg_white():
	global color
	color = 1
	print('Lifus: get white background')
	btn_icon_sun.place_forget()
	can["bg"] = "white"
	print('Lifus: get lines is white')
	can.create_line(0, 316, 653, 316, fill = '#000')
	can.create_line(0, 100, 653, 100, fill = '#000')
	can.create_line(0, 260, 653, 260, fill = '#000')
	print('Lifus: get labels is white')	
	header_label.config(bg = '#fff', fg = '#000')
	music_label.config(bg = '#fff', fg = '#000')
	format_label.config(bg = '#fff', fg = '#000')
	devicename_label.config(bg = '#fff', fg = '#000')
	status_label.config(bg = '#fff', fg = '#000')
	changedevice_label.config(bg = '#fff', fg = '#000')
	print('Lifus: get buttons is white')
	btn_change.config(bg = 'white', fg = 'black')
	btn_change_music.config(bg = 'white', fg = 'black')
	btn_play_music.config(bg = 'white', fg = 'black')
	btn_download.config(bg = 'white', fg = 'black')
	btn_start.config(bg = 'white', fg = 'black')
	btn_about.config(bg = 'white', fg = 'black')
	btn_update_list_device.config(bg = 'white', fg = 'black')
	btn_icon_loon.place(x = 593, y = 326)

des.geometry('653x386')
des["bg"] = "black"
des.title('Lifus')
des.resizable(width=0, height=0)
can = Canvas(des, width = 653, height = 386, bg = 'black')
can.pack()
print('Lifus: starting')

try:
 print('Lifus: loading sun iconimage: white theme')
 icon_sun_white = PhotoImage(file = 'src/theme/white/icon_sun.png')
except:
 print('Lifus: error of loading sun iconimage\nLifus: error stadia: green')
 messagebox.showerror('Lifus', 'Error of loading files')
try:
 print('Lifus: loading loon iconimage: black theme')
 icon_loon_black = PhotoImage(file = 'src/theme/black/icon_loon.png')
except:
 print('Lifus: error of loading loon iconimage\nLifus: error stadia: green')
 messagebox.showerror('Lifus', 'Error of loading files')

print('Lifus: create buttons')
btn_icon_sun = Button(can, image = icon_sun_white, width = 40, height = 40, bg = 'black', fg = 'white', command = bg_white)
btn_icon_loon = Button(can, image = icon_loon_black, width = 40, height = 40, bg = 'white', command = bg_black)
btn_change = Button(can, bg = 'black', fg = 'white', text = 'change file', font = ('Nunito', 16), command = change_iso)
btn_download = Button(can, bg = 'black',fg = 'white', text = 'download', font = ('Nunito', 16), command = download_iso)
btn_change_music = Button(can, bg = 'black', fg = 'white', text = 'change', font = ('Nunito', 16), command = music_load)
btn_play_music = Button(can, bg = 'black', fg = 'white', text = 'play', font = ('Nunito', 16), command = play)
btn_start = Button(can, bg = 'black', fg = 'white', text = 'start', font = ('Nunito', 16), command = start)
btn_update_list_device = Button(can, bg = 'black', fg = 'white', width = 15, text = 'update devices', font = ('Nunito', 12), command = device_update)
btn_about = Button(can, bg = 'black', fg = 'white', text = 'about', font = ('Nunito', 16), command = about)
print('Lifus: create lines')
can.create_line(0, 316, 653, 316, fill = '#fff')
can.create_line(0, 100, 653, 100, fill = '#fff')
can.create_line(0, 260, 653, 260, fill = '#fff')
print('Lifus: create text labels')
header_label = Label(can, text = 'Change ISO Image/Download ISO image', font = ('Nunito', 16), fg = '#fff', bg = '#000')
music_label = Label(can, text = 'Play a background music', font = ('Nunito', 16), fg = '#fff', bg = '#000')
format_label = Label(can, text = 'Change format', font = ('Nunito', 13), fg = '#fff', bg = '#000')
status_label = Label(can, text = 'Done', font = ('Nunito', 16), bg = '#000', fg = '#fff')
devicename_label = Label(can, text = 'Change device name', font = ('Nunito', 13), fg = '#fff', bg = '#000')
changedevice_label = Label(can, text = 'Change storage device', font = ('Nunito', 13), bg = '#000', fg = '#fff')
print('Lifus: create comboboxes')
format_combo = ttk.Combobox(can, font = ('Nunito', 10), state = 'readonly', values = ('fat32', 'ntfs', 'not formating'))
devices_combo = ttk.Combobox(can, font = ('Nunito', 10), state = 'readonly', values = devies_ex)
print("Lifus:create progressbar's")
pb_start = ttk.Progressbar(can, orient = 'horizontal', length = 653, maximum = 3, mode = 'determinate')
print("Lifus: create Entry's")
devicename_entry = Entry(can, font = ('Nunito', 10))

music_label.place(x = 5, y = 335)
header_label.place(x = 5,y = 10)
format_label.place(x = 5, y = 106)
devicename_label.place(x = 185, y = 106)
status_label.place(x = 302, y = 265)
changedevice_label.place(x = 5, y = 156)

btn_icon_sun.place(x = 593, y = 326)
btn_change.place(x = 5, y = 56)
btn_download.place(x = 140, y=56)
btn_change_music.place(x = 255, y = 330)
btn_play_music.place(x = 355, y = 330)
btn_start.place(x = 580, y = 216)
btn_about.place(x = 500, y = 216)
btn_update_list_device.place(x = 5, y = 203)

format_combo.place(x = 5, y = 136)
devices_combo.place(x = 5, y = 180)

pb_start.place(x = 0, y = 300)

devicename_entry.place(x = 185, y = 136)

des.protocol("WM_DELETE_WINDOW", close_security)
print('Lifus: get working')
des.mainloop()
