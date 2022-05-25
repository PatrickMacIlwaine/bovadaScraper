# Work in progress....
import bovadaAligulacCollecion
from bovadaAligulacCollecion import *

chunked_list = bovadaAligulacCollecion.get_chunked_list()
aligulac_list = bovadaAligulacCollecion.get_aligulac_list()
baseline = 100
for i in range(len(chunked_list)):

    if aligulac_list[0][1] == 0 or aligulac_list[0][3] == 0:
        print("Player not in database = 0")

    else:

        lower = float(chunked_list[i][1])
        namelower = chunked_list[i][0]
        higher = float(chunked_list[i][3])
        namehigher = chunked_list[i][2]
        if lower > float(chunked_list[i][3]):
            lower = float(chunked_list[i][3])
            namelower = chunked_list[i][2]
            higher = float(chunked_list[i][1])
            namehigher = chunked_list[i][0]
        # aligulac
        lowerA = float(aligulac_list[i][1])
        namelowerA = aligulac_list[i][0]
        higherA = float(aligulac_list[i][3])
        namehigherA = aligulac_list[i][2]
        if lowerA > float(aligulac_list[i][3]):
            lowerA = float(aligulac_list[i][3])
            namelowerA = aligulac_list[i][2]
            higherA = float(aligulac_list[i][1])
            namehigherA = aligulac_list[i][0]
        print("Bovada")
        print(lower)
        print(namelower)
        print(higher)
        print(namehigher)
        print("Aligulac")
        print(lowerA)
        print(namelowerA)
        print(higherA)
        print(namehigherA)

        # Bovada prob of non favored player winning
        BPNFW = lower
        # Bovad prob favored player winning
        BPFW = higher
        # actuall prob of non favored player winning
        PNFW = lowerA
        # amount won non favored wins
        AWNFW = (baseline * ip_to_decimal(BPNFW)) - 100
        # amount won favored player wins
        try:
            AWFW = (baseline * ip_to_decimal(BPFW)) - 100
        except:
            print("fail!")
        # Actuall prob of loss non favored player
        PNFL = higherA
        # amount loss
        AML = -baseline

        eNONFAVORED = (PNFW * AWNFW) + (PNFL * AML)
        print(AWNFW)

        print(PNFL, AWFW, PNFW, AML)
        eFAVORED = (PNFL * AWFW) + (PNFW * AML)
        print(eFAVORED)
        if eNONFAVORED >= 0:
            print(" e non favored > 0 ")
        if eFAVORED >= 0:
            print("e favored > 0")
        if eFAVORED == 0:
            print("e favored = 0 ")
        if eNONFAVORED == 0:
            print("e non favored = 0 ")
