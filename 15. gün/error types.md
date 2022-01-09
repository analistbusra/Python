# Python Error Types(Python Hata Türleri)

Kod yazarken, yazım hatası veya başka bir yaygın hata yapmamız yaygındır. Kodumuz çalışmazsa, Python yorumlayıcısı, sorunun nerede oluştuğu ve hatanın türü hakkında bilgi içeren geri bildirim içeren bir mesaj görüntüler. Ayrıca bazen bize olası bir düzeltme hakkında önerilerde bulunur. Programlama dillerindeki farklı hata türlerini anlamak, kodumuzda hızlı bir şekilde hata ayıklamamıza yardımcı olacak ve ayrıca yaptığımız işte daha iyi olmamızı sağlayacaktır.

En yaygın hata türlerini tek tek görelim. Önce Python etkileşimli kabuğumuzu açalım. Bilgisayarınızın terminaline gidin ve 'python' yazın. Python etkileşimli kabuğu açılacaktır.

## SyntaxError

>Python 3.9.6 (default, Jun 28 2021, 15:26:21)

>[Clang 11.0.0 (clang-1100.0.33.8)] on darwin

>Type "help", "copyright", "credits" or "license" 
>for more information.

>print 'hello world'

 > File "<stdin>", line 1

  >print 'hello world'

SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?




Gördüğünüz gibi bir sözdizimi hatası yaptık çünkü dizeyi parantez içine almayı unuttuk ve Python zaten çözümü öneriyor. Düzeltelim.


>Python 3.9.6 (default, Jun 28 2021, 15:26:21)

>[Clang 11.0.0 (clang-1100.0.33.8)] on darwin

>Type "help", "copyright", "credits" or "license" for more information.

>print 'hello world'

>File "<stdin>", line 1

>print 'hello world'

>print('hello world')

>#hello world

Basit bir örnekle anlatalım isterseniz aşağıdaki örneği inceleyebiliriz.

>print('merhaba dünya')

>#merhaba dünya

hatalı kodu inceleyelim:

>print 'merhaba dünya'

>SyntaxError: Missing parentheses in call to 'print'. Did you mean print('merhaba dünya')?

## NameError

>name='büşra'

>print(age)

>#NameError: name 'age' is not defined

gördüğünüz gibi doğru tanımlama yapılmadığında nameError verir.

>name='büşra'

>age='25'

>print(age)

>#25

Değişken adını doğru tanımlayarak hatayı sonlandırdık.

## IndexError

>numbers = [1, 2, 3, 4, 5]

>numbers[5]

>#IndexError: list index out of range

Düzeltilmiş halini inceleylim

>numbers = [1, 2, 3, 4, 5]

>numbers[2]

>#3

## ModuleNotFoundError

> import maths


ModuleNotFoundError: No module named 'maths'


Yukarıdaki örnekte bilerek 'math' fazladan bir 's' ekledim ve ModuleNotFoundError ortaya çıktı. Maths fazladan s'yi kaldırarak düzeltelim.

## AttributeError(Öznitelik Hatası)

>import math

>math.PI


AttributeError: module 'math' has no attribute 'PI'

Gördüğünüz gibi yine bir hata yaptım! Pi yerine matematik modülünden bir PI işlevi çağırmaya çalıştım. Bir öznitelik hatası oluşturdu, bu, işlevin modülde olmadığı anlamına gelir. PI'den pi'ye değiştirerek düzeltelim.

>import math

>math.pi

>#3.141592653589793

## KeyError(Anahtar Hatası)

>users = {'name':'Büşra', 'age':25, 

>'city':'İstanbul'}

>users['name']

>users['cty']

KeyError: 'cty'

Yukarıdaki örnekte yanlış kelime kullanımı görmekteyiz keyError veriyor şimdi düzeltelim ve çıktıyı inceleyelim.


>users = {'name':'Büşra', 'age':25, 

>'city':'İstanbul'}

>users['city']

>#'İstanbul'

## TypeError(TipHata)

>4+'3'


TypeError: unsupported operand type(s) for +: 'int' and 'str'

Yukarıdaki örnekte, bir dizeye sayı ekleyemediğimiz için bir TypeError ortaya çıkıyor. İlk çözüm, dizeyi int veya float'a dönüştürmek olacaktır. 

>4 + int('3')

>#7

>4+ float('3')

>#7.0

## ImportError

>from math import power

ImportError: cannot import name 'power' from 'math' (unknown location)

>from math import pow

>pow(4,3)

>#4*4*4 64

## ValueError(Değer Hatası)

>int('12a')

ValueError: invalid literal for int() with base 10: '12a'

Bu durumda, içindeki 'a' harfi nedeniyle verilen dizeyi bir sayıyla değiştiremeyiz.

>int('12')

>#12

## ZeroDivisionError
Bir sayıyı sıfıra bölemediğimizi gösteren bir hata türüdür.

>10/0

>#ZeroDivisionError: division by zero
