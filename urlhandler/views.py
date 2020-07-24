from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ShortUrl
import random, string
# Create your views here.


@login_required(login_url='/login/')
def dashboard(request):
    usr = request.user
    urls = ShortUrl.objects.filter(user=usr)
    return render(request, 'dashboard.html', {'urls': urls})


def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))



@login_required(login_url='/login/')
def generate(request):
    if request.method == 'POST':
        # generate
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = ShortUrl.objects.filter(short_query=short)
            single = bool(request.POST.get('single', False))
            if not check:
                newurl = ShortUrl(
                    user=usr,
                    original_url=original,
                    short_query=short,
                    single_use=single
                )
                newurl.save()
                return redirect(dashboard)
            else:
                messages.error(request, 'Already exists')
                return redirect(dashboard)
        elif request.POST['original']:
            # generate randomly
            usr = request.user
            original = request.POST['original']
            single = bool(request.POST.get('single', False))
            generated = False
            while not generated:
                short = randomgen()
                check = ShortUrl.objects.filter(short_query=short)
                if not check:
                    newurl = ShortUrl(
                        user=usr,
                        original_url=original,
                        short_query=short,
                        single_use=single
                    )
                    newurl.save()
                    return redirect(dashboard)
                else:
                    continue

        else:
            messages.error(request, 'Empty Fields')
            return redirect(dashboard)

    else:
        return redirect('/dashboard')


def home(request, query=None):
    if not query or query is None:
        return render(request, 'home.html')
    else:
        try:
            check = ShortUrl.objects.get(short_query=query)
            check.visits = check.visits + 1
            url_to_redirect = check.original_url
            if check.single_use and check.visits == 1:
                check.delete()
                return redirect(url_to_redirect)
            else:
                check.save()
                return redirect(url_to_redirect)
        except ShortUrl.DoesNotExist:
            return render(request, 'home.html', {'error': 'error'})
