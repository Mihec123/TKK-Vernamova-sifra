
def preberi(file):
    """prebere tekst in odstrani vse znake ki nosi crke, ter zapise vse z malo"""
    text = ""
    with open(file, 'r') as f:
            for vrstica in f:
                text += ''.join([i for i in vrstica if i.isalpha()]).lower()
    return text

def frekvenca(besedilo):
    i = 0
    slovar = {}
    for i in range(len(besedilo)-1):
        kljuc = besedilo[i] + besedilo[i+1]
        if kljuc in slovar:
            slovar[kljuc] += 1
        else:
            slovar[kljuc] = 1
    return slovar

besedilo = preberi("blackcat.txt")
frekvence = frekvenca(besedilo)
print(frekvence)

            
