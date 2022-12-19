from gempa import Gempa

gempaBanten = Gempa('Banten',1.2)
gempaPalu = Gempa('Palu',6.1)
gempaCianjur = Gempa('Cianjur',5.6)
gempaJayapura = Gempa('Jayapura',3.3)
gempaGarut = Gempa('Garut',4.0)

gempaBanten.Dampak()
gempaPalu.Dampak()
gempaCianjur.Dampak()
gempaJayapura.Dampak()
gempaGarut.Dampak()

gempaBanten.cetak()
gempaPalu.cetak()
gempaCianjur.cetak()
gempaJayapura.cetak()
gempaGarut.cetak()