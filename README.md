# theme-selecting
用一些方法來選取midi檔可能代表主旋律的track

主要分為兩種：

theme_average.py: 先算出整首歌的平均音高，如果有相鄰兩個音跨過此平均的次數越多，則越不可能是主旋律。


At first, we calculate the average of all the notes in one track. If there are more adjacent notes cross the average in that track, it should be less like a theme. 

theme_single_note.py: 如果同時有越多音演奏，則越不可能是主旋律。

More note play together, less like a theme.
