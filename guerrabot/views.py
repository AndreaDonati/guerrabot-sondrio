from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {
        "test_text":"PORCODIO!!"
    }
    return render(request, 'index.html', context=context)