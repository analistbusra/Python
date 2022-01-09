# Python datatime(tarih saat)

Python, tarih ve saati işlemek için datetime modülüne sahiptir .


>import datetime

>print(dir(datetime))

>['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

dir veya help yerleşik komutları ile belirli bir modüldeki kullanılabilir işlevleri bilmek mümkündür. Gördüğünüz gibi datetime modülünde birçok fonksiyon var ama biz date , datetime , time ve timedelta'ya odaklanacağız . Aşağıda inceleyelim.

## Getting datetime Information(datatime bilgi alma)

>from datetime import datetime

>now = datetime.now()

>print(now)                      # 2021-12-10 00:02:35.692810

>day = now.day                   # 10

>month = now.month               # 12

>year = now.year                 # 2021

>hour = now.hour                 # 0

>minute = now.minute             # 2

>second = now.second

>timestamp = now.timestamp()

>print(day, month, year, hour, minute)

>print('timestamp', timestamp)

>print(f'{day}/{month}/{year}, {hour}:{minute}') #10/12/2021, 0:2

## Formatting Date Output Using strftime(strftime Kullanarak Tarih Çıktısını Biçimlendirme)

>from datetime import datetime

>new_year = datetime(2020, 1, 1)

>print(new_year)      # 2020-01-01 00:00:00

>day = new_year.day

>month = new_year.month

>year = new_year.year

>hour = new_year.hour

>minute = new_year.minute

>second = new_year.second

>print(day, month, year, hour, minute) #1 1 2020 0 0

>print(f'{day}/{month}/{year}, {hour}:{minute}')


Örnek:

>from datetime import datetime

>#current date and time

>now = datetime.now()

>t = now.strftime("%H:%M:%S")

>print("time:", t)

>#time: 00:14:23

>time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

>#mm/dd/YY H:M:S format

>print("time one:", time_one)

>#time one: 12/10/2021, 00:14:23

>time_two = now.strftime("%d/%m/%Y, %H:%M:%S")

>#dd/mm/YY H:M:S format

>print("time two:", time_two)

>#time two: 10/12/2021, 00:14:23

Yukarıdaki örnek de kısaltmalar ile datatime işlevlerini kullanabildiğimizi görmekteyiz ve bunlar gibi birçok kısaltma bulunmaktadır ek olarak dosyaya tabloyu ekleyeceğim şimdi biz devam edelim.

## String to Time Using strptime(strptime Kullanarak Zaman Dizesi)

>from datetime import datetime

>date_string = "5 December, 2019"

>print("date_string =", date_string)

>date_object = datetime.strptime(date_string, "%d %B, %Y")

>print("date_object =", date_object)

## Using date from datetime(date kullanarak zamantarih)

>from datetime import date

>d = date(2020, 8, 4)

>print(d)

>#2020-08-04

>print('Current date:', d.today())    # Current date: 2021-12-10

>today = date.today()

>print("Current year:", today.year)   # Current year: 2021

>print("Current month:", today.month) # Current month: 12

>print("Current day:", today.day)     # Current day: 10



## Time Objects to Represent Time

time kullanarak tarih saat bilgilerine nasıl eriştiğimize dilerseniz bir inceleyelim.

>from datetime import time

>#time(hour = 0, minute = 0, second = 0)

>a = time()

>print("a =", a)

>#a = 00:00:00

>b = time(10, 30, 50)

>print("b =", b)

>#b = 10:30:50

>c = time(hour=10, minute=30, second=50)

>print("c =", c)

>#c = 10:30:50

>d = time(10, 30, 50, 200555)

>print("d =", d)

>#d = 10:30:50.200555

## Difference Between Two Points in Time Using(Zaman Kullanımında İki Nokta Arasındaki Fark)

>today = date(year=2021, month=12, day=11)

>new_year = date(year=2022, month=1, day=1)

>time_left_for_newyear = new_year - today

>print('Yeni yıla kalan süre: ', time_left_for_newyear)

>#Yeni yıla kalan süre:  21 days, 0:00:00

>t1 = datetime(year = 2021, month = 12, day = 11, hour = 0, 
minute = 59, second = 0)

>t2 = datetime(year = 2022, month = 1, day = 1, hour = 0, minute 
= 0, second = 0)

>diff = t2 - t1

>print('Yeni yıla kalan süre:', diff)

>#Yeni yıla kalan süre: 20 days, 23:01:00





## Difference Between Two Points in Time Using timedelate(Timedelata Kullanarak Zamanda İki Nokta Arasındaki Fark)

