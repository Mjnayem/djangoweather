from django.shortcuts import render

def home(request):
    import json
    import requests


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=B61ABBBE-EFDE-4DED-BC33-B9C29B956E38")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error found"

        return render(request, 'home.html', {'api': api})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=B61ABBBE-EFDE-4DED-BC33-B9C29B956E38")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error found"

        return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})