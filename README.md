# Упражнение по отработке навыков разработки мультипроцессных приложений.

## Задача

Требуется найти первую пару простых чисел, разница между которыми больше или равна заданному значению.
Значение задается в качестве первого аргумента в командной строке.

## Реализация

Задача реализуется на языках программирования python и rust. Таким образом с одной стороны приобретаются навыки разработки параллельно исполняемых программ на обоих языках, изучаются основные концепции и языковые различия многопроцессной, мультипоточной и асинхронной разработки. С другой стороны производятся замеры и сравнение скорости разработки программных продуктов, а также скорость вычисления результатов решаемой задачи на обоих языках.


## Алгоритм решения задачи

Последовательно в порядке возрастания определяется, является ли число простым, и каждое найденное простое число сравнивается с найденным перед ним. Если разность чисел больше либо равна заданному параметру, то задача решена.\b
Простота числа определяется путем целочисленного деления этого числа на все простые делители, не превышающие его квадратного корня, То есть, если хотя бы одно из таких чисел является делителем тестируемого числа (делит его нацело без остатка), то число являеттся составным.
Выполнение алгоритма начинается с некоторой заданной начальной последовательности простых чисел: [2, 3, 5, 7]. Дистанция между этими числами равна 2. Следующее тестируемое число - 9. Оно является составным и, следовательно, игнорируется. А следующее за ним 11 - простое. Вычисляем разницу между ним и предыдущим известным простым - 7, которая равна 4, и, так как она больше текущего значения дистанции (2), устанавливаем для дистанции новое значение. Найденное только что новое простое число добавляется в массив простых чисел и устанавливается как последнее известное простое число. Если полученная новая дистанция достигла или превысила  заданное целевое значение, то алгоритм останавливается и выводится результат. В противном случае цикл повторяется. \b
Описанный алгоритм является последовательным и, таким образом может выполняться одновременно только на одном ядре. Современные же системы практически стопроцентно являются многоядерными, и решение задач с помощью последовательных алгоритмов на таких системах представляется как не эффективное.
