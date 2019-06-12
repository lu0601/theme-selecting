from operator import attrgetter
### 印出所有的midi訊息

########類別，為了接下來要存track的編號和多音重複的數量#########
def select_theme(mid):
    class Select_Track:
        def __init__(self, track_num__, more_than_one__):
            self.track_num__ = track_num__
            self.more_than_one__ = more_than_one__

    select_track_num = 3 ##要選出的音軌的數目

    select_track = [] ##建立等等要存track的陣列##
    main_melody = 0

    for i, track in enumerate(mid.tracks):
        can_be_selected = False
        more_than_one = 0
        print('Track {}: {}'.format(i, track.name))
        for j in range(len(mid.tracks[i])):
            if mid.tracks[i][j].type == 'note_on' and mid.tracks[i][j].velocity != 0 :
                end_j = 0
                for k in range(j,len(mid.tracks[i])):
                    if (mid.tracks[i][k].type == 'note_off' and mid.tracks[i][k].note == mid.tracks[i][j].note) or (mid.tracks[i][k].type == 'note_on' and mid.tracks[i][k].note == mid.tracks[i][j].note and mid.tracks[i][k].velocity == 0):
                        end_j = k
                        break
                ##找到一個音現持續的區間##
                for k in range(j, end_j):
                    if mid.tracks[i][k].type== 'note_on' and mid.tracks[i][k].note != mid.tracks[i][j].note and mid.tracks[i][j].velocity!=0 and mid.tracks[i][k].velocity !=0 :
                        more_than_one += 1
                ##看看那個區間裡是否有其他音也在（即兩個音重疊）##
            if mid.tracks[i][j].type == 'note_on' or mid.tracks[i][j].type == 'note_off' :
                can_be_selected = True

        if can_be_selected == True:
            select_track.append(Select_Track(i, more_than_one)) ##把這些重疊的數量和track的編號加到剛剛的class裡面##
        print("***********")
        print(more_than_one)

    for i in range(len(select_track)):
        print(select_track[i].track_num__, select_track[i].more_than_one__)

    sorted_select_track = sorted(select_track,reverse = False, key = attrgetter('more_than_one__'))###排序，重疊音最少的往前擺###

    print("sorted:")

    for i in range(len(sorted_select_track)):
        print(sorted_select_track[i].track_num__, sorted_select_track[i].more_than_one__)

    selected_three_track = []

    for i in range(select_track_num):
        selected_three_track.append(sorted_select_track[i].track_num__) ##選取重疊因最少的三個track

    min_jump_count=2147483647
    main_melody = 0
    for i in range(len(selected_three_track)):
        note_num=0
        ##print('Track {}: {}'.format(i, track.name))
        print("###",selected_three_track[i])
        note_sum = 0  
        note_list = []
        for j in range(len(mid.tracks[selected_three_track[i]])):
            if mid.tracks[selected_three_track[i]][j].type == 'note_on' or mid.tracks[selected_three_track[i]][j].type == 'note_off':
                note_sum += mid.tracks[selected_three_track[i]][j].note
                note_num += 1
                note_list.append(mid.tracks[selected_three_track[i]][j].note)
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
            main_melody = selected_three_track[i]

    print('***')
    print( main_melody)

if __name__ == "__main__":
    import os
    from mido import MidiFile
    import time
    dirt_path = os.path.dirname(os.path.realpath(__file__))
    begin = time.time()
    mid = MidiFile(dirt_path+'\\new_song.mid')
    middle = time.time() - begin
    begin = time.time()
    select_theme(mid)
    print(middle) ##計算讀取、分析midi的時間
    print(time.time() - begin) ##計算選取主旋律的track的時間
