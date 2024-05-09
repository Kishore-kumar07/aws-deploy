from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd

# Create your views here.
def index(request):
    return render(request,'index.html')

def predict_view(request):
    if request.method == 'POST':
        gender = int(request.POST.get('gender'))
        age = int(request.POST.get('age'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        duration = float(request.POST.get('duration'))
        heart_rate = float(request.POST.get('heart_rate'))
        body_temp = float(request.POST.get('body_temp'))

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'Gender': [gender],
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'Duration': [duration],
            'Heart_Rate': [heart_rate],
            'Body_Temp': [body_temp]
        })

        # Load the model from the .pkl file
        model = pickle.load(open('templates/model.pkl','rb'))

        # Use the model to make predictions
        prediction = model.predict(input_data)

        # Handle the prediction as needed (e.g., return it as an HTTP response)
        return HttpResponse(f'Prediction: {prediction}')
    else:
        # Render the form template if it's a GET request
        return render(request, 'index.html')