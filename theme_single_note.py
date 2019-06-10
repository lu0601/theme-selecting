from mido import MidiFile, Message, MidiTrack, MetaMessage
import numpy as np
import os
dirt_path = os.path.dirname(os.path.realpath(__file__))
mid = MidiFile(dirt_path+'\\new_song.mid')
### 印出所有的midi訊息

class Select_Track:
    def __init__(self, track_num__, more_than_one__):
        self.track_num__ = track_num__
        self.more_than_one__ = more_than_one__
        
select_track = []
min_more_count=2147483647
min_more_than_one = 2147483647
main_melody = 0
for i, track in enumerate(mid.tracks):
    more_than_one = 0
    print('Track {}: {}'.format(i, track.name))
    for j in range(len(mid.tracks[i])):
        if mid.tracks[i][j].type == 'note_on' and mid.tracks[i][j].velocity != 0 :
            end_j = 0
            for k in range(j,len(mid.tracks[i])):
                if (mid.tracks[i][k].type == 'note_off' and mid.tracks[i][k].note == mid.tracks[i][j].note) or (mid.tracks[i][k].type == 'note_on' and mid.tracks[i][k].note == mid.tracks[i][j].note and mid.tracks[i][k].velocity == 0):
                    end_j = k
                    break
            ##print(end_j)
            for k in range(j, end_j):
                if mid.tracks[i][k].type== 'note_on' and mid.tracks[i][k].note != mid.tracks[i][j].note and mid.tracks[i][j].velocity!=0 and mid.tracks[i][k].velocity !=0 :
                    ##print(j, ':',k)
                    more_than_one += 1
    select_track.append(Select_Track(i, more_than_one))
    print("***********")
    print(more_than_one)
    if more_than_one < min_more_count and more_than_one!=0:
        min_more_count = more_than_one
        main_melody = i
for i in range(len(select_track)):
    print(select_track[i].track_num__, select_track[i].more_than_one__)
print('***')
print( main_melody)
