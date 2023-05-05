# Group-selection-models-for-multiple-projects 

Construction and research of models of group selection of a set of projects. 

Let N = {1, 2, ..., n} be the electors, A = {a, b, ..., z} be the alternatives.
For any i of N, for any a, b of A, a is preferable to b or b is preferable to a for i.

P(A) is a group profile of arrangements on a variety of alternatives. 

For example, for the set A = {a, b, c} and the set N = {1, 2, 3}, the group profile can have the form

1    2    3

a    b    b

b    c    a

c    a    c

GRS(A) is the set of all group profiles on the set A.

Implement the functions of Condorcet and the Board of group selection and compare the results of their application. 

Condorcet function:
a is preferable to b if and only if {for i of N, a is preferable to b} > n/2.

The Borda function:
a is preferable to b if and only if B(a) > B(b), where B(a) is equal to the sum of i of N Bi(a), in turn Bi(a) is equal to b of A such that a is preferable to b.

# Модели группового выбора множества проектов

Построение и исследование моделей группового выбора множества проектов.

Пусть N = {1, 2, ..., n} - выборщики, A = {a, b, ..., z} - альтернативы.
Для любого i из N, для любых a, b из A a предпочтительнее b либо b предпочтительнее a для i.

P(A) - групповой профиль ранжировок на множестве альтернатив. 

Например, для множества A = {a, b, c} и множества N = {1, 2, 3} групповой профиль может иметь вид

1    2    3

a    b    b

b    c    a

c    a    c

GRS(A) - множество всех групповых профилей на множестве A.

Реализовать функции Кондорсе и Борда группового выбора  и сравнить результаты их применения. 

Функция Кондорсе:
a предпочтительнее b тогда и только тогда, когда {для i из N a предпочтительнее b} > n/2.

Функция Борда:
a предпочтительнее b тогда и только тогда, когда B(a) > B(b), где B(a) равна сумме по i из N Bi(a), в свою очередь Bi(a) равна b из A такие что а предпочтительнее b.
