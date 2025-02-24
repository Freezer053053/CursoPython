mail=input("Introduce un mail: ")

arroba=mail.count('@')

if (arroba!=1 or mail.rfind('@')==(len(mail)-1) or mail.find('@')==0):
    print("Mail erróneo")
else:
    print("Mail correcto")