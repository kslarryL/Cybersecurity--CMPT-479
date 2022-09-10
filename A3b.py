
import sys



def convert_to_binary(target,lenth):
    res = [None] * lenth
    for i in range(lenth):
        if target & (1<<i):
            res[i] = '1'
        else:
            res[i] = '0'
    return res

def list2Str(list2):
    res = ''
    for i in range(len(list2)):
        res = res + list2[i]
    
    return res

def asciiBitToStr(list):
    
    res = list2Str(list)
    asc = int(res, 2)
    character = chr(asc)
    return character

def xor_bits(gen1,gen2):
    res = [None] * len(gen1)
    for i in range(len(gen1)):
        res[i] = str(int(gen1[i]) ^ int(gen2[i]))
    return res


def run():
    parityBits = sys.argv[1]
    inputStr = sys.argv[2]


    bits = []

    # generate bits
    for c in inputStr:
        charBits = '{0:08b}'.format(ord(c))
        for b in charBits:
            bits.append(b)
    



    # calculate parity bit number
    totalLength = len(bits) + len(parityBits)

    preBits = [None] * totalLength


    parityIndex = 0
    preBitIndex = 0

    for i in range(totalLength):
        if i+1>0 and (i+1 & (i+1 - 1)) == 0:
            preBits[i] = parityBits[parityIndex]
            parityIndex+=1
        else:
            preBits[i] = bits[preBitIndex]
            preBitIndex+=1
    

    res = [None] * len(parityBits)

    for i in range(totalLength-1,-1,-1):
        if preBits[i]=='1':
            bigIndex = i
            break
    
    res = convert_to_binary(bigIndex+1,len(parityBits))

    for j in range(bigIndex-1,-1,-1):
        if preBits[j]!='1':
            continue
        gen2 = convert_to_binary(j+1,len(parityBits))

        res = xor_bits(res,gen2)
    
 
    needProcess = True

    for i in range(len(res)):
        if res[i]=='1':
            needProcess = False
            break

    if not needProcess:
        errorBit = ''

        for i in range(len(parityBits)):
            errorBit = errorBit + res[i]
        
        posNum = int(errorBit,2)

        if preBits[posNum-1] =='0':
            preBits[posNum-1] = '1'
        else:
            preBits[posNum-1] = '0'

        genParity = list(parityBits)
        gpIndex =0
        genEncodeBits = preBits
        gbIndex =0

        for i in range(totalLength):
            if i+1>0 and (i+1 & (i+1 - 1)) == 0:
               genParity[gpIndex] = preBits[i]
               gpIndex+=1
            else:
                genEncodeBits[gbIndex] = preBits[i]
                gbIndex+=1


        # convert genParity to string
        genParityStr = ''
        for i in range(len(genParity)):
            genParityStr = genParityStr + genParity[i]

        newStr = ""

        for i in range(int(len(preBits)/8)):
            char = asciiBitToStr(genEncodeBits[i*8:i*8+8])
            newStr = newStr + char
        print(genParityStr)
        print(newStr)

    

        

        
    
        
    

if __name__ == "__main__":
    run()
