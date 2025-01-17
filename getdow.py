import wget

ubuntu = 'https://releases.ubuntu.com/22.04.1/ubuntu-22.04.1-desktop-amd64.iso'
lubuntu = 'https://cdimage.ubuntu.com/lubuntu/releases/22.04.1/release/lubuntu-22.04.1-desktop-amd64.iso'
xubuntu = 'https://cdimages.ubuntu.com/xubuntu/releases/22.04/release/xubuntu-22.04.1-desktop-amd64.iso'
kubuntu = 'https://cdimage.ubuntu.com/kubuntu/releases/22.04.1/release/kubuntu-22.04.1-desktop-amd64.iso'
ubuntu_budgie = 'https://cdimage.ubuntu.com/ubuntu-budgie/releases/22.04.1/release/ubuntu-budgie-22.04.1-desktop-amd64.iso'
ubuntu_mate = 'https://cdimage.ubuntu.com/ubuntu-mate/releases/22.04/release/ubuntu-mate-22.04.1-desktop-amd64.iso'

linux_mint_cinnamon = 'https://mirrors.layeronline.com/linuxmint/stable/21.1/linuxmint-21.1-cinnamon-64bit.iso'
linux_mint_xfce = 'https://mirrors.layeronline.com/linuxmint/stable/21.1/linuxmint-21.1-xfce-64bit.iso'
linux_mint_mate = 'https://mirrors.layeronline.com/linuxmint/stable/21.1/linuxmint-21.1-mate-64bit.iso'

mx = 'https://sourceforge.net/projects/mx-linux/files/Final/Xfce/MX-21.3_x64.iso/download'

linux_lite = 'https://osdn.net/dl/linuxlite/linux-lite-6.2-64bit.iso'

kde_neon = 'https://files.kde.org/neon/images/user/20230112-0714/neon-user-20230112-0714.iso'

debian_base = 'https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso'

manjaro_gnome = 'https://download.manjaro.org/gnome/22.0/manjaro-gnome-22.0-221224-linux61.iso'
manjaro_kde = 'https://download.manjaro.org/kde/22.0/manjaro-kde-22.0-221224-linux61.iso'
manjaro_xfce = 'https://download.manjaro.org/xfce/22.0/manjaro-xfce-22.0-221224-linux61.iso'
manjaro_mate = 'https://download.manjaro.org/mate/22.0/manjaro-mate-22.0-230104-linux61.iso'
manjaro_cinnamon = 'https://download.manjaro.org/cinnamon/22.0/manjaro-cinnamon-22.0-230104-linux61.iso'

endeavouros = 'https://github.com/endeavouros-team/ISO/releases/download/1-EndeavourOS-ISO-releases-archive/EndeavourOS_Cassini_22_12.iso'

arch_base = 'https://geo.mirror.pkgbuild.com/iso/2023.01.01/archlinux-2023.01.01-x86_64.iso'

fedora_base = 'https://download.fedoraproject.org/pub/fedora/linux/releases/37/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-37-1.7.iso'
fedora_xfce = 'https://download.fedoraproject.org/pub/fedora/linux/releases/37/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-37-1.7.iso'
fedora_kde = 'https://download.fedoraproject.org/pub/fedora/linux/releases/37/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-37-1.7.iso'


def download(dis):
	global ubuntu 
	global lubuntu
	global xubuntu
	global kubuntu
	global ubuntu_budgie
	global ubuntu_mate
	global linux_mint_cinnamon
	global linux_mint_xfce
	global linux_mint_mate
	global mx
	global linux_lite
	global kde_neon
	global debian_base
	global manjaro_gnome
	global manjaro_kde 
	global manjaro_xfce
	global manjaro_mate
	global manjaro_cinnamon
	global endeavouros
	global arch_base
	global fedora_base 
	global fedora_xfce 
	global fedora_kde
	
	if dis == 'ubuntu':
		wget.download(ubuntu)
	elif dis == 'kubuntu':
		wget.download(kubuntu)
	elif dis == 'xubuntu':
		wget.download(xubuntu)
	elif dis == 'lubuntu':
		wget.download(lubuntu)
	elif dis == 'ubuntu_mate':
		wget.download(ubuntu_mate)
	elif dis == 'ubuntu_budgie':
		wget.download(ubuntu_budgie)
	elif dis == 'mx':
		wget.download(mx)
	elif dis == 'linux_lite':
		wget.download(linux_lite)
	elif dis == 'linux_mint_cinnamon':
		wget.download(linux_mint_cinnamon)
	elif dis == 'linux_mint_mate':
		wget.download(linux_mint_mate)
	elif dis == 'linux_mint_xfce':
		wget.download(linux_mint_xfce)
	elif dis == 'kde_neon':
		wget.download(kde_neon)
	elif dis == 'debian_base':
		wget.download(debian_base)
	elif dis == 'manjaro_gnome':
		wget.download('manjaro_gnome')
	elif dis == 'manjaro_kde':
		wget.download(manjaro_kde)
	elif dis == 'manjaro_xfce':
		wget.download(manjaro_xfce)
	elif dis == 'manjaro_mate':
		wget.download(manjaro_mate)
	elif dis == 'manjaro_cinnamon':
		wget.download(manjaro_cinnamon)
	elif dis == 'endeavouros':
		wget.download(endeavouros)
	elif dis == 'arch_base':
		wget.download(arch_base)
	elif dis == 'fedora_base':
		wget.download(fedora_base)
	elif dis == 'fedora_kde':
		wget.download(fedora_kde)
	elif dis == 'fedora_xfce':
		wget.download(fedora_xfce)