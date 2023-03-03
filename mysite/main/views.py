from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# source: https://www.youtube.com/watch?v=sm1mokevMWk
# 1:17:33
# 2022_09_16: 1:42:52
# 2023_02_16: rewatch cap. 5 - simple forms (1:42:52)
# 2023_ß2_17: cap 6 (custom forms) finished (1:57:07)
# Create your views here.

# when accessing the admin Dashboard via /admin
# username: cg, pw = test1234

# username: cg2, pw tset4321

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):   # save is name of button
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def view(response):
    return render(response, "main/view.html", {})
