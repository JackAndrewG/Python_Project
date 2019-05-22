from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'app1/principal.html', {})

def Complejo(request):
    return render(request, 'app1/view_Complejo.html', {})
