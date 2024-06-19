from django.shortcuts import render

# Create your views here.


def design_page(request):
    return render(request, 'your_design/design.html')