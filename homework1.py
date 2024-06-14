# -*- coding: utf-8 -*-

from pprint import pprint

text_ =\
"""My soul is dark - Oh! quickly string
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

filename = 'homework1.txt'
file = open(filename, mode='w', encoding='utf8')
file.write(text_)
file.close()

file = open(filename, mode='r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)
