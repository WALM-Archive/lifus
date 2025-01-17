from pathlib import Path

def search_os():
	if Path('/mnt/iso/bootmgr.efi').is_file():
		print('Windows')
	elif Path('/mnt/iso/boot/grub/').is_dir() or Path('/mnt/iso/boot/grub2').is_dir():
		print('Gnu/Linux')
	else:
		print('I not working with FreeBSD or Windows XP\nOr in /mnt/iso/ no mounted ISO file')

#search_os()
