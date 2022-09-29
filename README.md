# t101_lab1
## Описание алгоритма работы скрипта
1. Генерируются факты и правила.
2. Правила приводятся к более удобному виду.
> В исходном варианте все правила имеют вид: **[ { if:{'operand : [numbers]'},then: number}, ...]**.  
> Все факты сортируются в 3 отдельных массива по логическому операнду и каждый массив имеет более удобный вид  
> **[ [ [if], then ], ...]**
3. Факты приводястя к более удобному виду.
> Изначально факты расположены в одномерном массиве и для того, чтобы избежать прогона по всему массиву ( *O(n)* )  
> и повторения фактов они помещаются в словарь по сигнатуре **{ number:True }**, если числа нет, то метод get()
> вернёт None.
4. На переработанных данных запускается скрипт проверки фактов.
> При проверке правила or ищется **хотя бы одно совпадение** условия и факт. В таком случае факт добавляется в БЗ.  
> При проверке правила and ищется **хотя бы одно несовпадение** условия и факта. В таком случае факт не добавляется в БЗ.  
> При проверке праила not ищется **хотя бы одно совпадение** условия и факта. В таком случае факт не добавляется в БЗ.  
5. Декоративной функцией *time()* замеряется время работы функции по добавлению правил.
