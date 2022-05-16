from datetime import datetime
from django.http import HttpResponse, JsonResponse


def sorted_integers(request):
    now = datetime.now()

    numbers = map(lambda item: int(item), request.GET["numbers"].split(","))

    data = {
        "message": "Hola Mundo",
        "date - time": now.strftime("%m %dth %Y - %H:%M"),
        "numbers": sorted(list(numbers)),
    }
    return JsonResponse(data=data, safe=False, json_dumps_params={"indent": 4})


def age_verification(request, name, age):
    menor = f"{name} es menor de edad"
    mayor = f"{name} es mayor de edad"

    message = mayor if age >= 18 else menor

    return HttpResponse(message)
