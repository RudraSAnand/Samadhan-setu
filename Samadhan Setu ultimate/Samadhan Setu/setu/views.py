from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Grievance, Contact


# ---- HTML page views ----
def home(request):
    return render(request, 'setu/index.html')

def about(request):
    return render(request, 'setu/about.html')

def submit(request):
    return render(request, 'setu/submit.html')

def track(request):
    return render(request, 'setu/tracker.html')

def map_view(request):
    return render(request, 'setu/map.html')

def contact(request):
    return render(request, 'setu/contact.html')

def admin_panel(request):
    return render(request, 'setu/admin_panel.html')

def faq(request):
    return render(request, 'setu/faq.html')
def testimonials(request):
    return render(request, 'setu/testimonials.html')

# ---- API views ----
@csrf_exempt
def submit_grievance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        adhar = request.POST.get('adhar')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        title = request.POST.get('title')
        message = request.POST.get('message')
        location = request.POST.get('location')
        image = request.FILES.get('image')  

        # Optional: Validate required fields
        if not all([name, adhar, email, phone, category, title, message]):
            return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

        try:
            grievance = Grievance.objects.create(
                name=name,
                adhar=adhar,
                email=email,
                phone=phone,
                category=category,
                title=title,
                message=message,
                location=location,
                image=image
            )
            return redirect('track')
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([name, email, message]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)

        try:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            return JsonResponse({'status': 'success', 'message': 'Contact message submitted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def view_grievances(request):
    grievances = Grievance.objects.all().order_by('-created_at')
    data = [{'name': g.name, 'email': g.email, 'adhar': g.adhar, 'message': g.message} for g in grievances]
    return JsonResponse({'status': 'success', 'grievances': data})

def view_contacts(request):
    contacts = Contact.objects.all().order_by('-created_at')
    data = [{'name': c.name, 'email': c.email, 'message': c.message} for c in contacts]
    return JsonResponse({'status': 'success', 'contacts': data})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Grievance

# Show the HTML page with form
def track_page(request):
    return render(request, "tracker.html")

# This handles the AJAX request from JS
def track_status(request):
    if request.method == "GET":
        track_id = request.GET.get("trackId")

        try:
            grievance = Grievance.objects.get(phone=track_id) if track_id.isdigit() else Grievance.objects.get(id=track_id)
            return JsonResponse({
                "status": grievance.status,
                "date": grievance.submitted_at.strftime("%Y-%m-%d"),
                "department": grievance.category,
                "updated": grievance.submitted_at.strftime("%Y-%m-%d %H:%M"),
            })
        except Grievance.DoesNotExist:
            return JsonResponse({"error": "Complaint not found"}, status=404)
