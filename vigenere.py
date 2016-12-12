import hashlib

str="ABCDEFGHIJKLMNOPQRSTUVWXYZ[]"
c="LMIG]RPEDOEEWKJIQIWKJWMNDTSR]TFVUFWYOCBAJBQ"
arr=[[0 for col in range(28)] for row in range(28)]
for i in range(len(str)):
	for j in range(len(str)):
		arr[i][j]=str[(i+j)%28] 

#key="VIGENERE"+"AAAAA"
#p="SECCON["+"ABCD"+"]"
print(c)
hash="f528a6ab914c1ecf856a1d93103948fe"
def brutef(key,c):
        pp=""
        for i in range(len(c)):
                if(i==6):
                        pp+='{'
                        continue
                if(i==42):
                        pp+='}'
                        continue
                for j in range(28):
                        rr=ord(key[i%12])-0x41
                        if(rr==28):
                                rr=27
                        if(arr[rr][j]==c[i]):
                                break
                if(j==27):
                        j=j+1
                pp+=chr(0x41+j)
        h=hashlib.md5(pp.encode()).hexdigest()
        if(h[0]=='f'and h[1]=='5'and h[2]=='2' and h[3]=='8'):
                print(h)
                print(pp)
        if(hash==hashlib.md5(pp.encode()).hexdigest()):
                print(pp)

c="LMIG]RPEDOEEWKJIQIWKJWMNDTSR]TFVUFWYOCBAJBQ"
arr2="ABCDEFGHIJKLMNOPQRSTUVWXYZ[]"
print(arr2)
for i in arr2:
        print(i)
        for j in arr2:
                for k in arr2:
                        for l in arr2:
                                key="VIGENERE"
                                key+=i
                                key+=j
                                key+=k
                                key+=l
                                brutef(key,c)

print("end")

