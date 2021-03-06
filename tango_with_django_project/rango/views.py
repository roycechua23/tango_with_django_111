from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

# Create your views here.
def index(request):
#    userprofilepic="profile_pics/ProfilePicture1.jpg"
#    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"
 #                   ,'profile_pic':userprofilepic}
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'pages':pages_list}
 
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    mediaimage = "profile_pics/cat.jpg"
    return render(request, 'rango/about.html',context={"image":mediaimage})

def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form':form})

def show_category(request, category_name_slug):
    context_dict={}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html',context_dict)

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
    
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
            
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html',context_dict)