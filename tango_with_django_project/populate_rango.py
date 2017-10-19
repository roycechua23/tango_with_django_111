# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    
    python_pages = [
            {"title": "Official Python Tutorial",
             "url":"http://docs.python.org/2/tutorial/",
             "views":300,"likes":200},
            {"title": "How to think like a Computer Scientist",
             "url":"http://www.greenteapress.com/thinkpython/",
             "views":232,"likes":190},
            {"title": "http://www.korokithakis.net/tutorials/python/",
             "url":"http://www.korokithakis.net/tutorials/python/",
             "views":100,"likes":30},]
    
    django_pages = [
            {"title":"Official Django Tutorial",
             "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
             "views":232,"likes":190},
            {"title":"Django Rocks",
             "url":"http://www.djangorocks.com/","views":128,"likes":64},
            {"title":"How to Tango with Django",
             "url":"http://www.tangowithdjango.com/","views":300,"likes":200}]

    other_pages = [
            {"title":"Bottle",
             "url":"http://bottlepy.org/docs/dev/","views":128,"likes":64},
            {"title":"Flask",
             "url":"http://flask.pocoo.org","views":128,"likes":64}]

    cats = {"Python": {"pages": python_pages,"views":500,"likes":400},
            "Django": {"pages": django_pages, "views":300,"likes":280},
            "Other Frameworks": {"pages": other_pages,"views":120,"likes":50} }
    
    
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])
        
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"], p["likes"])
            
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
            
def add_page(cat, title, url, views, likes):
    p = Page.objects.get_or_create(category=cat, title=title,
                                   views=views, likes=likes)[0]
    p.url=url
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango Population Script")
    populate()
