from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from reversefk.models import Size


class ReverseFK(ListView):
    model = Size
    def get_queryset(self):
        Size.objects.create()
        return Size.objects.filter(orders__user_id=5)
    model = Size


    def post(self, request, *args, **kwargs):
        if request.POST.get('create_user', False):
            #new_user = UserForm(data=request.POST)
            #if new_user.is_valid():
            #    new_user.save()
            return super(ReverseFK, self).get(request, *args, **kwargs)
            # return redirect('/mysite/')
        else:
            return super(ReverseFK, self).get(request, *args, **kwargs)
            # return redirect('/mysite/')