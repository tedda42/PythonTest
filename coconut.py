import math
fr = open('cocoin.txt', 'r')
f = fr.readline().strip().split(" ")
# print(f)
ix = int(f[0])
iy = int(f[1])
id = int(f[2])
f = fr.readline().strip().split(" ")
cx = int(f[0])
cy = int(f[1])
cd = int(f[2])
icd = math.sqrt((ix-cx)*(ix-cx) + (iy-cy)*(iy-cy));
# print(icd)

fileWriter = open('cocoout.txt', 'w')

if icd > (id + cd):
    fileWriter.write("no")
elif icd >= cd and icd >= id: #points not inside other circle
    fileWriter.write("yes")
elif (icd + id) < cd:
    fileWriter.write("no")
elif (icd + cd) < id:
    fileWriter.write("no")
else:
    fileWriter.write("yes")
