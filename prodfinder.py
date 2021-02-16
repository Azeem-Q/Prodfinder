prodlst = []
nflst = []
flst = []
wrtlst = []
areahead = []
retrieved = 0

def prodfinder():
    global prodlst, nflst, flst, wrtlst, areahead, retrieved
    fname = input('Enter File Name: ')
    fname = fname + '.txt'
    area = input('Enter Area: ')
    soc = input('Enter SO Code: ') #Sales Officer Code
    dac = input('Enter DA Code: ') #Delivery Asst. Code
    fh = open(fname)
    
    while True:
        if retrieved > 0:
            same = input('Do you want to search the same products again? (y/n)')
            if same == 'y':
                flst = []
                nflst = []
                wrtlst = []
                break
            elif same == 'n':
                prodlst = []
                flst = []
                nflst = []
                wrtlst = []
            else:
                print('Please enter either y or n')
                continue

        while True:
            prncode = input('Enter Principal Code: ')
            if prncode == 'ok': break
            if len(prncode) < 4:
                prncode = ('0' * (4 - len(prncode))) + prncode 

            prodcode = input('Enter Product Code: ')
            if prodcode == 'ok': break
            if len(prodcode) < 4:
                prodcode = ('0' * (4 - len(prodcode))) + prodcode
            
            product = prncode + prodcode
            prodlst.append(product)
        break

    fd = fh.readlines()
    
    retrieved = retrieved + 1
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
    areahead = []
    areahead.append('\n' + area + ' ' + soc + '-' + dac + '\n')

def filewrite(attr):
    global prodlst, nflst, flst, wrtlst, areahead
    wrtlst.sort()

    for pc in flst:
        if pc in nflst:
            nflst.remove(pc)

    
    with open('results.txt', attr) as fh:
        for pc in nflst:
            if retrieved == 1:
                fh.write(pc + ' not found \n')
            else:
                fh.write('\n' + pc + ' not found \n')
        fh.writelines(areahead)
        fh.writelines(wrtlst)        

prodfinder()
filewrite('w')

while True:
    another = input('Do you want to search another file? (y/n)')
    if another == 'y':
        prodfinder()
        filewrite('a')
    elif another == 'n':
        break
    else:
        print('Please enter either y or n')
        continue


import subprocess
subprocess.Popen(['notepad.exe', 'results.txt'])

