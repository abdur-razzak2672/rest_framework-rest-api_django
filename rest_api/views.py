from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import*
from .serializers import*
from rest_framework.response import Response
from rest_framework.views import APIView

#class based api view

class  ArticleAPIView(APIView):
    def get(self ,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many =True)
        return Response(serializer.data)


    def post(self ,request):
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status =status.HTTP_201_CREATED)
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)







 

#functional view
#@csrf_exempt

#api view
@api_view(['GET','POST'])

def article_list(request):

    if request.method =='GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many =True)
        #return JsonResponse(serializer.data, safe = False) functional view
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = ArticleSerializer(data = data) functional view
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data , status =201)
            return Response(serializer.data , status =status.HTTP_201_CREATED)
        #return JsonResponse(serializer.errors , status =400)
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)



#functional view
#@csrf_exempt


#api view
@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        #return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        #return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data = request.data)

        if serializer.is_valid():
            serializer.save()
        #     return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors , status =400) functional views

            return Response(serializer.data)
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)

        

    elif request.method == 'DELETE':
            article.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
            #return JsonResponse(status =  204)