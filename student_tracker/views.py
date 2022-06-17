from django.shortcuts import render

from .models import Student


def index(request):
    students = Student.objects.order_by("-name")[:5]
    return render(
        request,
        "student_tracker/index.html",
        {
            "students": students,
        },
    )
