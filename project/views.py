from django.shortcuts import render

def post_list(request):
    return render(request, 'project/post_list.html', {'values': [['foo', 32], ['bar', 64], ['baz', 96]]})