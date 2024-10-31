from django.shortcuts import render
from .models import Services_two , Services , Prices , FQA , Testimonials , Pros

def home (request):
    service = Services_two.objects.filter(status=True)
    special_service = Services.objects.filter(status=True)
    price = Prices.objects.filter(status=True)
    fqa = FQA.objects.all()
    testimonial = Testimonials.objects.all()
    pros = Pros.objects.all()

    contexts = {
        "services":service , 
        "special_services":special_service,
        "prices":price,
        "fqas":fqa,
        "testimonials":testimonial,
        "proses":pros
        }
    
    return render(request, "root/index.html" , context=contexts)
