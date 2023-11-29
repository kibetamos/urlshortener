from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):
    
    return render(request,'index.html')

# def create(request):
#     if request.method == 'POST':
#         link = request.POST['link']
#         uid = str(uuid.uuid4())[:5]
#         new_url = Url(link=link,uuid=uid)
#         new_url.save()
#         return HttpResponse(uid)

def create(request):
    if request.method == 'POST':
        # Get the 'link' parameter from the POST request
        link = request.POST['link']
        
        # Validate the URL
        url_validator = URLValidator()
        try:
            url_validator(link)
        except ValidationError as e:
            # Print the validation error to the console
            print(f"Invalid URL: {e}")
            
            # Return an error response with the validation error message
            return HttpResponse(f"Invalid URL: {e}", status=400)

        # Generate a unique identifier using the uuid module
        uid = str(uuid.uuid4())[:5]
        
        # Create a new Url instance with the provided link and generated uid
        new_url = Url(link=link, uuid=uid)
        
        # Save the new_url instance to the database
        new_url.save()
        
        # Return the shortened URL as the HTTP response
        return HttpResponse(uid)


        
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)