# Pandas

Pandas, Python programlama dili için açık kaynaklı, yüksek performanslı, kullanımı kolay veri yapıları ve veri analiz araçlarıdır. Pandas, seriler ve veri çerçeveleri olan tablo benzeri verilerle çalışmak üzere tasarlanmış veri yapıları ve araçlar ekler . Pandas, veri işleme için aşağıdaki özellikleri sağlar.

* yeniden şekillendirme
* birleştirme
* sıralama
* dilimleme
* toplama
* atama

## Installing Pandas(pandas yükleme)

    pip install pandas



* Pandas veri yapısı Seri ve DataFrame'lere dayanmaktadır .
Bir dizi bir sütundur ve bir DataFrame, dizi koleksiyonundan oluşan çok boyutlu bir tablodur . Bir pandas serisi oluşturmak için tek boyutlu diziler veya bir python listesi oluşturmak için numpy kullanmalıyız. 

## Importing Pandas(pandas içe aktarmak)

     import pandas as pd 
     import numpy  as np

## Creating Pandas Series with Default Index(Varsayılan Dizin ile PandaS Serisi Oluşturma)

Örnek:

    nums = [1, 2, 3, 4,5]
    s = pd.Series(nums)
    print(s)


Çıktı:


    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64


## Creating Pandas Series with custom index(Özel dizinle Pandas Serisi oluşturma) 

Örnek:
    nums = [1, 2, 3, 4, 5]
    s = pd.Series(nums, index=[1., 2., 3., 4., 5.])
    print(s)

    1.0    1
    2.0    2
    3.0    3
    4.0    4
    5.0    5
    dtype: int64


Örnek:

    names = ['Büşra','İbrahim','Fatma']
    names = pd.Series(names, index=[1, 2, 3])
    print(names)

    1      Büşra
    2    İbrahim
    3      Fatma
    dtype: object

## Creating Pandas Series from a Dictionary(Sözlükten Pandas Serisi Oluşturma)

    dct = {'name':'Büşra','country':'Türkiye','city':'İstanbul'}
    s = pd.Series(dct)
    print(s)


Çıktı:

    name          Büşra
    country     Türkiye
    city       İstanbul
    dtype: object

## Creating a Constant Pandas Series(Sabit Bir Panda Serisi Oluşturma)

      = pd.Series(10, index = [1, 2, 3])
    print(s)

     1    10
     2    10
     3    10
    dtype: int64

## Creating a Pandas Series Using Linspace(Linspace Kullanarak Panda Serisi Oluşturma)

     s = pd.Series(np.linspace(5, 22, 10)) # linspace(starting, end, items)
     print(s)


     0     5.000000
     1     6.888889
     2     8.777778
     3    10.666667
     4    12.555556
     5    14.444444
     6    16.333333
     7    18.222222
     8    20.111111
     9    22.000000
     dtype: float64

# DataFrames (Veri Çerçevesi)
Pandalar veri çerçeveleri farklı şekillerde oluşturulabilir.
data = [
    ['Büşra', 'Türkiye', 'İstanbul'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

   Names  Country       City
0  Büşra  Türkiye   İstanbul
1  David       UK     London
2   John   Sweden  Stockholm

## Creating DataFrames from List of Lists(Liste Listesinden DataFrames Oluşturma)

data = {'Name': ['Büşra', 'David', 'John'], 'Country':[
    'Türkiye', 'UK', 'Sweden'], 'City': ['İstanbul', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

    Name  Country       City
0  Büşra  Türkiye   İstanbul
1  David       UK     London
2   John   Sweden  Stockholm

## Creating DataFrame Using Dictionary(Sözlük Kullanarak DataFrame Oluşturma)

data = {'Name': ['Büşra', 'David', 'John'], 'Country':[
    'Türkiye', 'UK', 'Sweden'], 'City': ['İstanbul', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

    Name  Country       City
0  Büşra  Türkiye   İstanbul
1  David       UK     London
2   John   Sweden  Stockholm


## Creating DataFrames from a List of Dictionaries(Sözlükler Listesinden DataFrames Oluşturma)
data = [
    {'Name': 'Büşra', 'Country': 'Türkiye', 'City': 'İstanbul'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

    Name  Country       City
0  Büşra  Türkiye   İstanbul
1  David       UK     London
2   John   Sweden  Stockholm

## Reading CSV File Using Pandas(Pandas Kullanarak CSV Dosyasını Okumak)
import pandas as pd

df = pd.read_csv('veriler.csv')
print(df)



## Data Exploration(Veri Keşfi)

head() komutu ile head(5) ile ilk 5 veriyi çağırırız.


## Modifying a DataFrame(Bir DataFrame'i Değiştirme)

## Creating a DataFrame(DataFrame Oluşturma)

## Adding a New Column(Yeni Sütun Ekleme)

## Modifying column values(Sütun değerlerini değiştirme)

## Formating DataFrame columns(DataFrame sütunlarını biçimlendirme)

## Checking data types of Column values(Sütun değerlerinin veri türlerini kontrol etme)

### Boole İndeksleme