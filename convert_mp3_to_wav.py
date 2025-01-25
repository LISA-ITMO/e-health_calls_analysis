from pydub import AudioSegment
import glob


def convert_audio(mp3_path, wav_path):
    # Specify input MP3 and output WAV file paths
    mp3_file = mp3_path
    wav_file = wav_path

    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Export as WAV file
    audio.export(wav_file, format="wav")

    print(f"Converted {mp3_file} to {wav_file}")


def convert_all(dirname):
    # Указываем директорию, в которой нужно искать файлы

    i = 1
    for audio in glob.glob(f'{dirname}/**/*.mp3', recursive=False):
        # Формируем путь для выходного WAV файла
        wav_path = f"converted_audio/output_{i}.wav"
        i += 1
        # Вызываем функцию для конвертации и записи файла
        convert_audio(audio, wav_path)


convert_all('/Users/pashkalini/Documents/Yandex.Disk.localized/Теперь тут/ИТМО/Аспирантура/Данные для анализа/Ленинградская область/ЗАПИСИ 122 ЛО/отобранные записи')
