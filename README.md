# theme-selecting
用一些方法來選取midi檔可能代表主旋律的track

主要分為兩種：

theme_average.py: 

先算出整首歌的平均音高，如果有相鄰兩個音跨過此平均的次數越多，則越不可能是主旋律。

At first, we calculate the average of all the notes in one track. If there are more adjacent notes cross the average in that track, it should be less like a theme. 

theme_single_note.py: 

如果同時有越多音演奏，則越不可能是主旋律。

More note play together, less like a theme.

然而，以上的方法都僅僅是停留在「猜測的階段」，目前很難找到一個能百分之百精確取出主旋律的方法。

Nevertheless, the methods above is just "guessing", it is really difficult to find a method to select the theme track 100% correctly.

建議如果要使用的話，可以先用其中一個方法篩選出可能的數個track，再用第二種方法篩選最有可能的那一個

We suggest that if you want to find the theme track, 

you should use one of the two methods above and select some track which is possibly a theme track,

and than use the other to select the track that is most possibly a theme track.
