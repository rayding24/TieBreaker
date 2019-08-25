from django.shortcuts import render
# from django.http import HttpResponse


def default_map(request):
    title = "MyClub Event Calendar - test"
    datanum = 49.266360
    # return HttpResponse("<h1>%s</h1>" % (title))
    return render(request, 'index.html', {'title':title, 'datanum':datanum})