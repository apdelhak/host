import sys,os
from module.file import *
from module.sc import *

def x(t):
	v = ''
	v = raw_input(t)

	return str(v)

def main_menu():
	x("\n"+box("ABDOPUBGM",h)+"press enter to return ")
	os.system(sys.executable+" "+sys.argv[0])

def main():
	print "\nABDO HACK\n"
	print "THIS SCRIPT IS MADE BY @A_B_D_O_PUBG\n"
	print "WELCOME TO AMSM TOOL A_B_D_O_PUBG\n"
	print "                       ___ "
	print "         /)        ,-^     ^-. "
	print "        //        /           \\"
	print " .-----| |-------/  __     __  \---------.__"
	print " |"+h+"ABOOD"+r+" |"+m+">>>>>>"+r+" | /"+m+">> "+r+"\   /"+m+">> "+r+"\ |"+m+">>>>>>>>>>>>:>"+r
	print " `-----| |-------| \__/   \__/ |---------"
	print "        \\         \    /|\    /"
	print "         \)        \   \_/   /"
	print "                    |       |"
	print "                    |"+m+"A+M+S+M"+r+"|"
	print "                    \       /"
	print "                     ^-----^"
	print r+"["+h+"1"+r+"] START SEARCH"
	print r+"["+h+"2"+r+"] EXIT THIS TOOL\n"
	try:
		snm = x(box("ABDOPUBGM",h)+"SELECT [1/2] > ")
		if snm == '1':domain = x(box("ABDOPUBGM",h)+"ENTER UR DOMAIN HERE MA BOY > "); print "\n\n127.0.0.1	localhost\n127.0.0.1	localhost.localdomain\n255.255.255.255	broadcasthost\n::1		localhost\n127.0.0.1	local\n::1		ip6-localhost ip6-loopback\nfe00::0		ip6-localnet\nff00::0		ip6-mcastprefix\nff02::1		ip6-allnodes\nff02::2		ip6-allrouters\nff02::3		ip6-allhosts\nfe80::1%lo0	localhost\n\n\n127.0.0.1     localhost\n::1     ip6-localhost\n\n"; sub(domain); main_menu()
		elif snm == '2': raise SystemExit(box("ABDOPUBGM",h)+"DON'T FORGET TO JOIN OUR CHANNEL @A_B_D_O_PUBG !")
		else: main_menu()
	except KeyboardInterrupt:
		main_menu()

if __name__ == '__main__':
	main()
	