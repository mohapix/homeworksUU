# -*- coding: utf-8 -*-

text_ =\
    """# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song."""

filename = 'homework2.txt'
file = open(filename, mode='w', encoding='utf8')
file.write(text_)
file.close()

with open(filename, mode='r', encoding='utf8') as file:
    print('----- reading file: {} -----'.format(file.name))
    for line in file:
        print(line, end='')
    print('\n------- end of file -------')
print('Is file closed?', file.closed)

# Оператор with работает с файлом, как с объектом, используя служебный метод __enter__ при входе
# и служебный метод __exit__ при выходе, закрывая файл по окончанию работы вложенного кода.
