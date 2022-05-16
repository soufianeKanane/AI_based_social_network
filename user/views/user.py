from django.http import JsonResponse
from user.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def Authentificate(request):
    if request.method == 'POST':
        # create one user
        json_data = json.loads(request.body)
        name=json_data['name']
        age=json_data['age']
        email=json_data['email']
        password=json_data['password']
        userTest = User.nodes.get(email=email)
        if userTest :
            response = {"error":"User Already Exists - You cannot Create By this email"}
            return JsonResponse(response, safe=False)
        else:
            try:
                user = User(name=name,age=age,email=email,password=password)
                user.save()
                response = {
                    "id": user.id,
                }
                return JsonResponse(response)
            except :
                response = {"error":"Error occurred post not created"}
                return JsonResponse(response, safe=False)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email=json_data['email']
        password=json_data['password']
        user = User.nodes.get(email=email,password=password)
        if user :
            response = {
                "id": user.id,
            }
            return JsonResponse(response)
        else:
            response = {"error":"User Not Exists - You can Create  new account"}
            return JsonResponse(response, safe=False)




