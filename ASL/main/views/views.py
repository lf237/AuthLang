from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models import Content, CategoryType, Category, Subcategory, ContentCategory, ContentSubcategory
from django import forms
from main.forms import ContentForm, CategoryTypeForm, CategoryForm, SubcategoryForm, ContentCategoryForm, ContentSubcategoryForm


def home(request):
    return render(request, "main/home.html", {'difficulties':  Difficulty.objects.all, 'countries': Country.objects.all})


def content_details(request, id):
    content = Content.objects.get(id=id)
    return render(request, "main/content_details.html", {'content': content})


def category_details(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    return render(request, "main/category_details.html", {'category': category, 'subcategories': Subcategory.objects.filter(category=category)})


def subcategory_details(request, category_slug, subcategory_slug):
    category = Category.objects.get(slug=category_slug)
    subcategory = Subcategory.objects.get(slug = subcategory_slug)
    content_category = ContentCategory.objects.get(category = category)
    content_subcategory = ContentSubcategory.objects.get(subcategory = subcategory)
    contents = Content.objects.filter(id = content_category.content.id).filter(id = content_subcategory.content.id)
    return render(request, "main/subcategory_details.html", {'category': Category.objects.get(slug=category_slug), 'subcategory': subcategory, 'contents': contents})


def content_manager(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = ContentForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/content_form.html', { 'form': form })


def country_manager(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = CountryForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/country_form.html', { 'form': form })


def theme_manager(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = ThemeForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/theme_form.html', { 'form': form })


def difficulty_manager(request):
    if request.method == 'POST':
        form = DifficultyForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = DifficultyForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/difficulty_form.html', { 'form': form })