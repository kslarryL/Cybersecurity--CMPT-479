
import sys



def convert_to_binary(target,lenth):
    res = [None] * lenth
    for i in range(lenth):
        if target & (1<<i):
            res[i] = '1'
        else:
            res[i] = '0'
    return res



def xor_bits(gen1,gen2):
    res = [None] * len(gen1)
    for i in range(len(gen1)):
        res[i] = str(int(gen1[i]) ^ int(gen2[i]))
    return res


def run():
    inputStr = sys.argv[1]

    bits = []

    # generate bits
    for c in inputStr:
        charBits = '{0:08b}'.format(ord(c))
        for b in charBits:
            bits.append(b)

    # calculate parity bit number
    parityBitNum = 0

    checkLength = True
    strBitLength = len(bits)
    while checkLength:
        total = strBitLength + parityBitNum
        if total > 2**(parityBitNum-1) and total < 2**parityBitNum:
            checkLength = False
        else:
            parityBitNum +=1


    # parity bit placement
    encodeBits = [None] * (parityBitNum + strBitLength)
    placeIndex = 0
    for i in range(len(encodeBits)):
        if i+1>0 and (i+1 & (i+1 - 1)) == 0:
            encodeBits[i] = None
        else:
            encodeBits[i] = bits[placeIndex]
            placeIndex+=1

    # fill parity bits
    
    gen1 = [None] * parityBitNum

    for i in range (len(encodeBits)-1,-1,-1):
        if encodeBits[i]!='1':
            continue
        
        tarIndex = i
        gen1 = convert_to_binary(tarIndex+1,parityBitNum)
        break

    
    for j in range(tarIndex-1,-1,-1):
        if encodeBits[j]!='1':
            continue

        gen2 = convert_to_binary(j+1,parityBitNum)

        gen1 = xor_bits(gen1,gen2)

    print(''.join(gen1))
        
    

if __name__ == "__main__":
    run()
