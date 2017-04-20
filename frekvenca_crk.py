
def preberi(file):
    """prebere tekst in odstrani vse znake ki nosi crke, ter zapise vse z malo"""
    text = ""
    with open(file, 'r') as f:
            for vrstica in f:
                text += ''.join([i for i in vrstica if i.isalpha()]).lower()
    return text

def frekvenca(besedilo):
    """presteje stevilo ponovitev dveh zaporednih crk v besedilu
    in jih na koncu deli z dolzino besedila"""
    i = 0
    slovar = {}
    dol = len(besedilo)
    for i in range(dol-1):
        kljuc = besedilo[i] + besedilo[i+1]
        if kljuc in slovar:
            slovar[kljuc] += 1
        else:
            slovar[kljuc] = 1
    for kljuc in slovar:
        slovar[kljuc] = slovar[kljuc] / dol 
    return slovar

besedilo = preberi("blackcat.txt")
frekvence = frekvenca(besedilo)
print(frekvence)

            
