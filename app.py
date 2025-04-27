import streamlit as st
import pandas as pd
from data_preprocessing import preprocess_input
from prediction import make_prediction

st.title("\U0001F393 Prediksi Dropout Mahasiswa (Prototype)")

# Validasi fungsi
def validate_input(data):
    errors = []
    
    if data['Marital_status'] not in [1, 2, 3, 4, 5, 6]:
        errors.append("Marital Status harus bernilai antara 1 hingga 6.")
    if data['Application_mode'] not in [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57]:
        errors.append("Application Mode tidak valid.")
    if not (0 <= data['Application_order'] <= 9):
        errors.append("Application Order harus antara 0 - 9.")
    if data['Daytime_evening_attendance'] not in [0, 1]:
        errors.append("Attendance hanya 0 (evening) atau 1 (day).")
    if not (0 <= data['Previous_qualification_grade'] <= 200):
        errors.append("Nilai Previous Qualification Grade harus antara 0 - 200.")
    if not (0 <= data['Admission_grade'] <= 200):
        errors.append("Admission Grade harus antara 0 - 200.")
    for field in ['Displaced', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder']:
        if data[field] not in [0, 1]:
            errors.append(f"{field.replace('_', ' ')} hanya bisa 0 atau 1.")
    return errors

# Ambil input dari pengguna
st.header("\U0001F4E5 Masukkan Data Mahasiswa")
data = {}

cols = st.columns(3)
data['Marital_status'] = cols[0].number_input("Marital Status", value=1)
data['Application_mode'] = cols[1].number_input("Application Mode", value=1)
data['Application_order'] = cols[2].number_input("Application Order", value=1)

cols = st.columns(3)
data['Daytime_evening_attendance'] = cols[0].number_input("Attendance (1=Day, 0=Evening)", value=1)
data['Previous_qualification'] = cols[1].number_input("Previous Qualification", value=1)
data['Previous_qualification_grade'] = cols[2].number_input("Previous Qualification Grade", value=130.0)

cols = st.columns(3)
data['Admission_grade'] = cols[0].number_input("Admission Grade", value=140.0)
data['Displaced'] = cols[1].number_input("Displaced (0/1)", value=0)
data['Debtor'] = cols[2].number_input("Debtor (0/1)", value=0)

cols = st.columns(3)
data['Tuition_fees_up_to_date'] = cols[0].number_input("Tuition Fees Up To Date (0/1)", value=1)
data['Gender'] = cols[1].number_input("Gender (1=Male, 0=Female)", value=1)
data['Scholarship_holder'] = cols[2].number_input("Scholarship Holder (0/1)", value=0)

cols = st.columns(2)
data['Age_at_enrollment'] = cols[0].number_input("Age at Enrollment", value=20)
data['Curricular_units_1st_sem_credited'] = cols[1].number_input("1st Sem Credited Units", value=30)

cols = st.columns(2)
data['Curricular_units_1st_sem_enrolled'] = cols[0].number_input("1st Sem Enrolled Units", value=30)
data['Curricular_units_1st_sem_evaluations'] = cols[1].number_input("1st Sem Evaluations", value=6)

cols = st.columns(2)
data['Curricular_units_1st_sem_approved'] = cols[0].number_input("1st Sem Approved Units", value=6)
data['Curricular_units_1st_sem_grade'] = cols[1].number_input("1st Sem Grade", value=13.0)

cols = st.columns(2)
data['Curricular_units_1st_sem_without_evaluations'] = cols[0].number_input("1st Sem Without Evaluations", value=0)
data['Curricular_units_2nd_sem_credited'] = cols[1].number_input("2nd Sem Credited Units", value=30)

cols = st.columns(2)
data['Curricular_units_2nd_sem_enrolled'] = cols[0].number_input("2nd Sem Enrolled Units", value=30)
data['Curricular_units_2nd_sem_evaluations'] = cols[1].number_input("2nd Sem Evaluations", value=6)

cols = st.columns(2)
data['Curricular_units_2nd_sem_approved'] = cols[0].number_input("2nd Sem Approved Units", value=6)
data['Curricular_units_2nd_sem_grade'] = cols[1].number_input("2nd Sem Grade", value=13.0)

cols = st.columns(2)
data['Curricular_units_2nd_sem_without_evaluations'] = cols[0].number_input("2nd Sem Without Evaluations", value=0)
data['GDP'] = cols[1].number_input("GDP", value=1.2)

# Tampilkan data mentah (raw input user)
with st.expander("\U0001F4CA Lihat Data Mahasiswa (Raw Input)"):
    input_df = pd.DataFrame([data])
    st.dataframe(input_df, width=800)

# Prediksi
if st.button("\U0001F50D Prediksi Dropout"):
    validation_errors = validate_input(data)
    if validation_errors:
        st.error("\n".join(validation_errors))
    else:
        processed_input = preprocess_input(input_df)

        with st.expander("\U0001F6E0️ Lihat Data Setelah Preprocessing"):
            st.dataframe(processed_input, width=800)

        result = make_prediction(processed_input)
        result_label = result[0]  # Ambil hasil prediksi

        st.subheader("\U0001F4C8 Hasil Prediksi Dropout")

        if result_label == "Dropout":
            st.error("\U0001F6A8 Mahasiswa **berpotensi dropout**. Perlu perhatian lebih terhadap performa akademik dan faktor non-akademik.")
        else:
            st.success("\u2705 Mahasiswa **tidak berpotensi dropout**. Tetap pantau dan dukung proses belajarnya.")