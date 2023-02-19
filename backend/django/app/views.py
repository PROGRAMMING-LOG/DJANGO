from django.shortcuts import render

from django.views import generic
from django.http import HttpResponse

from package.logger import Logger
log = Logger('/django/app/views.py')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import traceback
import json


class Index(generic.View):
    def get(self, request, *args, **kwargs):
        log.debug('== GET ==')

        return HttpResponse('GET')


class Api(generic.FormView):
    def get(self, request, *args, **kwargs):
        log.debug('== GET ==')

        return JsonResponse({})

    def post(self, request, *args, **kwargs):
        try:
            log.debug('== API POST ==')

            data = json.loads(request.body)
            log.debug(data)

            response = JsonResponse({
                'api': 'API',
                'status': 'success',
            })

            response['Access-Control-Allow-Origin'] = 'http://localhost:1000'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response

        except:
            log.debug('== API POST ERROR ==')
            traceback.print_exc()

            response = JsonResponse({
                'api': 'API',
                'status': 'error',
            })

            response['Access-Control-Allow-Origin'] = 'http://localhost:1000'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = 'http://localhost:1000'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, X-CSRFToken'
        return response

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Api, self).dispatch(*args, **kwargs)
