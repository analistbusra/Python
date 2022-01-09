# Python for Statistical Analysis(İstatistiksel Analiz için Python)

İstatistik, verilerin toplanması , düzenlenmesi , görüntülenmesi , analiz edilmesi , yorumlanması ve sunulmasını inceler. İstatistik, veri bilimi ve makine öğrenimi için ön koşul olması önerilen bir Matematik dalıdır. İstatistik çok geniş bir alandır ama biz bu bölümde sadece en alakalı kısma odaklanacağız. Bu zorluğu tamamladıktan sonra web geliştirme, veri analizi, makine öğrenimi ve veri bilimi yoluna gidebilirsiniz. 

# Data(Veri)
 Veri, genellikle analiz olmak üzere, bir amaç için toplanan ve çevrilen herhangi bir karakter kümesidir. Metin ve sayılar, resimler, ses veya video dahil herhangi bir karakter olabilir. Veriler bir bağlama yerleştirilmezse, bir insan veya bilgisayar için bir anlam ifade etmez. Verilerden anlam çıkarmak için farklı araçlar kullanarak veriler üzerinde çalışmamız gerekir.Veri analizi, veri bilimi veya makine öğreniminin iş akışı verilerden başlar. Veriler bazı veri kaynaklarından sağlanabilir veya oluşturulabilir. Yapılandırılmış ve yapılandırılmamış veriler vardır.Veriler küçük veya büyük formatta bulunabilir. Alacağımız veri türlerinin çoğu, dosya işleme bölümünde ele alınmıştır.

 # Statistics Module(İstatistik Modülü)

 Python istatistik modülü, sayısal verilerin matematiksel istatistiklerini hesaplamak için işlevler sağlar. Modül, NumPy, SciPy gibi üçüncü taraf kitaplıklarına veya Minitab, SAS ve Matlab gibi profesyonel istatistikçileri hedefleyen tescilli tam özellikli istatistik paketlerine rakip olmayı amaçlamaz. Grafik ve bilimsel hesap makineleri seviyesine yöneliktir.

 # NumPy
 İlk bölümde Python'u başlı başına harika bir genel amaçlı programlama dili olarak tanımladık, ancak diğer popüler kütüphanelerin (numpy, scipy, matplotlib, pandas vb.) yardımıyla bilimsel hesaplama için güçlü bir ortam haline geldi.Numpy,Python'daki temel kiteplıklardan biridir dilerseniz detaylı NumPy kütüphanesini inceleyelim ve uygulayalım.

 ### Importing NumPy
NumPy kütüphanesini içe aktaralım.

 >import numpy as np

>print('numpy:', np.__version__)

>#numpy: 1.20.3

>print(dir(np))
# * Creating numpy array using

### Creating int numpy arrays(int numpy dizileri oluşturma)

>#python liste oluşturma

>python_list = [1,2,3,4,5]

>#Veri türleri kontrol

>print('Type:', type (python_list)) # <class 'list'>
    
>print(python_list) # [1, 2, 3, 4, 5]

>two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

>print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

>#Python listesinden Numpy(Sayısal Python) dizisi oluşturma

>numpy_array_from_list = np.array(python_list)

>print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>

>print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

### * Creating float numpy arrays(Float numpy dizileri oluşturma)
Bir kayan nokta veri türü parametresiyle listeden bir kayan nokta dizisi oluşturma

Örnek:

>python_list = [1,2,3,4,5]

>numy_array_from_list2 = np.array(python_list, dtype=float)

>print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

### * Creating boolean numpy arrays(Boolean numpy dizileri oluşturma)
Listeden bir boole dizisi oluşturma

>numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)

>print(numpy_bool_array)# [False  True  True False False]

### Creating multidimensional array using numpy(Numpy kullanarak çok boyutlu dizi oluşturma)
Numpy dizisinde bir veya birden çok satır ve sütun olabilir

>two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

>numpy_two_dimensional_list = np.array(two_dimensional_list)

>print(type (numpy_two_dimensional_list))

>print(numpy_two_dimensional_list)

><class 'numpy.ndarray'>

>[[0 1 2]
 
 >[3 4 5]
 
 >[6 7 8]]

### Converting numpy array to list(Numpy dizisini listeye dönüştürme)
Bir diziyi her zaman tolist() kullanarak bir python listesine dönüştürebiliriz. 

>np_to_list  =  numpy_array_from_list . tolist ()

>print( type ( np_to_list ))

>print( 'tek boyutlu dizi:' , np_to_list )

>print( 'iki boyutlu dizisi' , numpy_two_dimensional_list . tolist ())
### Creating numpy array from tuple(Tuple'dan numpy dizisi oluşturma)

>#NumPy Dizisi 

>python_tuple = (1,2,3,4,5)

>print(type (python_tuple)) # <class 'tuple'>

>print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)


>#Python'da NumPy Dizisi

>numpy_array_from_tuple = np.array(python_tuple)
>print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
>print('numpy_array_from_tuple: ', numpy_array_from_tuple) # >numpy_array_from_tuple:  [1 2 3 4 5]

### Shape of numpy array(Numpy dizisinin şekli)
Şekil yöntemi, dizinin şeklini bir tanımlama grubu olarak sağlar. Birincisi satır, ikincisi sütundur. Dizi tek boyutluysa dizinin boyutunu döndürür.


>nums = np.array([1, 2, 3, 4, 5,6,7])
>print(nums)
>print('shape of nums: ', nums.shape)
>print(numpy_two_dimensional_list)
>print('shape of numpy_two_dimensional_list: ', >numpy_two_dimensional_list.shape)
>three_by_four_array = np.array([[0, 1, 2, 3],
       
        [4,5,6,7],
        [8,9,10, 11]])
>print(three_by_four_array.shape)


>[1 2 3 4 5 6 7]

>shape of nums:  (7,)

>[[0 1 2]

> [3 4 5]

 >[6 7 8]]

>shape of numpy_two_dimensional_list:  (3, 3)
(3, 4)

### Data type of numpy array(Numpy dizisinin veri türü)
Veri türleri türü: str, int, float, Complex, bool, list, None

>int_lists = [-5,-4,-3, -2, -1, 0, 1, 2,3,4,5]

>int_array = np.array(int_lists)

>float_array = np.array(int_lists, dtype=float)

>print(int_array)
#[-5 -4 -3 -2 -1  0  1  2  3  4  5]

>print(int_array.dtype)#int32

>print(float_array)
#[-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]

>print(float_array.dtype)#float64

### Size of a numpy array(Numpy dizisinin boyutu)
Numpy'de, bir numpy dizi listesindeki öğelerin sayısını bilmek için "size" kullanırız.

>numpy_array_from_list = np.array([1, 3, 5, 7,9])
>
>two_dimensional_list = np.array([1, 2], [3, 4],[6, 7])


>print('The size:', numpy_array_from_list.size) # 5
>
>print('The size:', two_dimensional_list.size)  # 3

## Mathematical Operation using numpy(Numpy kullanarak matematiksel işlem)
NumPy dizisi, tam olarak python listesi gibi değildir. Python listesinde matematiksel işlem yapmak için öğeler arasında döngü yapmalıyız, ancak numpy herhangi bir matematiksel işlemi döngü yapmadan yapmamıza izin verebilir. Matematiksel operasyon:

Toplama (+)

çıkarma (-)

Çarpma işlemi (*)

Bölünme (/)

Modüller (%)

Kat Bölümü(//)

üstel(**)
### Addition(Toplama)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])

print('original array: ', numpy_array_from_list)

ten_plus_original = numpy_array_from_list  + 10

print(ten_plus_original)

#original array:  [1 2 3 4 5]

#[11 12 13 14 15]

### Subtraction(Çıkarma)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])

print('original array: ', numpy_array_from_list)

ten_minus_original = numpy_array_from_list  - 10

print(ten_minus_original)

    original array:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]

### Multiplication(Çarpma)
>numpy_array_from_list = np.array([1, 2, 3, 4, 5])

>print('original array: ', numpy_array_from_list)

>ten_times_original = numpy_array_from_list % 3

>print(ten_times_original)

original array:  [1 2 3 4 5]

    [1 2 0 1 2]
### Division(Bölünme)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
#original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)#[0 0 0 0 0]

### Modulus(Modül)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
    
#original array:  [1 2 3 4 5]
#[1 2 0 1 2]  
### Floor Division(Kat Bölümü)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
#original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
[0 0 0 0 0]
### Exponential(Üstel)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

original array:  [1 2 3 4 5]
[ 1  4  9 16 25]
### Checking data types

## Converting types(Türleri Değiştirme)
Numpy dizisinin veri türlerini dönüştürebiliriz

1) Int to Float

numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr
#array([1., 2., 3., 4.])

2) Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
#array([1, 2, 3, 4])

3) Int ot boolean

np.array([-3, -2, 0, 1,2,3], dtype='bool')
#array([ True,  True, False,  True,  True,  True])

4) Int to str

numpy_array_from_list.astype('int').astype('str')
#array(['1', '2', '3', '4', '5'], dtype='<U11')

## Multi-dimensional Arrays(Çok Boyutlu Diziler)

two_dimension_array = np.array([(0,2,4),(1,3,5), (6,7,8)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)


<class 'numpy.ndarray'>
[[0 2 4]
 [1 3 5]
 [6 7 8]]
Shape:  (3, 3)
Size: 9
Data type: int32


### Getting items from a numpy array(Numpy dizisinden öğe alma)

Örnek:1

two_dimension_array = np.array([[0,2,4],[3,5,7], [-1,-8,-9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('Even nubers row:', first_row)
print('odd row:', second_row)
print('negative numbers row: ', third_row)

Even nubers row: [0 2 4]
odd row: [3 5 7]
negative numbers row:  [-1 -8 -9]

Örnek:2
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)



First column: [ 0  3 -1]
Second column: [ 2  5 -8]
Third column:  [ 4  7 -9]
[[ 0  2  4]
 [ 3  5  7]
 [-1 -8 -9]]

### Slicing Numpy array(Numpy Dizisini Dilimleme)
Numpy'de dilimleme, python listesinde dilimlemeye benzer

two_dimension_array = np.array([[1,2,3,1],[4,5,6,2], [7,8,9,4]])
first_two_rows_and_columns = two_dimension_array[0:4, 0:4]
print(first_two_rows_and_columns)


[[1 2 3 1]
 [4 5 6 2]
 [7 8 9 4]]
 
 ### How to reverse the rows and the whole array?
 (Satırları ve tüm diziyi nasıl tersine çevirebilirim?)

 two_dimension_array[::]

#array([[1, 2, 3, 1],
      # [4, 5, 6, 2],
       #[7, 8, 9, 4]])

### Reverse the row and column positions(Satır ve sütun konumlarını ters çevirin)
    two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array[::-1,::-1]


array([[9, 8, 7],
       [6, 5, 4],
       [3, 2, 1]])

## How to represent missing values ?(Eksik değerler nasıl temsil edilir?)

     print(two_dimension_array)
    two_dimension_array[1,1] = 55
    two_dimension_array[1,2] =44
    print(two_dimension_array)


     [[1 2 3]
     [4 5 6]
     [7 8 9]]
     [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]

     #numpy.zeros(shape, dtype=float, order='C')
     numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
     numpy_zeroes


    array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])

* #Reshape: Yeniden adlandırma yapar.
numpy.reshape(), numpy.flatten() genel gösterimi aşağıdaki örnekte inceleyelim.

       first_shape  = np.array([(1,2,3), (4,5,6)])
       print(first_shape)
       reshaped = first_shape.reshape(3,2)
       print(reshaped)

       [[1 2 3]
       [4 5 6]]
       [[1 2]
       [3 4]
       [5 6]]

* "array" leri birleştirelim.

      np_list_one = np.array([1,2,3])   
 
      np_list_two = np.array([4,5,6])

      print(np_list_one + np_list_two)

      print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

      #[5 7 9]

      #Horizontal Append: [1 2 3 4 5 6]

    
• 	Vertical Stack(Dikey Yığın)

    
    print('Vertical Append:', np.vstack((np_list_one,  np_list_two)))

    #Vertical Append: [[1 2 3]
    #[4 5 6]]

* Generating Random Numbers(Rastgele Sayılar Üretme)

Örnek:1

       random_float = np.random.random()
       random_float
       #0.10062022391087522

Örnek:2

      #0 ile 10 arasında rastgele bir tamsayı oluşturma
       random_int = np.random.randint(0, 11)
       print(random_int)
      #9 rasgele 0 ile 10 arasında  bir sayı geldi


Örnek:3

        #2 ile 10 arasında rasgele 4 adet tam sayı üret
            random_int = np.random.randint(2,10, size=4)
            random_int
        #array([5, 4, 2, 9])



Örnek:4

    #3'e 3 lük matris olsun ve 2ile 10 arası rassal sayılardan oluşsun.
    random_int = np.random.randint(2,10, size=(3,3))
    random_int

    #array([[2, 4, 6],
       [6, 9, 2],
       [4, 2, 2]])

* Generationg random numbers(Rasgele Sayı Oluşturma)

Genel gösterim: np.random.normal(mu, sigma, size)

    normal_array = np.random.normal(79, 15, 80)
    normal_array
Çıktı:

    array([ 65.79162175,  52.87867978,  78.67320333,  52.61137418,
       108.93041318,  73.88803797,  98.40779342,  82.45002868,
        82.85260741,  64.99056632,  65.38146986,  48.36771228,
        49.04167286,  47.09471977,  54.94069096,  85.54996565,
        86.82911375,  64.6712154 ,  62.7470582 ,  60.22290748,
        78.70096193,  91.332835  ,  96.87060371,  79.63618362,
        88.38094156,  93.04927569,  90.43887856,  85.44640763,
        64.38383598,  81.21542455,  47.20465619,  80.2904986 ,
        65.16934088,  67.27709637,  76.83120845,  74.79379359,
        72.95407443,  90.49216529,  95.71560489,  57.5762741 ,
        57.55055755,  92.74968067,  56.1174167 ,  83.96339255,
        36.68622187,  84.49278091,  59.89850725,  73.36244983,
        61.27726988,  89.37622428,  89.22865229, 107.11481286,
        71.53717157,  72.96655027, 113.60741613,  72.96181181,
        67.54535122,  82.36553804,  88.61826315,  81.0347691 ,
        85.30413514,  71.34114649,  83.3867504 ,  61.90216392,
        75.64732757,  83.73429924,  67.1720353 ,  90.38365832,
        82.4072446 ,  84.25445911,  91.39229014,  81.98140515,
        77.11038093, 101.34846151,  78.80529281,  65.62182063,
        62.83452668,  98.49867943,  74.47540675,  82.57894099])

## Numpy and Statistics(NumPy ve İstatistik)

Öncelikle gerekli kütüphaneleri çağıralım “seaborn” ve “ matplotlip” çağıralım. Aşağıda örnekte bir set oluşturalım ve histogramını inceleyelim.

     import matplotlib.pyplot as plt
     import seaborn as sns
     sns.set()
     plt.hist(normal_array, color="grey", bins=50)

Çıktı:

     (array([1., 0., 0., 0., 0., 0., 2., 1., 1., 0., 2., 1., 1., 2., 0., 3., 3.,
        0., 7., 2., 1., 0., 2., 4., 3., 1., 2., 4., 3., 5., 5., 4., 1., 2.,
        5., 2., 2., 0., 1., 1., 2., 0., 1., 0., 0., 1., 1., 0., 0., 1.]),
    array([ 36.68622187,  38.22464575,  39.76306964,  41.30149352,
         42.83991741,  44.37834129,  45.91676518,  47.45518906,
         48.99361295,  50.53203683,  52.07046072,  53.6088846 ,
         55.14730849,  56.68573237,  58.22415626,  59.76258015,
         61.30100403,  62.83942792,  64.3778518 ,  65.91627569,
         67.45469957,  68.99312346,  70.53154734,  72.06997123,
         73.60839511,  75.146819  ,  76.68524288,  78.22366677,
         79.76209065,  81.30051454,  82.83893842,  84.37736231,
         85.91578619,  87.45421008,  88.99263397,  90.53105785,
         92.06948174,  93.60790562,  95.14632951,  96.68475339,
         98.22317728,  99.76160116, 101.30002505, 102.83844893,
        104.37687282, 105.9152967 , 107.45372059, 108.99214447,
        110.53056836, 112.06899224, 113.60741613]),
    <BarContainer object of 50 artists>)
## Matrix in numpy(NumPy'da Matris)

Örnek:
      
       four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
       four_by_four_matrix

Çıktı:

     matrix([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])


Örnek:
    
    np.asarray(four_by_four_matrix)[2] = 2
    four_by_four_matrix

Çıktı:

   
     matrix([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [2., 2., 2., 2.],
        [1., 1., 1., 1.]])

## Numpy numpy.arange()
Arange Nedir?
Bazen, tanımlanmış bir aralık içinde eşit aralıklarla yerleştirilmiş değerler oluşturmak istersiniz. Örneğin, 1'den 10'a kadar değerler oluşturmak istiyorsunuz; numpy.arange() işlevini kullanabiliriz.

    for l in lst:
    print(l)
    0
    2
    4
    6
    8
    10

Sayı oluşrutalım başlangış noktası artış, miktarı ve bitiş noktasını ele alalım genel gösterimi:
range arange numpy.arange(start, stop, step) 

    whole_numbers = np.arange(0, 20, 1)
    whole_numbers

    #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])
## Creating sequence of numbers using linspace(Linspace kullanarak sayı dizisi oluşturma)
Virgül sonrası olan değerler oluşturmak isterseniz linspace kullanabiliriz.

     np.linspace(1.0, 5.0, num=10)#1.0'dan 5.0'a 10 tane sayı oluşturalım.

    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
    
Son değeri dahil etmemek.

    np.linspace(1.0, 5.0, num=5, endpoint=False)
    #array([1. , 1.8, 2.6, 3.4, 4.2])

LogSpace, bir günlük ölçeğinde çift aralıklı sayıları döndürür. Logspace, np.linspace ile aynı parametrelere sahiptir.
Genel Gösterim: numpy.logspace(start, stop, num, endpoint)

     np.logspace(2, 4.0, num=4)

     array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])

    #Liste Parçalayalım
    np_list = np.array([(1,2,3), (4,5,6)])
    np_list

    #array([[1, 2, 3],
     #  [4, 5, 6]])

    #Birinci satır İkinci satır olarak parçalayalım.
    print('First row: ', np_list[0])
    print('Second row: ', np_list[1])

    #First row:  [1 2 3]
    #Second row:  [4 5 6]

    print('First column: ', np_list[:,0])
    print('Second column: ', np_list[:,1])
    print('Third column: ', np_list[:,2])

    #First column:  [1 4]
    #Second column:  [2 5]
    #Third column:  [3 6]

# NumPy Statistical Functions with Example(Örnekle NumPy İstatistiksel İşlevleri)
NumPy, dizideki verilen öğelerden minimum, maksimum, ortalama, medyan, yüzdelik, standart sapma ve varyans vb. bulmak için oldukça kullanışlı istatistiksel işlevlere sahiptir. Fonksiyonlar aşağıdaki gibi açıklanmıştır.
İstatistiksel fonksiyon Numpy, aşağıda listelendiği gibi sağlam istatistiksel fonksiyonla donatılmıştır.

Numpy Fonksiyonları

* Min np.min()
* Maks. np.maks()
* Ortalama np.mean()
* Medyan np.medyan()
* varyans
* Yüzdelik
* Standart sapma np.std()
### How to create repeating sequences?(Tekrar eden diziler nasıl oluşturulur?)

     a = [1,2,3]
     print('Tile:   ', np.tile(a, 2)) # 2 kere tekrar etsin

     #Tile:    [1 2 3 1 2 3]
Örnek:2

     print('Repeat: ', np.repeat(a, 2))
     #Repeat:  [1 1 2 2 3 3]

### How to generate random numbers?()

Örnek:1

     one_random_num = np.random.random()
     one_random_in = np.random
     print(one_random_num)
    #0.22885345753592512

Örnek:2

     r = np.random.random(size=[2,3])# 2'ye 3 Matris şeklinde 
     print(r)
     #[[0.43326235 0.06563784 0.37499954]
     #[0.87698826 0.11264158 0.81280818]] 


Örnek:3

     from scipy import stats
    np_normal_dis = np.random.normal(5, 0.1, 1000) 
    print(np_normal_dis)
    ##min, max, mean, median, sd
     print('min: ', np.min(np_normal_dis))
     print('max: ', np.max(np_normal_dis))
     print('mean: ', np.mean(np_normal_dis))
     print('median: ', np.median(np_normal_dis))
    print('mode: ', stats.mode(np_normal_dis))
    print('sd: ', np.std(np_normal_dis))

Çıktı:
   
    max:  5.329041899264341
    mean:  4.998723087998381
    median:  5.002055137562557
    mode:  ModeResult(mode=array([4.60482159]), count=array([1]))
    sd:  0.09456348661589764

Histogramını görelim:

     plt.hist(np_normal_dis, color="grey", bins=21)
     plt.show()

## Lineer Cebir
Doğrusal iki dizinin çarpımı 

     f = np.array([1,2,3])
     g = np.array([4,5,3])
    ### 1*4+2*5 + 3*6
    np.dot(f, g)  # 23

### NumPy Matrix Multiplication with np.matmul()

     h = [[1,2],[3,4]]
    i = [[5,6],[7,8]]
     ###1*5+2*7 = 19
    np.matmul(h, i)
    ###array([[19, 22],
       #[43, 50]])

Determinant:

    Determinant 2*2 matrix
    ### 5*8-7*6np.linalg.det(i)

Örnek:

     #x+2 olsun ve  0'dan başlasın ve 11'e kadar 1'er artsın
    new_list = [ x + 2 for x in range(0, 11)]
    new_list
    #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Örnek:
  
    #x+2 yerine bir başka şekilde aynı işlemi yapabiliriz.
    np_arr = np.array(range(0, 11))
    np_arr + 2
    #array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])

* Doğrusal ilişkisi olan nicelikler için doğrusal denklem kullanırız. Aşağıdaki örneği görelim:

      temp = np.array([1,2,3,4,5])
      pressure = temp * 2 + 5
      pressure
      #array([ 7,  9, 11, 13, 15])
      #doğrusal ilerleyen bir veriyi ele alalım.

* grafiği çizdirelim

      plt.plot(temp,pressure)
      plt.xlabel('Temperature in oC')
      plt.ylabel('Pressure in atm')
      plt.title('Temperature vs Pressure')
      plt.xticks(np.arange(0, 6, step=0.5))
      plt.show()

* Numpy kullanarak Gauss normal dağılımını çizmek. Aşağıda görebileceğiniz gibi, numpy rastgele sayılar üretebilir. Rastgele örnek oluşturmak için ortalama(mu), sigma(standart sapma), veri noktalarının sayısına ihtiyacımız var.

