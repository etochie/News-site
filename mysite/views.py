from django.shortcuts import redirect


def start_page(request):
    return redirect('news:index', permanent=True)
