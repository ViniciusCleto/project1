from django.shortcuts import render

from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    htmlContent = util.convert_mdToHtml(title)
    if htmlContent == None:
        return render(request, "encyclopedia/error.html", {
            "errorMsg": "This entry does not exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": htmlContent
        })

def search(request):
    if request.method == "POST":
        entrySearch = request.POST['q']
        htmlContent = util.convert_mdToHtml(entrySearch)
        if htmlContent is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entrySearch,
                "content": htmlContent
            })
        else:
            qSearchList = []
            entryList = util.list_entries()
            for entry in entryList:
                if entrySearch.lower() in entry.lower():
                    qSearchList.append(entry)
            return render(request, "encyclopedia/search.html", {
                "qSearchList": qSearchList
            })

def createPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create-page.html")
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['newPageContent']
        titleEntries = util.get_entry(title)
        if titleEntries is not None:
            return render(request, "encyclopedia/error.html", {
                "errorMsg": "A page with this title already exists"
            })
        else:
            util.save_entry(title, content)
            htmlContent = util.convert_mdToHtml(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": htmlContent
            })

def editPage(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        if content is None:
            return render(request, "encyclopedia/error.html", {
                "errorMsg": "This entry does not exist!"
            })
        return render(request, "encyclopedia/edit-page.html", {
            "title": title,
            "content": content
        })
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['newPageContent']
        util.save_entry(title, content)
        htmlContent = util.convert_mdToHtml(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": htmlContent
        })

def savePage(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['newPageContent']
        util.save_entry(title, content)
        htmlContent = util.convert_mdToHtml(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": htmlContent
        })

def randomPage(request):
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "errorMsg": "No entries found!"
        })
    randomEntry = random.choice(entries)
    htmlContent = util.convert_mdToHtml(randomEntry)
    return render(request, "encyclopedia/entry.html", {
        "title": randomEntry,
        "content": htmlContent
    })