from time import time
cvf=0
Portal=2
import os
import binascii
import math


zaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []

blockDR=168500

lenf=0
name=""
szx=""
wer=""
namez = input("c,c2: compress or e,u2: extract? ")

f = open("PI_10M.txt", "r")
PI=f.read()


#@Author Jurijus pacalovas
class compression:

    def Areacu2(self):
                    if namez=="u2":
                        x=0
                        x1=0
                        x2=0
                        x = time()
                        name = input("What is name of file? ")
                        namea="file.W"
                        namem=""
                        namema="?"
                       
                        blockw=5
                        blockw1=4
                        nameas=name
                        nac=len(nameas)
                        if nameas[nac-8:nac]==".bin.bin":
                            nameas=nameas[0:nac-8]
                        countraz=0
                        C=0
                        s=""
                        assx=0
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []
                       
            
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        with open(nameas, "a") as f3:
                                f3.write(s)
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            data = binary_file.read()
                            s=str(data)
                            lenf2=len(data)
                            lenf1=len(data)
                            if lenf1<6:
                                ##print("This file is too small");
                                raise SystemExit
                            if lenf1>(2**32)-1:
                                ##print("This file is too big");
                                raise SystemExit
            
                            while assx<10:
                                qqqwz=0
                                
                                a=0
                                ass=0
                                asss=0
                                b=0
                                aaqw=""
                                aaqws=""
                                l=""
                                j=0
                                b=0
                                aq=0
                                qfl=0
                                t=0
                                h=0
                                byteb=""
                                notexist=""
                                lenf=0
                                numberschangenotexistq = []
                                numberschangenotexistqz = []
                                qwa=0
                                m = []
                                p=0
                                
                                d=1
                                a=0
                                asd=""
                                b=0
                                szx=""
                                asf2="0b"
                                while b<1790:
                                    m+=[-1]
                                    b=b+1
                                k = []
                                wer=""
                                numberschangenotexist = []
                                numbers = []
                                assa=0
                                asaaq=""
                                szxzzzas=""
                                s=""
                                blockw=4
                                blockw1=3
                                sdaa=""
                                aas=0
                                asaaq=""
                                asaaqq=""
                                asaaql=""
                                asaaqll=""
                                en=0
                                assa=0
                                assas=0
                                wer=""
                                asaaqt=""
                                countraz=countraz+1
                                ddm=0
                                wers=""
                                asaaqllw=""
                                asaaqll=""
                                qqqslls=""
                                qqqslls=""
                                asaaqlls=""
                                asaaqllsq=""
                                ww=10
                                rr1=0
                                rr12=0
                                wers=""
                                countraz=0
                                blockD=(blockDR*14)
                                blockDE=(blockDR*14)-15
                                BlockF=blockDR
            
            
                                
                               
            
                               
                                with open(nameas, "ab") as f2:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    
                                    lenf1=len(data) 
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                          
                                    for byte in sda:

                                        if sda[0:8]=="01111111":
                                            
                                            sda=sda[8:]
                                            wer=sda
                                            n = int(wer, 2)
                                    
                                            qqwslenf=len(wer)
                                            qqwslenf=(qqwslenf/8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                                
                                               
                                                            
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)
                                            data=jl
                                            qqqwz=qqqwz+1
                                            szxzzza=""
                                            szxzs=""
                                           
                                            
                                            blockw=4
                                            blockw1=3
                                        
                                            #print(sssssw)
                                                
                                            wer=""
                                            
                              
                                            assx=10
                                            
                                            f2.write(jl)
                                            x2 = time()
                                            x3 = x2-x
                                            return print(x3) 
                                        if sda[0:1]=="1":
                                            sda=sda[1:]
                                        elif sda[0:2]=="01":
                                            sda=sda[2:]
                                        elif sda[0:3]=="001":
                                            sda=sda[3:]
                                        elif sda[0:4]=="0001":
                                            sda=sda[4:]
                                        elif sda[0:5]=="00001":
                                            sda=sda[5:]
            
                                        elif sda[0:6]=="000001":
                                            sda=sda[6:]
                                        elif sda[0:7]=="0000001":
                                            sda=sda[7:]
            
                                        elif sda[0:8]=="00000001":
                                            sda=sda[8:]
            
                                            
                                        sdalong=len(sda)
            
                                        
                                        if sda[sdalong-1:sdalong]=="1":
                                            sda=sda[:sdalong-1]
                                        elif sda[sdalong-2:sdalong]=="10":
                                            sda=sda[:sdalong-2]
                                        elif sda[sdalong-3:sdalong]=="100":
                                            sda=sda[:sdalong-3]
                                        elif sda[sdalong-4:sdalong]=="1000":
                                            sda=sda[:sdalong-4]
                                        elif sda[sdalong-5:sdalong]=="10000":
                                            sda=sda[:sdalong-5]
                                        elif sda[sdalong-6:sdalong]=="100000":
                                            sda=sda[:sdalong-6]
            
                                        elif sda[sdalong-7:sdalong]=="1000000":
                                            sda=sda[:sdalong-7]
            
                                        elif sda[sdalong-8:sdalong]=="10000000":
                                            sda=sda[:sdalong-8]


                                    

                                            

                                        


            
                                            
                                        sdad=len(sda)
                                        
                                        eo=0
                                        el=0
                                        
                                        while eo<sdad:
                                            wers=""
                                            
                                            
                                            el=eo
                                            eo=eo+blockD
                                            takebitsize=sda[el:eo]
                                            xssd=len(takebitsize)
                                            el=eo-blockD
                                            eo=eo-blockD

                                            
                                            if xssd<blockDE:
                                                wer=wer+takebitsize
                                                C=C+xssd
                                                   
                                                n = int(wer, 2)
                                        
                                                qqwslenf=len(wer)
                                                qqwslenf=(qqwslenf/8)*2
                                                qqwslenf=str(qqwslenf)
                                                qqwslenf="%0"+qqwslenf+"x"
                                             
                                                jl=binascii.unhexlify(qqwslenf % n)
                                                sssssw=len(jl)
                                                data=jl
                                                qqqwz=qqqwz+1
                                                szxzzza=""
                                                szxzs=""
                                        
                                                blockw=4
                                                blockw1=3
                                    
                                                    #print(sssssw)
                                            
                                                wer=""
                                       
                                                assx=10
                                        
                                                f2.write(jl)
                                                
                                                  
                                            el=eo
                                            eo=eo+14
                                            takebit2=sda[el:eo]
                                            takebitdw2=int(takebit2, 2)
                                            
                                            el=eo
                                            eo=eo+blockDE
                                            takebit=sda[el:eo]
             
                                            takebitdw=int(takebit, 2)
                                            sw=0
                                            numbertc=takebitdw
                                            
                                               
                                            while sw<BlockF:
                                                    
                                                numbertc3=numbertc%16383
                                                numbertc1=numbertc//16383
                                                numbertc2=int(numbertc1)
                                                    
                                                    
                                                if takebitdw2==numbertc3:
                                                    numbertc3=16383
                                                        #print(takebitdw2)
                                                       # print(numbertc3)
                                                        
                                                    
                                                szxzzz=""
                                                szxzzz=bin(numbertc3)[2:]
                                                dd=len(szxzzz)
                                                xc=14-dd%14
                                                z=0
                                                if xc!=0 and dd!=14:
                                                    while z<xc:
                                                        szxzzz="0"+szxzzz
                                                        z=z+1
                                                wers=wers+szxzzz
                                                    
                                                numbertc=numbertc2
                                                sw=sw+1
                                                    #print(sw)
                                                
                                            ddr=len(wers)
                                            
                                            sw=0
                                            el1=blockD
                                            eo1=blockD
                                           
                                            while sw<BlockF:
                                                    
                                                el1=eo1
                                                eo1=eo1-14
                                                takebit=wers[eo1:el1]
                                                C=el1
                                                    
                                                wer=wer+takebit
                                                sw=sw+1
                                                   
                                            wers=""
                                        


                                    wer=wer+sda[C:]
                                   
                                    lenf=len(wer)
                                    xc=8-lenf%8
                                    z=0
                                    if xc!=0:
                                        if xc!=8:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                    wer=szx+wer
                                    n = int(wer, 2)
                                    
                                    qqwslenf=len(wer)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                                        
                                       
                                                    
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                   
                                    
                                    blockw=4
                                    blockw1=3
                                
                                    #print(sssssw)
                                        
                                    wer=""
                                    
                      
                                    assx=10
                                    
                                    f2.write(jl)
                                    x2 = time()
                                    x3 = x2-x
                                    return print(x3) 

    
    def Areac2(self):
                    if namez=="c2":
                        x=0
                        x1=0
                        x2=0
                        x = time()
                        name = input("What is name of file? ")
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []


                        
                        blockD=(blockDR*14)-15
                        block=blockDR
                        blockw=block-1
                        blockw1=16384
                        virationc=16383
                        bitc=14
                        a=0
                        qfl=0
                        h=0
                        lenf1=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        qwa=0
                        z=0
                        m = []
                        p=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<blockw1:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        numberschangenotexist = []
                        numbers = []
                            
                        
                        namea=name+".bin.bin"
                        namem=name+"/"
            
                        nameas=name
                        nac=len(nameas)
            
                        s=""
                        qwt=""
                        sda=""
                        ert=0
                        aqwer=0
                        aqwq=0
                        aqwers=0
                        qwaw=""
                        qwaw1=""
                        xx=0
                        xx3=0
                        with open(namea, "w") as f4:
                            f4.write(s)
                        with open(namea, "a") as f3:
                            f3.write(s)
                        with open(name, "rb") as binary_file:
                            data = binary_file.read()
                            lenf1=len(data)
                            #if lenf1<400000:
                                #print("This file is too small");
                                #raise SystemExit
                            s=str(data)
                            lenf=len(data)
                        sda=bin(int(binascii.hexlify(data),16))[2:]
                        szx=""
                        lenf=len(sda)
                        xc=8-lenf%8
                        z=0
                        if xc!=0:
                            if xc!=8:
                                while z<xc:
                                    szx="0"+szx
                                    z=z+1
                        sda=szx+sda     
                        lenf=len(sda)
                        szx=""
            
                        for byte in sda:
                            aqwer=aqwer+1
                            aqwers=aqwers+1
                            qwaw=qwaw+byte
                            qwaw1=qwaw1+byte
                            
                                    
                            if aqwer<=bitc:
                                qwt=qwt+byte
                            if aqwer==bitc:
                                qwaw1=""
                                xx3=xx3+1
                                aqwq=int(qwt,2)
                                qwt=""
                                a=a+1
                                h=h+1  
                            av=bin(aqwq)
                            if a<=block and aqwer==bitc:
                                aqwer=0
                                m[aqwq] = aqwq
                                numbers.append(aqwq)  
                            if a == block:
                                
                                p=0
                                while p<blockw1:
                                    if p!=m[p]:
                                        k.append(p)     
                                    p=p+1
                                lenfg=len(k)
                                
                                if lenfg==0:
                                    xx=0

                                    wer="01111111"+sda
                                    lenf=len(wer)
                                    xc=8-lenf%8
                                    z=0
                                    if xc!=0:
                                        if xc!=8:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                    wer=wer+szx
                                    lenf=len(szx)                      
                                    szx=""        
                                    wer="0b"+wer
                                    n = int(wer, 2)
                                    qqwslenf=len(wer)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    with open(namea, "ab") as f2ww:             
                                        f2ww.write(jl)
                                        x2 = time()
                                        x3 = x2-x
                                        return print(x3)

                                    
                                if lenfg>0:
                                    acvb=lenfg-1
                                    ss=0
                                    ww=0
                                   
                                    acvb=lenfg-1
                                    notexist=k[0]
                                    
                                   
                                    
                                    if notexist>16383 or notexist<0:
                                        wer="01111111"+sda
                                     
                                        lenf=len(szx)                      
                                        szx=""        
                                        wer="0b"+wer
                                        n = int(wer, 2)
                                        qqwslenf=len(wer)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        sssssw=len(jl)
                                        with open(namea, "ab") as f2ww:             
                                            f2ww.write(jl)
                                            
                                            x2 = time()
                                            x3 = x2-x
                                            return print(x3)

                                        
                                        
                                        
                                       
                                    else:
                                        xx=1
                                        szx=bin(notexist)[2:]
                                        lenf=len(szx)
                                        
                                            
                                        
                                        xc=14-lenf
                                            
                                        z=0
                                        if xc!=0 and lenf!=14:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                        takebitdw2=int(szx, 2)
                                        
                                        szxw1=""
                                        szxw1=szx
                                        
                                        lenf=len(szx)
                                        
                                       
                                        szx=""  
                                        if lenfg==0:
                                            wer="01111111"+sda
                                            lenf=len(wer)
                                    
                                            lenf=len(szx)                      
                                            szx=""        
                                            wer="0b"+wer
                                            n = int(wer, 2)
                                            qqwslenf=len(wer)
                                            qqwslenf=(qqwslenf/8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)
                                            with open(namea, "ab") as f2ww:             
                                                f2ww.write(jl)
                                                jls=jl
                                                x2 = time()
                                                x3 = x2-x
                                                return print(x3)

                                b=-1
                                kl=blockw+1
                                bnkw=16383**(kl)
                                
                                
                                
                                cb=0        
                                er=-1
                                ghj=0
                                ghjd=1
                                bnk=1
                                p=0
                                cvz=0
                                if xx==1:
                                    
                                    for p in range(blockw+1):
                                        if lenfg>0:
                                            if 16383!=byteb:
                                                byteb=numbers[p]
                                                
                                                ghj=byteb
                                            if 16383==byteb:
                                                byteb=notexist
                                                
                                                ghj=byteb
                                                #print(ghj)
                                                #os.system("pause")
                                        qfl=qfl+1
                                        ghjd=ghj
                                        bnk=1
                                        
                                        bnkd=1        
                                        kl=kl-1
                                                
                                                
                                                
                                                  
                                        if lenfg>0:
                                                    
                                            bnkw=bnkw//16383
                                            #print(bnkw)
                                            #os.system("pause")
                                           
                                            
                                        
                                                        
                                                
            
                                            ghjd=0
                                            ghjd=ghj*bnkw
                                            #print(ghj)
                                                    
                                        cvz=cvz+ghjd
                                                
                                    
                                    bnkw=1023**(kl)
                                    
                                    szx=bin(cvz)[2:]
                                    cvz=0
                                    lenf=len(szx)
                                   
                                   
                                    
                                    
                                    
                                    if lenfg>0:
                                        if lenf>blockD:
                                            wer="01111111"+sda
                                            lenf=len(wer)
                                      
                                            lenf=len(szx)                      
                                            szx=""        
                                            wer="0b"+wer
                                            n = int(wer, 2)
                                            qqwslenf=len(wer)
                                            qqwslenf=(qqwslenf/8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)
                                            with open(namea, "ab") as f2ww:             
                                                f2ww.write(jl)
                                                
                                                x2 = time()
                                                x3 = x2-x
                                                return print(x3)
                                        xc=blockD-lenf
                                        z=0
                                        if xc!=0 and lenf!=blockD:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                        
                                        if xx==1:  
                                            wer=wer+szx+szxw1
                                            szxw1=""
                                       
                                            
                                        
            
                                    
                                        lenf=len(szx)
                                        
                                        szx=""
                                
                                
                                        
                                qwaw=""
                                
                                a=0
                                numberschangenotexist = []    
                                del k[:]     
                                del numbers[:]
                                m = []
                                b=0
                                while b<blockw1:
                                    m+=[-1]
                                    b=b+1
                                b=0
                                        
                        a=0
            
                        wer=wer+qwaw
                        qwaw=""
            
            
                        wer="1"+wer+"1"
                        lenf=len(wer)
                        xc=8-lenf%8
                        z=0
                        if xc!=0:
                            if xc!=8:
                                while z<xc:
                                    szx="0"+szx
                                    z=z+1
                        wer=wer+szx
                        lenf=len(szx)                      
                        szx=""        
                        wer="0b"+wer
                        n = int(wer, 2)
                        qqwslenf=len(wer)
                        qqwslenf=(qqwslenf/8)*2
                        qqwslenf=str(qqwslenf)
                        qqwslenf="%0"+qqwslenf+"x"
                        jl=binascii.unhexlify(qqwslenf % n)
                        sssssw=len(jl)
                        with open(namea, "ab") as f2ww:             
                            f2ww.write(jl)
                            
                            x2 = time()
                            x3 = x2-x
                            return print(x3)


    def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2
                    
                    #import mpmath as m
                    #m.mp.dps = 100000
                    #PI=4 * m.atan(1)

                    spin=0
                    c=0
                    A=0
                    Spin=0
                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    name = input("What is name of file? ")
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=7
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sda5=""
                    sda6=""
                    sda7=""
                    sda8=""
                    sda9=""
                    sda11=""
                    sda12=""
                    
                    sda14=""
                    sdaB=""
                    D=0

                    block=1
                    block2=0
                    block3=0
                    
                    count=0
                    
                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        
                        END_working=0
                        Circle_times2=0
                        ii=0
                        sda20=""
                        
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1

                            with open(nameas, "ab") as f2:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**32)-1:
                                        raise SystemExit
                                        
                                    if lenf7<=82:
                                        raise SystemExit 
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:

                                    lenf5=len(sda2)

                                    block2=0
                                    ei4=0
                                    ei5=1

                                    
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    Spin3=0

                                    Spin2=0
                                    #Extract
                                    
                                    
                                    s=""

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""
                                    sda8=""
                                    sda9=""
                                    sda17=""
                                    Bytes_row4=""
                                    sda19=""
                                    
                                    ei=0

                                    if Circle_times2==0:
                                           
                                           g=1

                                    if g==1:

                                        if sda2[lenf5-8:lenf5]=="10000000":

                                            sda2=sda2[1:lenf5-8]

                                        elif sda2[lenf5-7:lenf5]=="1000000":

                                            sda2=sda2[1:lenf5-7]

                                        elif sda2[lenf5-6:lenf5]=="100000":

                                            sda2=sda2[1:lenf5-6]

                                        elif sda2[lenf5-5:lenf5]=="10000":

                                            sda2=sda2[1:lenf5-5]


                                        elif sda2[lenf5-4:lenf5]=="10000":

                                            sda2=sda2[1:lenf5-4]

                                        elif sda2[lenf5-3:lenf5]=="100":

                                            sda2=sda2[1:lenf5-3]

                                        elif sda2[lenf5-2:lenf5]=="10":

                                            sda2=sda2[1:lenf5-2]

                                        elif sda2[lenf5-1:lenf5]=="1":

                                            sda2=sda2[1:lenf5-1]

                                    sda3=sda2

                                    lenf6=len(sda3)
                        
                                    count_times4=0

                                    FF=len(sda3)
                                    
                                    sda17=""
                                    sda19=""
                                    
                                    sda3=sda2
                                    Spin=0
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""
                                    sda17=""

                                    ei=0
 
                                    lenf6F=lenf6

                                    ei=0

                                    while ei<lenf6F:

                                           sda9=sda3[ei:ei+1]
                                           sda12=sda3[ei:ei+2]
                                           sda18=sda3[ei:ei+34]
                                           lenf2=len(sda18)

                                           
                                           
                                           


                                           if sda12[0:2]=="00":
                                                         sda10=sda3[ei:ei+34]
                                                         sda10=sda10[2:]
                                                         sda17=sda17+sda10
                                                         ei=ei+34


                                           if sda12[0:2]=="01":

                                                         sda10=sda3[ei:ei+17]

                                                         sda10=sda10[2:]

                                                         lenf1=len(sda10)

                                                         N1 = int(sda10, 2)

                                                         lenf2=len(sda10)
                                                         
                                                           

                                                           

                                                         #32 bit 33 bit 31 bit

                                                         #print(sda10)
                                                         PI_take=str(PI)

                                                        

                                                        
                                                         N3 = PI_take[N1:N1+3]
                                                         N3=int(N3)
                                                         
                                                         N4=bin(N3)[2:]
                                                         
                                                         N7=len(N4)
                                                         
                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=32-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=32:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         
                                                        
                                                         sda17=sda17+szx2+N4
                                                         ei=ei+17
                                                         
                                           if sda12[0:2]=="11":

                                                         sda10=sda3[ei:ei+31]

                                                         sda10=sda10[2:]


                                                         lenf1=len(sda10)

                                                         N1 = int(sda10, 2)
                                                         

                                                        
                                                         N4=bin(N1)[2:]

                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=32-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=32:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         
                                                        
                                                         sda17=sda17+szx2+N4
                                                         ei=ei+31
                                                         
                                           if sda12[0:2]=="10":

                                                         sda10=sda3[ei:ei+25]

                                                         sda10=sda10[2:]

                                                         lenf1=len(sda10)

                                                         N1 = int(sda10, 2)

                                                         lenf2=len(sda10)
                                                         
                                                           

                                                           

                                                         #32 bit 33 bit 31 bit

                                                         #print(sda10)
                                                         PI_take=str(PI)

                                                        

                                                        
                                                         N3 = PI_take[N1:N1+5]
                                                         N3=int(N3)
                                                         
                                                         N4=bin(N3)[2:]
                                                         
                                                         N7=len(N4)
                                                         
                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=32-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=32:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         
                                                        
                                                         sda17=sda17+szx2+N4
                                                         ei=ei+25
                                                         

                                                         

                                           
                                           
                                                  
                                    Circle_times2=Circle_times2+1
                                    
                                    if   Circle_times2==1:
                                         #print(sda17)
                                       
                                         n = int(sda17, 2)
                                         qqwslenf=len(sda17)
                                         qqwslenf=(qqwslenf/8)*2
                                         qqwslenf=str(qqwslenf)
                                         qqwslenf="%0"+qqwslenf+"x"
                                         jl=binascii.unhexlify(qqwslenf % n)
                                         sssssw=len(jl)

                                         szxzzza=""
                                         szxzs=""
                                            
                                         f2.write(jl)
                                         x2 = time()
                                         x3=x2-x
                                         return print(x3)
                                        
                                if i==1:

                                    sda17=""
                                    sda19=""
                                    
                                    sda3=sda2
                                    Spin=0
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""

                                    ei=0
 
                                    lenf6F=lenf6

                                    ei=0

                                    while ei<lenf6F:

                                           sda10=sda3[ei:ei+32]#32 bit 33 bit 31 bit

                                           
                                           lenf1=len(sda10)

                                           N1 = int(sda10, 2)

                                           lenf2=len(sda10)

                                           N4=N1

                                           
                                           N1=str(N1)
                                           PI_take=str(PI)

                                           N3 = PI_take.find(N1)
                                           N6=str(N3)
                                           N5=len(N6)
                                           
                                           N7=len(N1)
                                           



                                           if lenf2!=32:
                                                  sda17=sda17+"00"+sda10


                                         
                                                  
                                          
                                        
                                           elif lenf2==32  and N7==3 and N5==3 and N3>=0:
                                                         N4=bin(N3)[2:]
                                                         

                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=15-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=15:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         
                                                         sda17=sda17+"01"+szx2+N4

                                               
                                                         
                                           elif lenf2==32  and N7==5 and N5==5 and N3>=0:

                                                         N4=bin(N3)[2:]
                                                         

                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=23-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=23:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         sda17=sda17+"10"+szx2+N4


                                           else:

                                                  if N4<=(2*29)-1 and lenf2==32:

                                                             N4=bin(N4)[2:]

                                                             lenf=len(N4)
                                                                     
                                                             szx2=""
                                                             xc=29-lenf
                                                             z=0
                                                             if xc!=0:
                                                                   if xc!=29:
                                                                          while z<xc:
                                                                                 szx2="0"+szx2
                                                                                 z=z+1
                                                             sda17=sda17+"11"+szx2+N4
                                                  else:
                                                     sda17=sda17+"00"+sda10

                                                         


                                           ei=ei+32
                                                  
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    
                                    Spinh=0              
                                    block2=0
                              
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    sda2=sda17
                                   

                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        
                                        Circle_times2=Circle_times2+1

                                        lenf9=len(sda17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==1:
                                            #print(lenf6-1)

                                            
                                            sda17="1"+sda17+"1"
                                            
                                            lenf=len(sda17)
                                            
                                            szx=""
                                            xc=8-lenf%8
                                            z=0
                                            if xc!=0:
                                                if xc!=8:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1

                                            lenf=len(sda17)
                                            B3=""

                                                                                      

                                            sda17=sda17+szx
                                            

                                            n = int(sda17, 2)
                                            qqwslenf=len(sda17)
                                            qqwslenf=(qqwslenf//8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                              
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)

                                            Speed=0

                                            if x3!=0:

                                                   Speed=(lenf7//xs)#B/s
                                                   print(Speed)
                                                   print("B/s")

                                            if x3==0:
                                                   print("FAST")

                                            return print(x3)



d=compression()

xwc3=d.Areacu2()
print(xwc3)

xwc2=d.Areac2()
print(xwc2)

xw=d.cryptograpy_compression4()
print(xw)
