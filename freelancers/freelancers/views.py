from django.shortcuts import render

# Create your views here.

def freelancers(request):
    return render(request, 'freelancers.html')
def blog(request):
    return render(request, 'blog.html')
def case_studies(request):
    return render(request, 'case_studies.html')
def pricing(request):
    pricing_data = {
        'Web Development': '$1000',
        'Mobile App Development': '$1500',
        'Backend Engineer': '$2000'
    }
    return render(request, "pricing.html", {'pricing.html': pricing_data})
def services(request):
    service_list = ['Web development', 'Mobile App Development','Backend Engineer ']
    return render(request, "services.html", {'services': service_list})
def testimonials(request):
    testimonials_data = {
        'Alice Johnson': 'Excellent service and support',
        'Bob Smith': 'Highly Professional and timely delivery',
    }
    return render(request, "testimonials.html", {'testimonials': testimonials_data})

