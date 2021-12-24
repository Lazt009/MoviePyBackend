#third party Libraries
from moviepy.editor import *


#File Imports
from django.conf import settings
from Api import models
from Api import constants


def get_video_from_alphabet(input_word):
    clip_arr = []
    for j, char in enumerate(input_word):
        if char.isalpha():
            charObj = models.Alphabet.objects.get( character = char.capitalize() )
            path = settings.MEDIA_ROOT + "/" + str( charObj.data )
            print("\n\n\nPath - {}\n\n".format(path))
            clip = VideoFileClip(path)
            clip = clip.fx( vfx.speedx, 2.5)
            clip_arr.append(clip)
    merged_clip = concatenate_videoclips(clip_arr)


    return merged_clip 


def get_video_from_word(input_word):

    video_object = models.Word.objects.get(word=input_word)
    print("\n\n\n Video_Object ",video_object,"\n\n")
    video_path = settings.MEDIA_ROOT  + '/' + str( video_object.data )
    print("\n\n\n Video path - ", video_path, "\n\n")
    clip = VideoFileClip(video_path)   
    return clip
   


def isDigit(word):
    digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    if word in digit:
        ind = digit.index(word)
        return ind+1, True
    else:
        return -1, False


def checkSize(clip):
    wd, ht = clip.size
    width_ratio = constants.WIDTH / wd
    height_ratio = constants.HEIGHT / ht
    if width_ratio == 1 and height_ratio == 1:
        return clip
    elif width_ratio == height_ratio:
        clip = clip.resize( width_ratio )
    else:
        clip = clip.resize( max(width_ratio, height_ratio) )
    return clip   


def generateVideo(input_text, word_set):

    processed_word_list = input_text.split()

    clip_list = []
    
    for word in processed_word_list:
        num, flag = isDigit(word)
        if (word in word_set):
            clip = get_video_from_word(word)
        elif flag:
            clip = get_video_from_word( str(num) )
        else:
            clip = get_video_from_alphabet(word)

            
        clip = checkSize(clip)
        clip_list.append(clip)

    merged_video = concatenate_videoclips(clip_list)
    output = settings.MEDIA_ROOT + '/Videos/' + "merged.mp4"
    merged_video.write_videofile( output )
    
    return '/media/Videos/merged.mp4'


if __name__ == '__main__':
    generateVideo("this ball Focus")

