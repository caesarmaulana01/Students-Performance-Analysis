import joblib

# Fungsi untuk preprocessing data
def preprocess_input(data):

    # Membuat fitur interaksi antara jumlah mata kuliah yang disetujui di semester 1 dan 2
    data['Interaction_CU_1st_2nd_Approved'] = data['Curricular_units_1st_sem_approved'] * data['Curricular_units_2nd_sem_approved']

    # Membuat fitur interaksi antara nilai mata kuliah semester 1 dan 2
    data['Interaction_CU_1st_2nd_Grade'] = data['Curricular_units_1st_sem_grade'] * data['Curricular_units_2nd_sem_grade']

    # Menambahkan fitur agregat total mata kuliah yang disetujui
    data['Total_CU_Approved'] = data['Curricular_units_1st_sem_approved'] + data['Curricular_units_2nd_sem_approved']

    # Menghitung nilai rata-rata dari semua mata kuliah
    data['Total_CU_Grade'] = (data['Curricular_units_1st_sem_grade'] + data['Curricular_units_2nd_sem_grade']) / 2

    # Menghapus kolom asli untuk menghindari multikolinearitas dalam model
    columns_to_drop = [
        'Curricular_units_1st_sem_approved',
        'Curricular_units_2nd_sem_approved',
        'Curricular_units_1st_sem_grade',
        'Curricular_units_2nd_sem_grade'
    ]
    data.drop(columns=columns_to_drop, axis=1, inplace=True)

    # Menyalin DataFrame asli untuk mempertahankan dataset awal
    df_baru = data.copy()

    # Standardisasi data
    scaler = joblib.load('model/scaler.joblib')
    X = scaler.transform(df_baru.iloc[:, :26].values)

    return X
