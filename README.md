# 01 Работа
Задание: Тимофей составляет 5-буквенные коды из букв Т, И, М, О, Ф, Е, Й. Буква Й может использоваться в коде не более одного раза, при этом она не может стоять на первом месте, на последнем месте и рядом с буквой И. Все остальные буквы могут встречаться произвольное количество раз или не встречаться совсем. Сколько различных кодов может составить Тимофей?
Описание работы: Cоздает все возможные комбинации из пяти букв, взятых из списка. Затем код проверяет каждую комбинацию на соответствие условиям:
1. В комбинации не более одной буквы 'Й'.
2. Строка 'ИЙ' не содержится в комбинации.
3. Второй и последний символ комбинации не равны 'Й'.
Если комбинация удовлетворяет всем трём условиям, переменная valid_codes увеличивается на 1. По завершении проверки всех возможных комбинаций, программа выводит количество корректных комбинаций в переменной valid_codes.
![изображение](https://github.com/QNekoma/python_labs2/assets/147964939/ce77d953-91e0-434f-9545-e9b48b84f86d)
# 02 Работа
Условия: Сколько единиц содержится в двоичной записи значения выражения $4^{2020}+2^{2017}−15$ 
Описание работы: Записывается бинарное представление результата данного выражения, затем записывается количество единиц в строке result и выводим.
![image](https://github.com/QNekoma/python_labs2/assets/147964939/90dc19e9-9b9e-4941-9a44-f80aba713bc9)
# 03 Работа
Условия: Найдите среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа, имеющие ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти два делителя в два соседних столбца на экране с новой строки в порядке возрастания произведения этих двух делителей. Делители в строке также должны следовать в порядке возрастания. Например, в диапазоне [5; 9] ровно два различных натуральных делителя имеют числа 6 и 8, поэтому для этого диапазона вывод на экран должен содержать следующие значения: 
2 3
2 4
Описание работы: Находит числа в интервале 174457, 174505, у которых ровно два натуральных делителя (не считая 1 и само число), и выводит их делители в порядке возрастания.
![image](https://github.com/QNekoma/python_labs2/assets/147964939/3a9a24c5-75f8-4575-ad93-27869d384ace)
