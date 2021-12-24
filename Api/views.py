# Django Imports
from django.http.response import HttpResponse
from django.shortcuts import render

# Third Party Imports
import os
from moviepy.editor import *


# Rest Api Framework Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Files Imports(Files in the App) 
from Api import Serializers
from Api import models
from django.conf import settings
from Api import getTextData
from Api import videoCreater

# Utility Functions
def fileDeleter():
    media = os.path.join( settings.MEDIA_ROOT, "Videos" )

    for videos in os.listdir(media):
        if videos != '.buffer-file':
            # print((settings.MEDIA_ROOT + '/Videos/' + videos))
            os.remove( (settings.MEDIA_ROOT + '/Videos/' + videos) )


# Create your views here.
def home(request):
    # cwd = os.getcwd()
    media = os.path.join( settings.MEDIA_ROOT, "Videos" )
    # print(media)/
    D = {}
    for videos in os.listdir(media):
        if videos.endswith('.mp4'):
            D[ videos ] = "path"
    return render(request, "Api/home.html", {"Data" : D})

@api_view(['GET'])
def alphabets(request):
    # Deleting the files which was present prior to this api call
    fileDeleter()

    alphabet = models.Alphabet.objects.all()
    serializer = Serializers.AlphabetSerializer(alphabet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def words(request):
    # Deleting the files which was present prior to this api call
    # fileDeleter()

    word = models.Word.objects.all()
    serializer = Serializers.WordSerializer(word, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def getVideo(request):
    # print(request.data)
    # Deleting the files which was present prior to this api call
    fileDeleter()

    if "text" in request.data.keys():
        #process text here
        text = request.data["text"]

        word = models.Word.objects.all()
        word_set = set()
        for i in word:
            print(i.word)
            word_set.add(i.word)
        print("\n\n\nWord Set : ", word_set)

        processed_data = getTextData.getProcessedDataFromApi(text)
        if processed_data == None:
            return "None"
        else:
            path = videoCreater.generateVideo(processed_data, word_set)
            return HttpResponse(path)
    else:
        return HttpResponse("None")