import frekvenca_crk as fc

abeceda_to_int = dict([(chr(i),i-97) for i in range(97,123)])
abeceda_to_str = dict([(i-97,chr(i)) for i in range(97,123)])

def razlika(kriptogram, kljuc):
    """danemu kriptogramu odsteje kljuc po modulo 26"""
    besedilo = ""
    if len(kriptogram) == len(kljuc):
        for i in range(len(kljuc)):
            besedilo += abeceda_to_str[(abeceda_to_int[kriptogram[i]] - abeceda_to_int[kljuc[i]]) % 26 ]
    return besedilo

def verjetnost(kljuc,kriptogrami,porazdelitev,minimum = pow(10,-80)):
    """izracuna verjetnost kljuca glede na dano porazdelitev parov crk porazdelitev je
    slovar parov crk in verjetnosti da ti nastopata skupaj"""
    verjetnost = 1
    besedilo0 = razlika(kriptogrami[0],kljuc)
    besedilo1 = razlika(kriptogrami[1],kljuc)
    besedilo2 = razlika(kriptogrami[2],kljuc)
    for i in range(len(kljuc)-1):
        bes0 = besedilo0[i] + besedilo0[i+1]
        bes1 = besedilo1[i] + besedilo1[i+1]
        bes2 = besedilo2[i] + besedilo2[i+1]
        if bes0 not in porazdelitev:
            verjetnost = 0
            return verjetnost
        elif bes1 not in porazdelitev:
            verjetnost = 0
            return verjetnost
        elif bes2 not in porazdelitev:
            verjetnost = 0
            return verjetnost
        else:
            verjetnost = verjetnost * porazdelitev[bes0] * porazdelitev[bes1] * porazdelitev[bes2]
    if verjetnost < minimum:
        verjetnost = 0
    return verjetnost

#test
#verjetnost("aa",["ba","ah","bb"],{"ab":0.17,"ah":0.02,"ba":0.03,"bb":0.02,"ha":0.71,"hb":0.01,"hh":0.04})
#rezultat mora bit 12*10^-6

kripto1 = "BLIBIPHJBQYZB".lower()
kripto2 = "ZIPNAQPVDUCFB".lower()
kripto3 = "ELEWIKIXOSZFM".lower()

besedilo = fc.preberi("blackcat.txt")
poraz = fc.frekvenca(besedilo)

slovar = {}
stevec = 0


for a in range(26):
    for b in range(26):
        kljuc_temp = abeceda_to_str[a] + abeceda_to_str[b]
        if verjetnost(kljuc_temp,[kripto1[0:2],kripto2[0:2],kripto3[0:2]],poraz, pow(10,-7)) == 0:
            continue
        for c in range(26):
            kljuc_temp = abeceda_to_str[b] + abeceda_to_str[c]
            if verjetnost(kljuc_temp,[kripto1[1:3],kripto2[1:3],kripto3[1:3]],poraz,pow(10,-7)) == 0:
                continue
            for d in range(26):
                kljuc_temp = abeceda_to_str[c] + abeceda_to_str[d]
                if verjetnost(kljuc_temp,[kripto1[2:4],kripto2[2:4],kripto3[2:4]],poraz,pow(10,-7)) == 0:
                    continue           
                for e in range(26):
                    kljuc_temp = abeceda_to_str[d] + abeceda_to_str[e]
                    if verjetnost(kljuc_temp,[kripto1[3:5],kripto2[3:5],kripto3[3:5]],poraz,pow(10,-7)) == 0:
                        continue
                    for f in range(26):
                        kljuc_temp = abeceda_to_str[e] + abeceda_to_str[f]
                        if verjetnost(kljuc_temp,[kripto1[4:6],kripto2[4:6],kripto3[4:6]],poraz,pow(10,-7)) == 0:
                            continue
                        for g in range(26):
                            kljuc_temp = abeceda_to_str[f] + abeceda_to_str[g]
                            if verjetnost(kljuc_temp,[kripto1[5:7],kripto2[5:7],kripto3[5:7]],poraz,pow(10,-7)) == 0:
                                continue                            
                            for h in range(26):
                                kljuc_temp = abeceda_to_str[g] + abeceda_to_str[h]
                                if verjetnost(kljuc_temp,[kripto1[6:8],kripto2[6:8],kripto3[6:8]],poraz,pow(10,-7)) == 0:
                                    continue                                
                                for i in range(26):
                                    kljuc_temp = abeceda_to_str[h] + abeceda_to_str[i]
                                    if verjetnost(kljuc_temp,[kripto1[7:9],kripto2[7:9],kripto3[7:9]],poraz,pow(10,-7)) == 0:
                                        continue  
                                    for j in range(26):
                                        kljuc_temp = abeceda_to_str[i] + abeceda_to_str[j]
                                        if verjetnost(kljuc_temp,[kripto1[8:10],kripto2[8:10],kripto3[8:10]],poraz,pow(10,-7)) == 0:
                                            continue                                          
                                        for k in range(26):
                                            kljuc_temp = abeceda_to_str[j] + abeceda_to_str[k]
                                            if verjetnost(kljuc_temp,[kripto1[9:11],kripto2[9:11],kripto3[9:11]],poraz,pow(10,-7)) == 0:
                                                continue                                               
                                            for l in range(26):
                                                kljuc_temp = abeceda_to_str[k] + abeceda_to_str[l]
                                                if verjetnost(kljuc_temp,[kripto1[10:12],kripto2[10:12],kripto3[10:12]],poraz,pow(10,-7)) == 0:
                                                    continue                                                 
                                                for m in range(26):
                                                    kljuc = abeceda_to_str[a] + abeceda_to_str[b] + abeceda_to_str[c] + abeceda_to_str[d] + abeceda_to_str[e] \
                                                    + abeceda_to_str[f] + abeceda_to_str[g] + abeceda_to_str[h] + abeceda_to_str[i] + abeceda_to_str[j] \
                                                    + abeceda_to_str[k] + abeceda_to_str[l] + abeceda_to_str[m]
                                                    ver = verjetnost(kljuc,[kripto1,kripto2,kripto3],poraz)
                                                    if ver > 0:
                                                        print(kljuc)
                                                        slovar[kljuc]=ver
                                                        
                                                    
    
    
    
    
    

