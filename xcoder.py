#!/usr/bin/python3
import os
from pathlib import Path
import sys
import argparse

_ = argparse.ArgumentParser()
_.add_argument("-f", "--file", type=str)
_.add_argument("-d", "--dir", type=str)
_.add_argument("-E", "--encrypt", action="store_true")
_.add_argument("-D", "--decrypt", action="store_true")
_.add_argument("-K", "--key", type=str)
_.add_argument("--KeepOriginals", action="store_true")
_.add_argument("--DeleteOriginals", action="store_true")
args= _.parse_args()
##########################################
if args.encrypt is True and args.decrypt is True or args.encrypt is False and args.decrypt is False:
        print("[-] Error : Must Provide A Single Action i.e. Encrypt/Decrypt\nExitting!")
        sys.exit()
##########################################
if args.KeepOriginals is True and args.DeleteOriginals is True or args.KeepOriginals is False and args.DeleteOriginals is False:
        print("[-] Error : Must Provide A Single Post-Action i.e. Delete or Keep Originals\nExitting!")
        sys.exit()
##########################################
banner="\n\n\t  ██╗  ██╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗\n "
banner+="\t  ╚██╗██╔╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗\n"
banner+="\t   ╚███╔╝     ██║     ██║   ██║██║  ██║█████╗  ██████╔╝\n"
banner+="\t   ██╔██╗     ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗\n"
banner+="\t  ██╔╝ ██╗    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║\n"
banner+="\t  ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n"
banner+="\t        _____Encode or Decode any Text File_____\n"
banner+="\t                 ...  Coded By 3th1K  ...\n"
banner+="\t ~ Please give credits before using any part of the Code ~\n"
##########################################
if args.key is None:
	print("[-] Error : Must Provide The Key\nExitting !")
	sys.exit()
##########################################
single_file=dir_files=total_files=[]
if args.file is None and args.dir is None:
	print("[-] Error : Must Provide File/s\nExitting !")
	sys.exit()

if args.file != None:
	file=Path(args.file)
	if file.is_file():
		single_file=[args.file]
	else:
		print("[-] Error : Couldnot Find File\nExitting !")
		sys.exit()
if args.dir != None:
	dir=Path(args.dir)
	if dir.is_dir():
		print("Please Wait : Reading Files ...")
		dir_files = [os.path.join(r,file) for r,d,f in os.walk(args.dir) for file in f]
	else:
		print("[-] Error : Couldnot Find Directory\nExitting !")
		sys.exit()
total_files=single_file+dir_files
############################################
print(banner)
print("Current Options Set[*]\n")
if args.file:
	print("[+] File             :",args.file)
if args.dir:
	print("[+] Directory        :",args.dir)
if args.encrypt:
	print("[+] Action           : Encryption")
	print("[+] Encryption Key   :",args.key)
elif args.decrypt:
	print("[+] Action           : Decryption")
	print("[+] Decryption Key   :",args.key)
if args.KeepOriginals:
	print("[+] Post-Action      : Keep Original Files")
elif args.DeleteOriginals:
	print("[+] Post-Action      : Delete Original Files")
print("[+] Total File Count :",len(total_files),"\n")
##############################################
choice=input("Would You Like To Go With These Inputs? Y/N  : ").lower()
while choice !='y' and choice !='n' and choice !='yes' and choice !='no':
	print("[-] Please Give Correct Input")
	choice=input("Would You Like To Go With These Inputs? Y/N  : ").lower()
if choice == 'yes' or choice == 'y':
	print("\nStarting Process ...\n")
else:
	print("[-] Exitting !")
	sys.exit()
##############################################
def encode(file_name,raw_key):


	try :
		f_read=open(file_name,"r")
		print("[+] Encoding File :  ",file_name)
		f1=f_read.readlines()
		total=''
		for x in f1:
			total+=x
		f_read.close()
	except FileNotFoundError:
		print("File not found, Please Check your input ! ")
		exit()

	raw_line=total
	binary_line = ("".join("{:010b}".format(ord(i)) for i in raw_line))
	binary_a=binary_b=""
	for i in range(0,len(binary_line)//2):
		binary_b+=binary_line[i]
	for j in range(len(binary_line)//2,len(binary_line)):
		binary_a+=binary_line[j]
	if len(binary_b)<len(binary_a):
		binary_b+='0'
		flag='odd'
	else:
		flag='even'


	def join(a,b):
		joined=''
		for i in range(0,len(a)):
			joined+=a[i]+b[i]
		return joined





	def out(joined_letter):
		l=list(joined_letter)
		nl=[]
		final_string=''
		for i in range(0,len(joined_letter)//2):
			nl.append(l[0:2])
			l[0:2]=[]
		for ele in nl:
			final_string+=str(  int(  ele[0]+ele[1] ,2  )  )
		return final_string




	temp_val=out(join(binary_a,binary_b))

	if flag=='odd':
		out_val=join(temp_val,temp_val)
	elif flag=='even':
		out_val=temp_val
##########
	final_out=''
	key=("".join("{:010b}".format(ord(i)) for i in raw_key))
	while len(key)<len(out_val):
		key+=key
	for i in range(0,len(out_val)):
		final_out+=str(int(out_val[i])+int(key[i]))
##########
	encoded_output=file_name+"_ENCODED"
	f_write=open(encoded_output,"w")
	f_write.writelines(final_out)
	f_write.close()
	print("\t\t   |____ ... Done !\n")
####################################################################################################################################################
def decode(encoded_file,raw_key):
	
	try :
		encoded_read=open(encoded_file,'r')
		lines=encoded_read.readlines()
		print("[+] Decoding File :  ",encoded_file)
		total_lines=''
		for line in lines:
			total_lines+=line
		encoded=total_lines
		encoded_read.close()
	except FileNotFoundError:
		print("File Not Found, Please Check Your Input")
		exit()

############################################
	encoded_raw=''
	key=("".join("{:010b}".format(ord(i)) for i in raw_key))
	while len(key)<len(encoded):
		key+=key
	for i in range(0,len(encoded)):
		encoded_raw+=str(int(encoded[i])-int(key[i]))
############################################
	def detach(encoded_raw):
		encoded_a=''
		encoded_b=''
		for i in range(0,len(encoded_raw),2):
			encoded_a+=encoded_raw[i]
		for j in range(1,len(encoded_raw),2):
			encoded_b+=encoded_raw[j]
		if encoded_a==encoded_b:
			rflag='odd'
			return encoded_a,rflag
		else:
			rflag='even'
			return encoded_raw,rflag
	encoded_data, flag_recieved=detach(encoded_raw)

	binary_of_every_piece= ("".join("{:02b}".format(int(i)) for i in encoded_data))

	def detach2(mingled,rflag):
		encoded_a=''
		encoded_b=''
		for i in range(0,len(mingled),2):
			encoded_a+=mingled[i]
		for j in range(1,len(mingled),2):
			encoded_b+=mingled[j]
		if rflag=='odd':
			encoded_b=encoded_b[0:-1]
		return encoded_a, encoded_b

	encoded_a, encoded_b = detach2(binary_of_every_piece,flag_recieved)
	decoded_binary = encoded_b+encoded_a

	def f_out(decoded_binary):
		opl=list(decoded_binary)
		nnl=[]
		final_string=''
		for i in range(0,len(decoded_binary)//10):
			nnl.append(opl[0:10])
			opl[0:10]=[]
		for ele in nnl:
			final_string+=chr(  int(  ele[0]+ele[1]+ele[2]+ele[3]+ele[4]+ele[5]+ele[6]+ele[7]+ele[8]+ele[9] ,2  )  )
		return final_string
	final_outcome=f_out(decoded_binary)
	outfname=encoded_file[:-8]
	decoded_out=open(outfname,'w')
	decoded_out.writelines(final_outcome)
	print("\t\t   |____ ... Done !\n")



if args.encrypt:
	for file in total_files:
		if file[-8:] == '_ENCODED':
                        print("[-] Error :",file," Already Have \'_ENCODED\' flag")
                        print("\t  |____ ... SKIPPING !\n")
		else:
			encode(file,args.key)
			if args.KeepOriginals:
				print("\t\t   |____ ...  Keeping Original Files !\n")
			if args.DeleteOriginals:
				print("\t\t   |____ ...  Deleting Original Files !\n")
				os.remove(file)
	sys.exit()
if args.decrypt:
	for file in total_files:
		if file[-8:] != '_ENCODED':
			print("[-] Error :",file," Dont Have \'_ENCODED\' flag")
			print("\t\t   |____ ... SKIPPING !\n")
		else:
			decode(file,args.key)
			if args.KeepOriginals:
				print("\t\t   |____ ...  Keeping Original Files !\n")
			if args.DeleteOriginals:
				print("\t\t   |____ ...  Deleting Original Files !\n")
				os.remove(file)
	sys.exit()
