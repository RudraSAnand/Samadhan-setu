from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from setu.models import Grievance, Contact


# HTML Page Rendering Views

def home(request):
    return render(request, 'setu/index.html')

def about(request):
    return render(request, 'setu/about.html')

def track(request):
    return render(request, "setu/tracker.html")

def map_view(request):
    return render(request, "setu/map.html")

def admin_panel(request):
    return render(request, "setu/admin_panel.html")

def faq(request):
    return render(request, "setu/faq.html")

def testimonials(request):
    return render(request, "setu/testimonials.html")


# Grievance Submission View (Handles both form and JSON)
@csrf_exempt
def submit(request):
    if request.method == "POST":
        try:
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
                name = data.get("name")
                email = data.get("email")
                phone = data.get("phone")
                adhar = data.get("adhar")
                category = data.get("category")
                title = data.get("title")
                description = data.get("description")
                location = data.get("location")
                image = None  # JSON can't send files
            else:
                name = request.POST.get("name")
                email = request.POST.get("email")
                phone = request.POST.get("phone")
                adhar = request.POST.get("adhar")
                category = request.POST.get("category")
                title = request.POST.get("title")
                description = request.POST.get("description")
                location = request.POST.get("location")
                image = request.FILES.get("image")

            Grievance.objects.create(
                name=name,
                email=email,
                phone=phone,
                adhar=adhar,
                category=category,
                title=title,
                description=description,
                location=location,
                image=image
            )

            return render(request, "setu/index.html", {"success": True})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return render(request, "setu/submit.html")


# Contact Page View (Handles both rendering and submission)
@csrf_exempt
def contact(request):
    if request.method == "POST":
        try:
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
                name = data.get("name")
                email = data.get("email")
                subject = data.get("subject")
                message = data.get("message")
            else:
                name = request.POST.get("name")
                email = request.POST.get("email")
                subject = request.POST.get("subject")
                message = request.POST.get("message")

            Contact.objects.create(name=name, email=email, subject=subject, message=message)

            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({"status": "success", "message": "Contact submitted!"})
            else:
                return render(request, "setu/contact.html", {"success": True})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return render(request, "setu/contact.html")
