from django.shortcuts import render

# Create your views here.

def practice_dtl(request):
    context = {
        'username': 'Usman',
        'no_of_messages': 5,
        'messages': ['hello', 'free to chat chat?', 'when can we talk'],
        'is_logged_in': True,
    }

    return render(request, 'dtl_app/practice-dtl.html', context)
