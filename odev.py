from docx import *
import docx.package
import docx.parts.document
import docx.parts.numbering
import logging

logging.basicConfig(filename="tez.log", format='%(asctime)s %(message)s', filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def main(filename):
kontrolEt= false    
dosyadenenecek= (Documentdosyaadi+'.docx')
 kontroledilecekpag= dosyaadi.dosyadenenecek
Aranacak=dosyadenenecek.text.lower()
Paragraf=dosyadenenecek.text
    tekrarlanandosya = 0
    liste =  list()
    Onsozsayi = 0
    ProgramCalistir(kontrolEt,dosyadenenecek,kontroledilecekpag,tekrarlanandosya,KontrolDizisi,Onsozsayi)
    Kaynakca_Kontrol(kaynakca,dosyadenenecek):
if __name__ == "__main__":
    dosyaAdi = input('Dosya Girişi.')
    main(dosyaAdi)



def  Program(kontrolEt,dosyadenenecek,kontroledilecekpag,tekrarlanandosya,KontrolDizisi,Onsozsayi):
   for sayi,dosyadenenecek in enumerate(dosyadenenecek):
        if 'Özgeçmiş' == kontroledilecekpag.text:
            kontrolEt = False       
        elif 'Kaynak' in kontroledilecekpag.text:
            kontrolEt = True
        elif 'Ön Söz' == Paragraf:
            Onsozsayi = sayi
        if kontrolEt and kontroledilecekpag.text != '' and '[' in Paragraf:
            liste+(Aranacak.strip())
        elif sayi == Onsozsayi + 1:
            if 'teşekkür' in Aranacak:
                logging.info('Önsöz tarandı Teşekkür ifadesi mevcut')
        if '“' in Paragraf:
            if len(dosyadenenecek.split('“')[1].split('”')[0].split(' ')) > 50:
                logging.info('{} ile başlayan paragraf {} kelime.'.format(Paragraf.split(' ')[0] + ' ' + Paragraf.split(' ')[1] + ' ' +Paragraf.split(' ')[2],len(Paragraf.split('“')[1].split('”')[0].split(' '))))



def Kaynakca_Kontrol(kaynakca,dosyadenenecek):
    dokumanturleri = ['ve','pp.','ss.','of','by','and','in','the','cilt']
    for satir,kaynakcasatiri in enumerate(kaynakca,1):
        kaynakno = int(kaynaksatiri.split('[')[1].split(']')[0])
        if satir != kaynakno:
            logging.info('{} Kaynakça Bulunamadi.)
        for kelime in kaynakcasatiri.split(' '):
            if kelime[0] != '(' and not (kelime.replace('[{}]'.format(satir),'').strip()[0].isupper() or kelime.replace('[{}]'.format(satir),'').strip()[0].isnumeric() or kelime in kaynakca_pass):
                logging.info('{} Numaralı kaynakçada format hatası. {} kelimesi küçük harf'.format(kaynakca_no,kelime))
        kontrol = True
        for paragraph in dosyadenenecek:
            if 'Kaynaklar' in Paragraf:
                break
            if '[{}]'.format(kaynakno) in Paragraf:
                kontrol = False
                break
        if kontrolEt:
            logging.info('Kaynakça tezde bulunmadı')

    KaynakKontrol(liste,dosyadenenecek)

