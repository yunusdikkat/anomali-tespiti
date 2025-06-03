from flask import Flask, render_template, request, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'ag-anomali-tespiti-123'  # Session için gerekli gizli anahtar

# Modeli yükle
model = joblib.load('C:\\Users\\yunus\\Desktop\\Proje Fikirleri\\anomali-tespiti\\models\\ag_anomali_model.pkl')

# Özellik sırası
FEATURES = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Total Length of Fwd Packets',
    'Total Length of Bwd Packets'
]

# Tahmin etiketleri
LABELS = ['BENIGN', 'BruteForce', 'DDoS', 'PortScan']

@app.route('/')
def home():
    return render_template('index.html', history=session.get('history'))

@app.route('/tahmin', methods=['POST'])
def tahmin():
    try:
        # Formdan gelen verileri al
        veri = [float(request.form[f]) for f in FEATURES]
        tahmin_index = model.predict([veri])[0]
        sonuc = LABELS[tahmin_index]

        # Tahmin geçmişini güncelle
        if 'history' not in session:
            session['history'] = []
        session['history'].append(sonuc)
        session.modified = True

        return render_template('index.html', prediction=sonuc, history=session['history'])
    except:
        return render_template('index.html', prediction="❌ Hatalı veri girdiniz.", history=session.get('history'))

if __name__ == '__main__':
    app.run(debug=True)
