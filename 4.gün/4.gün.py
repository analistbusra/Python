
sayılar= 's' # tek bir karakter ile dize olabilir.
print(sayılar)  # s
print(len(sayılar))# 1
mesaj='Python Dünyasına Hoş Geldiniz!'# tek tırnakla dize oluşturdum
print(mesaj) #Python Dünyasına Hoş Geldiniz!
print(len(mesaj))#30
#uzun bir cümleyi tek tırnak dize şeklinde yazalım.
cümle='Python programını öğrendiğim için çok mutluyum.'

"""
print(cümle)#Python programını öğrendiğim için çok mutluyum.

"""

uzun_cümle=''' Ben bir istatistikçiyim aslında 
bu tam bana göre bir meslek çocukluğumdan beri 
sürekli gözlem yaparak etrafımda olup bitenleri 
tahmin etmeye çalışırdım.'''
print(uzun_cümle)
Ben bir istatistikçiyim aslında 
bu tam bana göre bir meslek çocukluğumdan beri 
sürekli gözlem yaparak etrafımda olup bitenleri 
tahmin etmeye çalışırdım.

uzun_cümle=""" Ben bir istatistikçiyim aslında 
bu tam bana göre bir meslek çocukluğumdan beri 
sürekli gözlem yaparak etrafımda olup bitenleri 
tahmin etmeye çalışırdım."""
print(uzun_cümle)

ad='büşra'
meslek='istatistikçi'
boş= " "
AD_MESLEK= ad + boş + meslek
print(AD_MESLEK)#büşra istatistikçi


ad='büşra'
meslek='istatistikçi'
boş= " "
AD_MESLEK= ad + boş + meslek
print(AD_MESLEK)
print(len(AD_MESLEK))#18
print(len(meslek))#12
print(len(meslek)>len(ad))#True


print ( 'Umarım herkes rahatlıkla kod yazabiliyor \n Öyle mi?' ) 
Umarım herkes rahatlıkla kod yazabiliyor 
 Öyle mi?

print('il\tölüm sayısı\tVakaSayısı') 
print('Adana   \t8\t587')
print('Diyarbakır\t14\t547')
print('Edirne  \t8\t500')
print('Giresun  \t8\t647')
print('İstanbul \t13\t1050')
print('Kayseri \t18\t897')
print('Mersin    \t11\t201')

il	ölüm sayısı	VakaSayısı
Adana   	8	587
Diyarbakır	14	547
Edirne  	8	500
Giresun  	8	647
İstanbul 	13	1050
Kayseri 	18	897
Mersin    	11	201

print('Program açıldığında il yazdığım \"Merhaba, Dünya!\" oldu.')
Program açıldığında il yazdığım "Merhaba, Dünya!" oldu.


ad= 'Büşra'
soy_ad = 'Akkaya'
program = 'Python'
cümle_oluşturma = 'Ben %s %s. Ben %s öğreniyorum.' %(ad, soy_ad, program)
print(cümle_oluşturma)

Ben Büşra Akkaya. Ben Python öğreniyorum.


matematik_konu = ['Köklü Sayılar', 'Üslü Sayılar', 'Problemler', 'Temel Kavramlar','Rasyonel Sayılar']
cümle_ekle = 'Matematikte bir çok konu vardır.Bunlardan en temelleri:%s' % (matematik_konu)
print(cümle_ekle)


Matematikte bir çok konu vardır.Bunlardan en 
temelleri:['Köklü Sayılar', 'Üslü Sayılar', 
'Problemler', 'Temel Kavramlar', 'Rasyonel Sayılar']


ad  =  'Büşra' 
soy_ad=  'Akkaya' 
dil  =  'Python anlatacağım' 
yeni_cümle=  'Ben {} {}. Sizlere {}'  . format(ad , soy_ad , dil)
print( yeni_cümle )


Ben Büşra Akkaya. Sizlere Python anlatacağım


x=10
y=5
print('{} + {} = {}'.format(x, y, x + y))
print('{} - {} = {}'.format(x, y, x - y))
print('{} * {} = {}'.format(x, y, x * y))
print('{} / {} = {:.2f}'.format(x, y, x / y)) 
print('{} % {} = {}'.format(x, y, x % y))
print('{} // {} = {}'.format(x, y, x // y))
print('{} ** {} = {}'.format(x, y, x ** y))


10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.00
10 % 5 = 0
10 // 5 = 2
10 ** 5 = 100000

x=10
y=5
print ( f' { x } + { y } = { x  + y } ' )
print( f' { x } - { y } = { x  -  y } ' )
print( f' { x } * { y } = { x *  y } ')
print( f' {x } / { y } = { x /  y } ' )
print ( f' { x } % { y } = { x  %  y } ' )
print ( f' { x } / / { y } = { x  //  y } ' )
print (f' { x } ** { y } = { x **  y} ' )


 10 + 5 = 15 
 10 - 5 = 5 
 10 * 5 = 50 
 10 / 5 = 2.0 
 10 % 5 = 0 
 10 / / 5 = 2 
 10 ** 5 = 100000 

 PROGRAM_DİL = 'Python'
a,b,c,d,e,f = PROGRAM_DİL
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


dil  =  ['Python','c++','R','SQL'
ilk_program=  dil [ 0 ]
print ( ilk_program) # P 
ikinci_program =  dil [ 1 ]
print ( ikinci_program) # 
üçüncü_program=dil[2]
print(üçüncü_program)
son_hal =  len ( dil ) -  1 
son_hal =  dil [ son_hal ]
print ( son_hal ) # n



dil  =  'Python' 
ilk_üç =  dil [ 0 : 3 ] # 3 dahil değil
print ( ilk_üç ) #Pyt 
son_üç =  dil [ 3 : 6 ]
print ( son_üç ) 
# Başka bir yol 
son_üç  =  dil [ - 3 :]
print( son_üç )    
son_üç  =  dil [3 :]
print( son_üç )   

hon

hon

hon

selamlama  =  'Merhaba Dünya!' 
print ( selamlama [:: - 1 ]) # !aynüD abahreM

değiş= 'iklim değişiyor'
print(değiş.capitalize()) # Iklim değişiyor

değiş= 'iklim değişiyor'
print(değiş.count('i')) # 4
print(değiş.count('y', 7, 14)) # 1, 
print(değiş.count('or')) # 1

değiş= 'iklim değişiyor'
print(değiş.endswith('yor'))   #True
print(değiş.endswith('değ')) # False

değiş= 'iklim\değişiyor'
print(değiş.expandtabs ())   #iklim   değişiyor
print(değiş.expandtabs (10))   #iklim       değişiyor

challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th'))

değiş= 'iklim değişiyor'
print(değiş.find('y'))  # 12
print(değiş.find('kl'))#1


ad = 'Büşra'
soy_ad = 'Akkaya'
yaş= 25
meslek = 'veri analisti'
ülke = 'Türkiye'
cümle= 'Ben  {} {}. Benim yaşım {}. Ben {}yim. Ben  {} yaşıyorum.'.format(ad, soy_ad, yaş, meslek, ülke)
print(cümle)

Ben  Büşra Akkaya. Benim yaşım 25.
 Ben veri analistiyim. Ben  Türkiye yaşıyorum.

değiş= 'iklim değişiyor'
ek='de'
print(değiş.index('ek')) #6
print(değiş.index('ek',9)) 

meydan   =  'OtuzGünProgram' 
print( meydan . isalnum ()) # Doğru

meydan =  '30GünProgram' 
print( meydan . isalnum ()) # Doğru

meydan   =  'otuz gün program' 
print ( meydan okuma . isalnum ()) # Yanlış, boşluk bir sayısal karakter algılamaz

meydan  =  'otuz gün python 2019' 
print( meydan okuma . isalnum ()) # Yanlış

meydan   =  'OtuzGünProgram' 
print( meydan . isalpha ()) # Doğru

meydan =  '30GünProgram' 
print( meydan . isalpha()) # Doğru

meydan   =  'otuz gün program' 
print ( meydan okuma . isalpha ()) # Yanlış, boşluk bir sayısal karakter algılamaz

meydan  =  'otuz gün python 2019' 
print( meydan okuma . isalpha ()) # Yanlış

meydan   =  'OtuzGünProgram' 
print( meydan . isdecimal ()) # False

meydan =  '123' 
print( meydan . isdecimal()) # True

meydan   = '30.2' 
print ( meydan  . isdecimal ()) #False
 
meydan  = 'otuz gün python 2019' 
print( meydan . isdecimal()) # False


metin='otuz'
print(metin.isdigit())# False
metin='30'
print(metin.isdigit())# True
metin='pandas34'
print(metin.isdigit())#False

tanım='üç_gün_sonra'
print(tanım.isidentifier())#True
tanım='3GünSonrası'
print(tanım.isidentifier())#False

ower='siz gerçek çok zekisiniz'
print(ower.isupper())# False
ower='TAKİPTE KALIN'
print(ower.isupper())# True

dil=['fransızca','almanca', 'rusça']
sonuç=' ' .join(dil)
print(sonuç)

mesaj='BBugün harika bilgiler öğrendim'
print(mesaj.strip(' '))

mesaj='Ben karpuz isterim'
print(mesaj.replace('karpuz', 'şeftali'))# Ben şeftali isterim

mesaj='ben karpuz isterim'
print(mesaj.title())#Ben Karpuz Isterim


mesaj='ben karpuz isterim'
print(mesaj.swapcase())#BEN KARPUZ ISTERIM


meydan   =  'OtuzGünProgram' 
print( meydan . startswith ('Otuz')) # Otuz ile başladığı için True

meydan =  '30GünProgram' 
print( meydan . startswith ('30')) # True

meydan   =  'otuz gün program' 
print ( meydan . startswith ('otuz')) # True
meydan  =  'otuz gün python 2019' 
print( meydan .startswith ('otuz')) # True

5. gün 

