from django.shortcuts import render, redirect
from .forms import AdmissionForm

# ================= PAGES =================

def home(request):
    return render(request, 'main/home.html')  # ROOT URL

def about(request):
    return render(request, 'main/about.html')  # About page

def news(request):
    return render(request, 'main/news.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def academics(request):
    return render(request, 'main/academics.html')

def student_life(request):
    return render(request, 'main/student_life.html')

def careers(request):
    return render(request, 'main/careers.html')

def contact(request):
    return render(request, 'main/contact.html')

def courses(request):
    return render(request, 'main/courses.html')

def blog(request):
    return render(request, 'main/blog.html')


# ================= APPLY NOW =================

def apply_now(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apply_success')
    else:
        form = AdmissionForm()

    return render(request, 'main/apply_now.html', {'form': form})


def apply_success(request):
    return render(request, 'main/apply_success.html')
