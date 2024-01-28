import streamlit as st
import speech_recognition as sr


def convert_audio_to_text(audio_file, language):
    # Inisialisasi recognizer
    recognizer = sr.Recognizer()

    # Baca audio menggunakan recognizer
    with sr.AudioFile(audio_file) as audio_data:
        try:
            # Menggunakan Google Web Speech API untuk mengonversi audio ke teks
            audio_data = recognizer.record(audio_data)
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API tidak dapat mengenali audio"
        except sr.RequestError as e:
            return f"Terjadi kesalahan pada request Google Web Speech API: {e}"

def main():
    st.set_page_config(
        page_title="Konversi Audio ke Teks",
        page_icon="🔊",
        layout="wide",  # Pilihan layout: "centered" atau "wide"
        initial_sidebar_state="auto",  # Pilihan: "auto", "expanded", "collapsed"
    )

    st.header("Konversi Audio ke Teks")

    col1, col2 = st.columns(2)

    with col1:
        # st.markdown("<p style='color: red;'>Tekan tombol Konversi untuk melakukan proses konversi dari audio contoh ke teks.</p>", unsafe_allow_html=True)
        # st.markdown("<p style='color: red;'>Jika anda memiliki file audio untuk dikonversi, maka lakukan proses upload/unggah audio pada form yang telah disediakan, selanjutnya silahkan tekan tombol konversi.</p>", unsafe_allow_html=True)
        # Pengguna dapat mengunggah file audio
        uploaded_file = st.file_uploader("Unggah File Audio", type=["wav", "mp3"])
        st.markdown("\n")
        # Menampilkan audio yang diunggah
        if uploaded_file is not None:
            st.markdown("Audio yang Diunggah:")
            st.audio(uploaded_file, format="audio/wav")
        else:
            st.markdown("Audio contoh:")
            audio_data = "contoh.wav"
            st.audio(audio_data, format="audio/wav")


    with col2:
        # Pilihan bahasa menggunakan dropdown
        language_options = {'Bahasa Indonesia': 'id-ID', 'English': 'en-US'}
        selected_language = st.selectbox('Pilih Bahasa', list(language_options.keys()))

    st.markdown("\n")
    # Tombol untuk memulai proses konversi
    if st.button("Konversi", type="primary", use_container_width=True):
        if uploaded_file is not None:
            # Tampilkan animasi loading
            with st.spinner("Sedang mengonversi audio..."):
                # Konversi audio ke teks
                result_text = convert_audio_to_text(uploaded_file, language_options[selected_language])

                # Tampilkan hasil teks
                st.subheader("Hasil Konversi Teks:")
                st.write(result_text)

                # Tampilkan tombol download untuk hasil teks
                st.subheader("Download Hasil Teks")
                st.download_button(
                    label="Download Teks",
                    data=result_text,
                    file_name="hasil_teks.txt",
                    key="download_button",
                )
        else:
            # Tampilkan animasi loading
            with st.spinner("Sedang mengonversi audio..."):
                # Konversi audio ke teks
                result_text = convert_audio_to_text(audio_data, language_options[selected_language])

                # Tampilkan hasil teks
                st.subheader("Hasil Konversi Teks:")
                st.write(result_text)

                # Tampilkan tombol download untuk hasil teks
                st.subheader("Download Hasil Teks")
                st.download_button(
                    label="Download Teks",
                    data=result_text,
                    file_name="hasil_teks.txt",
                    key="download_button",
                )

if __name__ == "__main__":
    main()