from django.shortcuts import render
from django.db.models import Subquery, OuterRef, F, Sum
from .models import Cases
from django.http import JsonResponse
from config.settings import TEMPLATES_DIR


def index(request):
    cases_list = Cases.objects.order_by('-confirmed')
    context = {
        'cases_list': cases_list
    }
    return render(request, TEMPLATES_DIR, context)