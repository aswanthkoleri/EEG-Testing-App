from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def test(request):
    return render(request,'test.html')
def feedback(request):
    return render(request,'feedback.html')
    
