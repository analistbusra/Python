# List Comprehension(Liste Anlama)

Python'da liste anlama, bir diziden liste oluşturmanın daha kolay bir yoludur.

* Örneğin, bir dizeyi bir karakter listesine dönüştürmek istiyorsanız. Birkaç yöntem kullanabilirsiniz. Bunlardan bazılarını görelim:

>language = 'Python'

>lst = list(language) 

>print(type(lst))     

>print(lst)   

>#<class 'list'>       

>#['P', 'y', 't', 'h', 'o', 'n']

Bir bal şeklide aynı işlemi gerçekleştirelim.

>lst = [i for i in language]

>print(type(lst)) # list

>print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

* Bir sayı listesi oluşturmak istiyorsak

Örnek:

>numbers = [i for i in range(13)]  

>print(numbers)    

>#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]          

Örnek:

>suquares= [ i *  i  for i  in range ( 13 )]

>print( suquares) 

>#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]

Örnek:

>numbers = [(i, i * i) for i in range(13)]

>print(numbers) 

>#[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100), (11, 121), (12, 144)]

* Liste anlama if ifadesi ile birleştirilebilir

Örnek:
>even_numbers = [i for i in range(40) if i % 2 == 0]

>print(even_numbers)

>#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

Örnek:

>odd_numbers = [i for i in range(41) if i % 2 != 0] 

>print(odd_numbers)

>#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

Örnek:

>list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>flattened_list = [ number for row in list_of_lists for number 
in row]

>print(flattened_list)

>#[1, 2, 3, 4, 5, 6, 7, 8, 9]

## Lambda Function

Lambda işlevi, adı olmayan küçük bir anonim işlevdir. Herhangi bir sayıda argüman alabilir, ancak yalnızca bir ifadeye sahip olabilir. 

## Creating a Lambda Function
Bir lambda işlevi oluşturmak için lambda anahtar sözcüğünü, ardından bir parametre(ler) ve ardından bir ifade kullanırız.

Örnek:

>def add_two_nums(a, b):
 
 >   return a + b

>print(add_two_nums(2, 3)) #5

kendi kendini çağıran lambda örneği:

>add_two_nums  =  lambda  a , b : a  +  b 

>print ( add_two_nums ( 2 , 3 ))  #5

Örnek:

>(lambda a, b: a + b)(2,3) #5

Örnek:

>multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c

>print(multiple_variable(5, 5, 3))#22


## Lambda Function Inside Another Function(Lambda İşlevi Başka Bir İşlev İçinde)

Başka bir işlevin içinde bir lambda işlevi kullanma.
