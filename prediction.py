import joblib

# Fungsi untuk memuat model dan melakukan prediksi
def make_prediction(data):
    # Load model yang sudah dilatih
    model = joblib.load('model/best_model_lr.joblib')

    # Prediksi data menggunakan model yang telah dilatih
    predictions = model.predict(data)

    # Mengubah hasil prediksi menjadi label yang sesuai
    results = ["Dropout" if p == 1 else "No Dropout" for p in predictions]
    return results
