from django.shortcuts import render


def post_list(requset):
    n = ['Oleg', 'Masha', 'Olya']
    return render(requset, 'blog/index.html', context={'names':n})