from django.shortcuts import render, redirect
from .models import Personal
from django.contrib import messages

def home(request):
    personals = Personal.objects.all().order_by('-score')
    return render(request, 'home.html', {'personals':personals})

def about(request):
    return render(request, 'about.html', {})

def form(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        age = request.POST['age']
        grade = request.POST['grade']
        score = request.POST['score']
        personals = Personal.objects.create(
            first_name = first_name,
            last_name = last_name,
            age = age,
            grade = grade,
            score = score
        )
        personals.save()
        messages.success(request, "บันทึกเรียบร้อย")
        return redirect('home')
    else:
        return render(request, 'form.html', {})
    
def edit(request, personal_id):
    if request.method == "POST":
        personals = Personal.objects.get(id=personal_id)
        personals.first_name = request.POST['firstname']
        personals.last_name = request.POST['lastname']
        personals.age = request.POST['age']
        personals.grade = request.POST['grade']
        personals.score = request.POST['score']
        personals.save()
        messages.success(request, "แก้ไขเรียบร้อย")
        return redirect('home')
    else:
        personals = Personal.objects.get(id=personal_id)
        return render(request, 'edit.html', {'personals':personals})
    
def delete(request, personal_id):
    personals = Personal.objects.get(pk=personal_id)
    personals.delete()
    messages.success(request, "ลบเรียบร้อย")
    return redirect('home')