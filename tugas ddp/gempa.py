class Gempa:
    lokasi = ''
    skala = ''
    dampak = ''

    def _init_(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        self.dampak = ''

    def Dampak(self):
        if(self.skala <= 2):
            self.dampak = 'Tidak berasa'
        elif(self.skala >= 2 and self.skala < 4):
            self.dampak = 'Bangunan Retak'
        elif(self.skala >= 4 and self.skala < 6):
            self.dampak = 'Bangunan Ambruk'
        elif(self.skala >= 6):
            self.dampak = 'Berpotensi Tsunami'

    def cetak(self):
        print(
            '\n---------------------',
            '\nLokasi:',self.lokasi,
            '\nSkala:',self.skala,
            '\nDampak:',self.dampak,
            '\n----------------------'
            )