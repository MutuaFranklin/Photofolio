from gallery.models import Image, Location
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    title ='Home'
    context = {
        "title": title, 
        
    }
    return render(request, 'gallery/index.html',context)

def gallery(request):
    title= 'Gallery'
    images = Image.display_all_image_items()
    locations= Location.display_all_image_locations()

    context = {
        "title": title, 
        "images":images,
        "locations":locations
    }

    return render(request, 'gallery/gallery.html',context)

class LocationView(ListView):
    model= Location
    template_name= 'gallery/gallery.html'


class galleryView(ListView):
    model=Image
    template_name='gallery/gallery.html'

class imageDetailsView(DetailView):
    model=Image
    template_name ='gallery/imageDetails.html'



def image_location(request, location_name):
    images = Image.filter_by_location(location_name)
    print(images)
    return render(request, 'gallery/location.html', {'location_images': images})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")
        # print(search_category)
        searched_category_images = Image.search_by_category(search_category)
        # print(searched_category_images)
        message = f"{search_category}"

        return render(request, 'gallery/search.html',{"message":message,"category_images": searched_category_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
