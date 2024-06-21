from django.shortcuts import render, redirect
from django.http import HttpResponse
# Importing the helper functions from "util.py"
from .util import list_entries, save_entry, get_entry
# Using the markdown library to convert the content to html
# found that the markdown library is easier to use
# compared to the suggested "markdown2" one.
from markdown import markdown

# Import random to get a random number for the "random_page" funciton
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries()
    })


def wiki(request, article_name):
    # Store the "article_name's" content in "content"
    # "article_name" is provided through the urls.py file, where we have the following implemented:
    # path("wiki/<str:article_name>", views.wiki, name="wiki"),

    content = get_entry(article_name)
    if not content:
        # Returning an HTTP response that shows the 404 message and
        # also indicates it's a 404 with "status=404" at the end of it
        return HttpResponse("<h1>404<br>Page does not exist, please provide a valid wiki-article name</h1>", status=404)
    return render(request, "encyclopedia/wiki.html", {
        "article_name": article_name,
        # Using markdown library to change content to HTML content.
        "content": markdown(content),
    })



def search(request):
    # Check if the "q" parameter is in the URL, meaning a query has been performed
    q = request.GET.get('q')
    if q:
        # If there is a search parameter, then that's basically the article_name
        article_name = q
        content = get_entry(article_name)
        if not content:
            # If the content does not exist, take the user to a search result page
            # that displays encyclopedia entries that have the quert as a substring.
            # i.e. "ango" was searched, we should show a list that shows "Django" as
            # a potential serach result the user was looking for.
            all_entries = list_entries()
            matching_entries = []

            for entry in all_entries:
                if q in entry:
                    matching_entries.append(entry)
            return render(request, "encyclopedia/didyoumean.html", {
                "matching_entries": matching_entries,
                "all_entries": all_entries,
            })
        # If we get content from the get_entry function, then we redirect the user
        # to the "/wiki/article_name" page of that article
        return redirect('wiki', article_name=article_name)
    # If no query is provided, render the index page
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries()
    })


# Create_new_page function for "create_new_page" route
def create_new_page(request):
    if request.method == "POST":
        # Get all current entries
        all_entries = list_entries()
        # Get data from the POST request.
        article_name = request.POST.get('article_name')
        content = request.POST.get('content')
        # Serverside check to see if article_name and content hve been provided
        if not article_name or not content:
                return render(request, "encyclopedia/create_new_page.html", {
                "error": "Please provide a name for the new entry as well as the content for it."

            })
        # Check if title already exists, if so render the same page, but pass in the error.
        # The error will be displayed with a jinja/django templating block in the create_new_page.html page.
        if article_name in all_entries:
            return render(request, "encyclopedia/create_new_page.html", {
                "error": "An entry with this title exists already. Please choose a different title or edit the existing entry."

            })
        # Otherwise safe entry with the title and the content.
        save_entry(article_name, content)
        # Finally redirect to the wiki/article_name page of whatever the name of the article was that we just saved.
        return redirect('wiki', article_name=article_name)


    # If its not a post request, simply render the page.
    return render(request, "encyclopedia/create_new_page.html")


# edit_page function for "edit_page" route
def edit_page(request, article_name):
    if request.method == "POST":
        # Get data from the POST request.
        content = request.POST.get('content')
        # Serverside check to see if content hve been provided
        if not content:
            return render(request, "encyclopedia/edit_page.html", {
                "article_name": article_name,
                # If no content was provided before saving, then we need to retrieve the content again with the get_entry function.
                "content": get_entry(article_name),
                "error": "Please provide content to save changes."

            })

        #  If content has been provided, save the entry.
        save_entry(article_name, content)
        # Finally redirect to the wiki/article_name page of whatever the name of the article was that we just saved.
        return redirect('wiki', article_name=article_name)

    # Store the "article_name's" content in "content"
    # "article_name" is provided through the urls.py file, where we have the following implemented:
    # path("edit_page/<str:article_name>", views.edit_page, name="edit_page"),

    content = get_entry(article_name)
    if not content:
        # Returning an HTTP response that shows the 404 message and
        # also indicates it's a 404 with "status=404" at the end of it
        return HttpResponse("<h1>404<br>Page does not exist, please provide a valid wiki-article name</h1>", status=404)
    return render(request, "encyclopedia/edit_page.html", {
        "article_name": article_name,
        # Using markdown library to change content to HTML content.
        "content": content,
    })

# create_new_page function for "create_new_page" route
def random_page(request):
    all_entries = list_entries()
    random_number = random.randint(0, len(all_entries) -1)
    random_article = all_entries[random_number]

    return redirect('wiki', article_name=random_article)
