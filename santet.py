# coding=utf-8
import os,sys,time

def asu(s):
	for a in s + '\n':
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.1)
		
def metu():
	asu('\n\033[1;93mTerimakasih telah menggunakan tools ini,\nini hanya tools mainan doang yahh hehee\033[1;97m')
	os.sys.exit()
	
njer = "\n\n\033[1;97m=========================================\n==>        \033[1;91mTOOLS SANTET ONLINE        \033[1;97m<== \n=========================================\n"

def santet():
	os.system('clear')
	print njer
	print('\033[1;97m[!] \033[1;96mMOHON DI ISI PAKK \033[1;97m[!]')
	nama = raw_input('\033[1;97m[*] \033[1;93mNama korban ? \033[1;91m: \033[1;97m')
	if nama =="":
		print'\033[1;91mIsi yang benar pakk!'
		time.sleep(1)
		santet()
	else:
		ttl = raw_input('\033[1;97m[*] \033[1;93mTanggal lahir korban ? \033[1;91m: \033[1;97m')
		if ttl =="":
			print'\033[1;91mIsi yang benar pakk!'
			time.sleep(1)
			santet()
		else:
			jenis = raw_input('\033[1;97m[*] \033[1;93mJenis santet ? \033[1;91m: \033[1;97m')
			if jenis =="":
				print'\033[1;91mIsi yang benar pakk!'
				time.sleep(1)
				santet()
			else:
				by = raw_input('\033[1;97m[*] \033[1;93mDisantet oleh ? \033[1;91m: \033[1;97m')
				if by =="":
					print'\033[1;91mIsi yang benar pakk!'
					time.sleep(1)
					santet()
				else:
					time.sleep(2)
					asu('\n[!] \033[1;96mKETERANGAN \033[1;97m:')
					time.sleep(2)
					print 40*"\033[1;97m="
					print"\033[1;92m[✓] \033[1;91mNama korban\033[1;97m" ,nama, "\n\033[1;92m[✓] \033[1;91mTanggal lahir korban\033[1;97m" ,ttl, "\n\033[1;92m[✓] \033[1;91mJenis santet\033[1;97m" ,jenis
					print 40*"\033[1;97m="
					time.sleep(2)
					asu('\033[1;97mTunggu sebentar pakk lagi proses hehee !!')
					time.sleep(3)
					print'\n\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(1)
					print'\033[1;92m[✓] Berhasil \n\033[1;91mTersantet by \033[1;97m:' ,by
					time.sleep(3)
					print'\n\033[1;97mSudah selesai pakk korban sudah disantet hehee!'
					pilih()
				

def pilih():
	ya = raw_input('Ingin santet ulang? (y/t) : ')
	if ya =="":
		print'\033[1;91mIsi yang benar!\033[1;97m'
		pilih()
	elif ya =="y":
		santet()
	elif ya =="t":
		metu()
	elif ya =="Y":
		santet()
	elif ya =="t":
		metu()
	else:
		print'\033[1;91mIsi yang benar!'
		pilih()
	

if __name__ == "__main__":
	santet()