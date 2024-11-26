from django.http import JsonResponse

# Create your views here.

def handshake(request):
    if(request.method == 'GET'):
        return JsonResponse({
            "Backend": "Handshake response working"
        })
        
    return JsonResponse({
        "Backend": "HTTP Method Not Allowed"
    })
