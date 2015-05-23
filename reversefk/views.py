from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from reversefk.models import Size


class ReverseFK(ListView):
    model = Size
    def get_queryset(self):
        Size.objects.create()
        return Size.objects.filter(orders__user_id=5)