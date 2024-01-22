from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def twohundred(request):
    return render(request, "200hrs.html")

def threehundred(request):
    return render(request, "300hrs.html")

def philosophy(request):
    return render(request, "philosophy.html")

def chakra(request):
    return render(request, "chakra.html")

def cosmic(request):
    return render(request, "cosmic.html")

def natal(request):
    return render(request, "natal.html")

def Contact(request):
    return render(request, "contact.html")

def test(request):
    return render(request, "test.html")

def instructor(request):
    return render(request, "instructor.html")
def sitemap(request):
    return render(request, "sitemap.xml")
def robot(request):
    return render(request, "robot.txt")

def whatsapp(request):
    whatsapp_number = '919008663139'

    # Generate the WhatsApp URL
    whatsapp_url = f'https://api.whatsapp.com/send?phone={whatsapp_number}'

    # Redirect the user to the WhatsApp URL
    return redirect(whatsapp_url)


def Become_A_Healer(request):
    return render(request, "image.html")


def Spiritual_Retreat(request):
    return render(request, "spirit.html")