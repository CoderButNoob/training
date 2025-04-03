i1 = open(r"C:\Program Files\GE\training\file_handling2\q3\file1.txt","r")
i2 = open(r"C:\Program Files\GE\training\file_handling2\q3\file2.txt", "r")
op = open(r"C:\Program Files\GE\training\file_handling2\q3\output.txt", "w")

for line1 , line2 in zip(i1,i2):
    op.write(line1.strip() + " " + line2)

op.writelines(i1.readlines())
op.writelines(i2.readlines())
