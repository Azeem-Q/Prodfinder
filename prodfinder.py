fname = input('Enter File Name: ')
fname = fname + '.txt'
area = input('Enter Area: ')
soc = input('Enter SO Code: ') #Sales Officer Code
dac = input('Enter DA Code: ') #Delivery Asst. Code
fh = open(fname)
prodlst = []
while True:
    prncode = input('Enter Principal Code: ')
    if prncode == 'ok': break
    if len(prncode) < 4:
        prncode = ('0' * (4 - len(prncode))) + prncode 
    prodcode = input('Enter Product Code: ')
    if prodcode == 'ok': break
    if len(prodcode) < 4:
        prodcode = ('0' * (4 - len(prodcode))) + prodcode
    #print(prncode, prodcode)
    product = prncode + prodcode
    prodlst.append(product)

#print(prodlst)

fd = fh.readlines()
#print(fh)
nflst = []
flst = []
wrtlst = []

for prod in prodlst:
    for line in fd:
        if prod in line:
            wrtlst.append(line)
            if prod not in flst:
                flst.append(prod)
        else:
            if prod not in nflst: 
                nflst.append(prod) 
            continue

fh.close()

wrtlst.sort()
#print('fl', flst)

for pc in flst:
    if pc in nflst:
        nflst.remove(pc)

#print('nf', nflst)


with open('results.txt', 'w') as fh:
    for pc in nflst:
        fh.write(pc + ' not found \n')
    fh.write('\n' + area + ' ' + soc + '-' + dac + '\n')
    fh.writelines(wrtlst)

#import os
#os.system('pause')

import subprocess
subprocess.Popen(['notepad.exe', 'results.txt'])

