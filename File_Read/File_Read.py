import os
print("Read Line >")
f = open('test.txt', 'r')
for line in f:
    print(line, end="")
f.close()


print("\n\nRead char >")
f = open('test.txt', 'r')
ch = f.read(1)
while ch:
    print (ch)
    #print (ch, end="")
    ch = f.read(1)
    if ch=='c':
        print('#####')
f.close()
os.system("pause")
# 关闭打开的文件

