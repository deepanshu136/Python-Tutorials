text_file=open("text.txt","w")
text_file.write("hello my namen is deepanshu kumar \n")
text_file.close()
text_file=open("text.txt","a")
text_file.write("with the help of append can re axis the file and withe write again add whatever we wanted to add in pur file")
text_file.close()
text_file=open("text.txt","r")
print(text_file.read())
text_file.close() 

