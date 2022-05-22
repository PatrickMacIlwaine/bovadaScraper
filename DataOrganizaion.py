#Work in progress....




# data orginization
baseline = 100
for i in range(len(chunked_list)):

    if chunked_list[0][1] == 0 or chunked_list[0][3] == 0:
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
        lowerA = float(AligulacList[i][1])
        namelowerA = AligulacList[i][0]
        higherA = float(AligulacList[i][3])
        namehigher = AligulacList[i][2]
        if lowerA > float(AligulacList[i][3]):
            lowerA = float(AligulacList[i][3])
            namelowerA = AligulacList[i][2]
            higherA = float(AligulacList[i][1])
            namehigherA = AligulacList[i][0]

        # Bovada prob of non favored player winning
        BPNFW = lower
        # Bovad prob favored player winning
        BPFW = higher
        # actuall prob of non favored player winning
        PNFW = lowerA
        # amount won non favored wins
        AWNFW = (baseline * ip_to_decimal(BPNFW) / 100) - baseline
        # amount won favored player wins
        try:
            AWFW = (baseline * ip_to_decimal(BPFW) / 100) - baseline
        except:
            print("fail!")
        # Actuall prob of loss non favored player
        PNFL = higherA
        # amount loss
        AML = -baseline

        eNONFAVORED = (PNFW * AWNFW) + (PNFL * AML)

        eFAVORED = (PNFL * AWFW) + (PNFW * AML)

        if eNONFAVORED > 0:
            print(" e non favored > 0 ")
        if eFAVORED > 0:
            print("e favored > 0")
        if eFAVORED == 0:
            print("e favored = 0 ")
        if eNONFAVORED == 0:
            print("e non favored = 0 ")
