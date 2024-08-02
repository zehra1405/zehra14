from flask import Flask, jsonify, render_template, request
import requests
import os

app = Flask(__name__,template_folder='.')

API_KEY = os.getenv('005ccf3901eb02a42bcbe1aee7ce1e31', '005ccf3901eb02a42bcbe1aee7ce1e31')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city', 'Istanbul')
    country = request.args.get('country', 'TR')
    
    try:
        response = requests.get(BASE_URL, params={
            'q': f'{city},{country}',
            'appid': API_KEY,
            'units': 'metric'
        })
        response.raise_for_status()  # HTTP hataları için kontrol
        
        # JSON verisini alma
        data = response.json()
        
        # Hata kontrolü
        if data.get('cod') != 200:
            return jsonify({'error': data.get('message', 'Bir hata oluştu')}), 400
        
        return jsonify(data)
    
    except requests.RequestException as e:
        return jsonify({'error': f'API isteği sırasında bir hata oluştu: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Genel bir hata oluştu: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
