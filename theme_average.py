from mido import MidiFile, Message, MidiTrack, MetaMessage
import numpy as np
import os
dirt_path = os.path.dirname(os.path.realpath(__file__))
mid = MidiFile(dirt_path+'\\new_song.mid')
### 印出所有的midi訊息

min_jump_count=2147483647
main_melody = 0
for i, track in enumerate(mid.tracks):
    note_num=0
    print('Track {}: {}'.format(i, track.name))
    note_sum = 0  
    note_list = []
    for j in range(len(mid.tracks[i])):
        if mid.tracks[i][j].type == 'note_on' or mid.tracks[i][j].type == 'note_off':
            note_sum += mid.tracks[i][j].note
            note_num += 1
            note_list.append(mid.tracks[i][j].note)
    note_avg=0
    if(note_num!=0):
        note_avg = note_sum/note_num

    print(note_avg)
    jump_count=0
    for j in range (len(note_list)-1):
        if note_list[j] < note_avg and note_list[j+1]>note_avg:
            jump_count+=1
    print(jump_count)
    if jump_count < min_jump_count and jump_count!=0:
        min_jump_count = jump_count
        main_melody = i
print('***')
print( main_melody)
