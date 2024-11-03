from django.shortcuts import render


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# les détails de chaque entries ou sujet 


def entrie(request, entries_id):
    entrie = Topic.objects.get(id=entries_id)
    topic = entrie.topics_set.all()
    context = {'entrie': entrie, "topic":topic}
    return render(request, "encyclopedia/entrie.html", context)

