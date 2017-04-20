# TKK-Vernamova-sifra
Programerska domaca naloga pri predmetu TKK

Naloga. Prestregli ste naslednje tri kriptograme:

c1 = BLIBIPHJBQYZB 
c2 = ZIPNAQPVDUCFB 
c3 = ELEWIKIXOSZFM 

Šifrirano besedilo je v vseh treh primerih angleško, brez ločil in presledkov, pri šifriranju vseh treh besedil je bil uporabljen isti ključ. Šifriranje poteka v grupi Z26 (A->0,B->1,...,z->25) tako, da se besedilu prišteje naključno generiran ključ (vsi ključi so enako verjetni) enake dolžine kot besedilo. Dešifrirajte vsa tri besedila. 

Nasvet: pomagajte si s frekvencami digramov v tipičnem angleškem tekstu. Dovolj dober približek lahko generirate sami s pomočjo primernega besedila, npr. iz besedila blackcat, v katerem odstranite vse znake, ki niso črke. Najbolj verjetne ključe izmed 26^2 za vsak digram posebej (torej znaka 12, 23, 34, 45,...) potem izračunate s pogojno verjetnostjo. Izmed več predlaganih besedil potem izberete tista, ki so smiselna. Bodite pozorni na to, da v Z26 seštevanje ni enako odštevanju.
