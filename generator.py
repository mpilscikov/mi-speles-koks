'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

import random # importē ģeneratoru
rand_list=[] # inicializē masīvu
n=5 # nosaka ģenerējamo skaitļu daudzumu
for i in range(n): # izvēlās vērtību diapazonu
    rand_list.append(random.randint(30000,99999)) #ģenerē nejaušības skaitli no diapazona
print(rand_list) # izprintē ģenerētos skaitļus
m = int(input())
banka=0 
for izv_sk in range(m):
izv_sk=37276
if izv_sk%2==0:
    banka=banka+1
    print(banka)
    if izv_sk%3==0 and izv_sk%2==0:
        banka=banka-1
        print(banka)
       