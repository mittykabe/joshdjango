from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
import logging



### LOGGING
logger = logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Mosh'})
    
### CACHING
# class HelloView(APIView):
#     @method_decorator(cache_page(5 * 60))
#     def get(self, request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         return render(request, 'hello.html', {'name': 'Mosh'})



# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': 'Mosh'})


# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key, data)
#     return render(request, 'hello.html', {'name': cache.get(key)})