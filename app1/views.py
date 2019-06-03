from django.shortcuts import render
from django.utils import timezone
from .models import Complejo
from .forms import ComplejoForm

# Create your views here.
def post_list(request):
    return render(request, 'app1/principal.html', {})

def complejoAdmin(request):
    complejo = Complejo.objects.get(usuario_id='3')
    return render(request, 'app1/view_Complejo.html', {'complejo': complejo})

def complejoUpdate(request):
    if request.method == 'POST':
        form = ComplejoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('app1: update_Complejo')
    else:
        form = ComplejoForm()

    return render(request, 'app1/update_Complejo.html', {'form': form})
    # complejo = Complejo.objects.get(usuario_id='3')
    # return render(request, 'app1/update_Complejo.html', {'complejo': complejo})
