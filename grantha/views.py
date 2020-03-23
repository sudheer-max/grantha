from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Package, Bus, Car, About, Testimonial, Counter
from marketing.models import Signup
from django.views.generic import ListView


def navbar(request):
    queryset = Package.objects.filter(featured=True)
    context = {
        'queryset' : queryset
    }
    return render(request, 'navbar.html', context)

def Search(request):
    queryset = Package.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset' : queryset
    }
    return render(request, 'search_result.html', context)


def get_tag_count():
    queryset = Package.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

def get_category_count():
    queryset = Package.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


def home(request):
    featured = Package.objects.filter(featured=True)
    category_count = get_category_count()
    tag_count = get_tag_count()
    pack = Package.objects.all()
    paginator = Paginator(pack, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try : 
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    most_recent = Package.objects.order_by('-timestamp') [0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'queryset' : paginated_queryset,
        'most_recent' : most_recent,
        'page_request_var' : page_request_var,
        'category_count' : category_count,
        'tag_count' : tag_count,
        'featured' : featured

    }
    return render(request, 'home.html', context)

def about(request):
    counter_num = Counter.objects.filter(featured=True)
    aboutimage = About.objects.all()
    about = Package.objects.order_by('-timestamp') [0:3]
    featured = Testimonial.objects.filter(featured=True)
    context = {
        'about' : about,
        'featured' : featured,
        'aboutimage' : aboutimage,
        'counter_num' : counter_num
    }
    return render(request, 'about.html', context)



def blog(request, id):
    featured = Package.objects.filter(featured=True)
    category_count = get_category_count()
    tag_count = get_tag_count()
    most_recent = Package.objects.order_by('-timestamp') [0:3]
    pack = get_object_or_404(Package, id=id)
    context = {
        'pack': pack,
        'category_count' : category_count,
        'tag_count' : tag_count,
        'featured' : featured,
        'most_recent' : most_recent
    }
    return render(request, 'blog.html', context)


class busView(ListView):
    model = Bus
    template_name = 'bus.html'

class carView(ListView):
    model = Car
    template_name = 'car.html'




