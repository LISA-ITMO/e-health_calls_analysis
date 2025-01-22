from pydub import AudioSegment

# Specify input MP3 and output WAV file paths
mp3_file = ("B:\YandexDisk\Теперь тут\ИТМО\Аспирантура\Данные для анализа\Ленинградская область\ЗАПИСИ 122 ЛО\отобранные записи\/79523774950_Групповой_78136269882_2024_06_10_100455.mp3")
wav_file = "B:\YandexDisk\DISK\ITMO\Aspirantura\Code\Sber_Giga_recognition\giga_recognition\converted_audio\output_2.wav"

# Load the MP3 file
audio = AudioSegment.from_mp3(mp3_file)

# Export as WAV file
audio.export(wav_file, format="wav")

print(f"Converted {mp3_file} to {wav_file}")
