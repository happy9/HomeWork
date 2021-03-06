#!/usr/bin/env python
# coding: utf-8

# #Контрольная работа
# 

# # 1.
# 
# Напишите **рекурсивную** функцию ```fact```, которая вычисляет факториал заданного числа ```x```. 
# 

# In[2]:


def fact(x):
    if x == 0:
        return 1
    return fact(x-1) * x


# #2
#  Создайте функцию ```filter_even```, которая принимает на вход список целых чисел,  и фильтруя, возвращает список, содержащий только четные числа. Используйте ```filter``` для фильтрации и  ```lambda```.

# In[4]:


def filter_even(li):
    return list(filter(lambda item: not item %2 , li))



# #3
# Напишите функцию ```square``` ,которая принимает на вход список целых чисел и возвращает список с возведенными в квадрат элементами. Используйте ```map```.

# In[5]:


def square(li):
    return list(map(lambda item: item**2 , li))



# #4
# Напишите функцию бинарного поиска ```bin_search```, которая принимает на вход отсортированный список и элемент. Функция должна возвращать индекс искомого элемента в списке. 
# 
# Ввод: 
# ```
# [2,5,7,9,11,17,222] 11
# ```
# Вывод: 
#  ```
#  4
#  ```
# 
# Ввод:
# ```
#  [2,5,7,9,11,17,222] 12
# ```
# Вывод:
# ```
#   -1
# ```

# In[8]:


def bin_search(li, element):
    try:
        index = li.index(element)
        return index
    except ValueError:
        return -1



# #5
# Напишите функцию ```is_palindrome``` определяющую,является ли строка палиндромом.
# Палиндромами являются текстовые строки, которые одинаково читаются слева направо и справа налево. В строках не учитываются знаки препинания, пробельные символы и цифры; регистр не имеет значения. 
# 
# На вход подается строка ```string```.
# 
# Выведите YES, если строка является палиндромом и NO иначе.
# 
# Запрещается использовать reverse списка - ```list[::-1]``` и функцию ```reversed```.
# Чтобы учесть это ограничение, эту задачу рекомендуется решать используя технику решения задач "два указателя". Один указатель читает только символы слева направо, а второй - справа налево.
# 
# Примеры:
# 
# Ввод 
# ```
# Madam, I'm Adam
# ``` 
# Вывод
# ```
# YES
# ```
# Ввод
# ```
# А роза упала на лапу Азора
# ``` 
# Вывод  
# ```
# YES
# ```

# In[10]:


def is_palindrome(string):
    string="".join(c for c in string.lower() if c.isalpha())
    length = len(string)
    first = 0
    last = length - 1
    isPalindrome = "YES"

    while first < last:
        if string[first] == string[last]:
            first = first + 1
            last = last - 1
        else:
            isPalindrome = "NO"
            break

    return isPalindrome



# # 6
# Написать функцию ```calculate```, которая принимает на вход текстовый файл содержащий строки следующего формата:
# 
# Формат файла:
#     ```арифметическая операция```    ```целое число #1```    ```целое число #2```\
# Разделитель - 4 пробела
# 
# Функция должна вернуть 1 строку.
# Строка содержит набор из чисел, разделенных запятой. 
# После последнего числа запятая не ставится.
# Каждое число - результат операции: 
#     ```"результирующее целое число"``` = ```"целое число #1"``` применить ```"арифметическая операция"``` ```"целое число #2"```
# 
# **Пример входного файла:**
# 
# `+    5    4`\
# `-    -10449    -7623`\
# `**    2    10`
# 
# **Пример выходной строки (для примера входного файла выше):**
# 
# `9,-2826,1024`
# 
# **Допустимые операции:**
# 
# `+ (сложение)`\
# `- (вычитание)`\
# `* (умножение)`\
# `// (целочисленное деление) (для этой операции подаются только положительные числа)`\
# `% (остаток от деления) (для этой операции подаются только положительные числа)`'\
# `** (возведение в степень) (для этой операции подаются только положительные числа)`
# 
# Входные числа - только целые.\
# Выходные числа - только целые.
# 
# [Входной файл для самопроверки.](https://drive.google.com/file/d/1OcqaMTseYffO2JAF_thBJDJ-aqFq9Vxc/view?usp=sharing)
# 
# [Выходная строка для самопроверки содержится в файле.](https://drive.google.com/file/d/1IkCn8C6ULuEIngSSpkvI-0cIhDUiIEk9/view?usp=sharing)
# 
# 
# 
# 
# 
# 
# 

# In[2]:


def calculate(path2file):
    f = open(path2file)
    li = f.read().split()
    f.close()
    
    x1 = li[0::3]
    x2 = li[1::3]
    x3 = li[2::3]

    result = ''
    for i in range(len(x3)):
        result += str((eval("".join(x2[i] + x1[i] + x3[i]))))
        if i!=len(x2)-1:
            result += ','
            
    return result



# # 7
# Написать функцию ```substring_slice```,которой на вход поступают два текстовых файла.
# 
# - Первый файл содержит строки текста.   
#  
# - Второй файл содержит строки из двух целых неотрицательных чисел.
# Первое число в строке всегда меньше или равно второму.
# Числа всегда меньше длины соответствующей строки первого файла.
# Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла, а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.
# 
# - Функция должна вернуть строку, состоящую из подстрок 1-го входного файла.
# Подстроки разделены пробелами.
# Какие брать подстроки - написано во втором файле.
# В конце файла пробела нет.
# 
# **Например**
# 120 строка в 1-ом файле: `JBOljrfkrfjgikenfjerkrkvkfKUGlknc`
# 120 строка во 2-ом файле: `13 27`
# Это значит 120 подстрока в результирующем файле это символы с 13 по 27, включая 13-ый и 27-ой символы.
# Не забывайте, что нумерация символов в строке с 0.
# Пример требуемой подстроки: `kenfjerkrkvkfKU`
# - **Пример 1-го входного файла:**
#   ```
# QxBpXEeyDWHiuTttWjhFMGTlrCMqpSvrNOQoxUbyiZombbLaYqBHvydPJlvdspwwpgeLNlHMVYrZvPsQkcQgPpierYSahialdXlde
# rNsZEKdYYlKKRrYGNWEXTYXOpQqrdGANRfoyeVvRwLVhZDfzKhFQkuSYODIXFLYafnXbxuwqZKQKjSiFZAtSponvmulcjicIDhNaQ
# TttSFLqbNkHvOeHSKTTGEEGxwtXImLeCmcKjvsIkIIvvlsUSazNuEsdDYlOljweSubVJxHbSJkBpByFiUCFctgrLKhlYgEWWuDYqx
# ```
# 
# - **Пример 2-го входного файла:**
# ```
# 30 84
# 5 79
# 70 70
# ```
# - **Пример выходной строки:**
# ```
# vrNOQoxUbyiZombbLaYqBHvydPJlvdspwwpgeLNlHMVYrZvPsQkcQgP KdYYlKKRrYGNWEXTYXOpQqrdGANRfoyeVvRwLVhZDfzKhFQkuSYODIXFLYafnXbxuwqZKQKjSiF b
# 
# ```

# 
# [Пример 1-го входного файла для самопроверки.](https://drive.google.com/file/d/1XlnnBunKfNA2c4so3VKH1kXKvFjOLDAX/view?usp=sharing)
# 
# [Пример 2-го входного файла для самопроверки.](https://drive.google.com/file/d/1_gIyNhoSptvlvfA8UOlY60rXDva1fW2G/view?usp=sharing)
# 
# [Пример выходной строки для двух файлов выше содержится в этом файле.](https://drive.google.com/file/d/11Lsq1DV8iuMsZ_LPuTj50w5Htq1-95Ys/view?usp=sharing)

# In[3]:


def substring_slice(path2file_1, path2file_2):
    data_file1 = open(path2file_1)
    path2file_1 = data_file1.read()
    data_file1.close()
    
    data_file2 = open(path2file_2)  
    path2file_2 = data_file2.read()  
    data_file2.close()
    
    path2file_1 = path2file_1.split()
    path2file_2 = path2file_2.split()
    
    result = ''
    x1 = path2file_2[0::2]
    x2 = path2file_2[1::2]
    for i in range(len(x2)):
        result += path2file_1[i][int(x1[i]):int(x2[i])+1]
        if i!=len(x1)-1:
            result += ' '
            
    return result



# #8
# 
# Написать функцию ```decode_ch```,на вход которой поступает строка.В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов.
# Нужно расшифровать химические символы в название химических элементов.Функция должна вернуть строку - расшифровку
# 
# Для удобства, прилагается [json файл](https://drive.google.com/file/d/1Uugf4zLRjBx-73RfelroOrf1JlTtpLfi/view?usp=sharing), который ставит в соответствие химическому символу его химическое название.
# 
# Как прочитать этот файл в словарь python (dict):
# ```
# periodic_table = json.load(open('periodic_table.json'))
# ```
# - **Пример входной строки:**
# ```
# NOTiFICaTiON
# ```
# -**Пример выходной строки:**
# ```
# АзотКислородТитанФторЙодКальцийТитанКислородАзот
# ```
# 
# Обратите внимание, что, например, "Bi" - это "Висмут", а не "БорЙод".
# То есть регистр (заглавные или прописные) букв имеет значение.
# 
# 

# In[5]:


import json

def decode_ch(sting_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
    
    string = ''
    for item in sting_of_elements:   
        if item.isupper():
            string += ' '
        string += item
    
    string = string.split()

    result = ''

    for i in string:
        for j in periodic_table:
            if i == j:
                result += periodic_table[j]
            else:
                continue
                
    return result



# #9
# 
# Создайте класс с названием Student.
# 
# При инициализации объекта подается два аргумента. Первый - имя студента. Второй - фамилия студента.
# 
# 1. Создайте три атрибута объекта данного класса:
# 
# - *name* имя студента
# - *surname* фамилия студента
# - *fullname* имя и фамилия студента через пробел
# 2. Создайте метод для экземпляра класса Student под названием greeting, который при вызове возвращает строку Hello, I am Student
# Здесь и далее нужно только написать сам класс. 
# 3. Добавьте новый атрибут класса под названием grades. При инициализации объекта соответственно добавляется новый аргумент, в котором будет лежать список оценок данного студента, по дефолту равный списку [3,4,5]. Создайте метод под названием mean_grade, который возвращает среднее всех оценок студента (то есть среднее этого атрибута).
# 4. Сделайте метод is_otlichnik, который возвращает строку YES, если средняя оценок студента больше или равна 4.5 и NO в противном случае.
# Примечание: этот метод должен вызывать метод mean_grade внутри себя.
# 5. На этот раз определим операцию сложения для двух студентов. Пусть такая операция возвращает строку следующего вида: "Name1 is friends with Name2", где Name1 и Name2 - имена первого студента и второго (именно атрибут name). То есть, если создать два экземпляра класса Student, то их сумма должна вернуть вышеописанную строку.
# 6. Теперь переопределим поведение нашего класса с функцией print. Пусть при вызове функции print от экземпляра класса Student печатается его атрибут fullname.
# 
# 

# In[8]:


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname = self.name + ' ' + self.surname
        self.grades = [3, 4, 5]
        
    def __add__(self, other):
        print('{}'.format(self.name) + ' is friends with {}'.format(other.name))
        
    def __str__(self):
        return self.fullname
    
    def greeting(self):
        return 'Hello, I am {}'.format(self.fullname)
    
    def mean_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)
    
    def is_otlichnik(self):
        if (self.mean_grade() < 4.5):
            return 'NO'
        else:
            return 'YES'
        


# #10
# 
# Определите  класс исключений ```MyError```,
#  который принимает строковое сообщение ```msg``` в качестве параметра при инициализации и также имеет атрибут ```msg```.
# 
# Подсказка: Чтобы определить кастомный класс  исключения,нужно создавать класс, унаследованный от ```Exception```.
# 
# 

# In[11]:


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
