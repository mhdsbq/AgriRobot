from urllib import response
import requests
BACKEND_URL = 'http://localhost:3000'

def sync_report_with_backend(report):
    # send post request usig requests library
    # get response and do error management
    pass



def get_latest_disease_data():
    pass

def get_disease_history():
    pass

def post_disease_report(plant_id, disease_name, disease_probability):
    data = {
        'plantId': plant_id,
        'disease': disease_name,
        'diseaseProbability': disease_probability
    }
    response = requests.post(BACKEND_URL + '/disease', json=data)
    return response.text

if __name__ == "__main__":
    print("program started")
    response = post_disease_report(0, 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 0.9)
    print(response)
    print("program ended")
