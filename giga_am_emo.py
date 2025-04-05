import csv
import glob
from typing import Dict
from pydub.utils import mediainfo
from GigaAM import gigaam
from  giga_am_30_sec import giga_transcript_30_sec


def emo_recognition(wav_audio_path):
    model = gigaam.load_model('emo')

    with open(f'{wav_audio_path}/emotions_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Audio', 'Duration', 'Transcription', 'Angry', 'Sad', 'Neutral', 'Positive']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        try:
            for audio in glob.glob(f'{wav_audio_path}/**/*.wav', recursive=True):
                emotion2prob: Dict[str, float] = model.get_probs(audio)

                info = mediainfo(audio)
                duration = float(info['duration'])  # Duration in seconds
                print(duration)

                if duration <= 25.0:
                    row = {'Audio': audio,
                           'Duration': duration,
                           'Transcription': giga_transcript_30_sec(audio),
                           'Angry': f"{emotion2prob.get('angry'):.3f}",
                           'Sad': f"{emotion2prob.get('sad'):.3f}",
                           'Neutral': f"{emotion2prob.get('neutral'):.3f}",
                           'Positive': f"{emotion2prob.get('positive'):.3f}"}
                    writer.writerow(row)

                else:
                    row = {'Audio': audio,
                           'Duration': duration,
                           'Transcription':  "audio is longer than 30 seconds",
                           'Angry': f"{emotion2prob.get('angry'):.3f}",
                           'Sad': f"{emotion2prob.get('sad'):.3f}",
                           'Neutral': f"{emotion2prob.get('neutral'):.3f}",
                           'Positive': f"{emotion2prob.get('positive'):.3f}"}
                    writer.writerow(row)

                print(f'{audio} - ' + ", ".join([f"{emotion}: {prob:.3f}" for emotion, prob in emotion2prob.items()]))
        except ValueError as e:
            print(f"Error occurred in file {audio}: {e}")
        except RuntimeError as e:
            print(f"Error occurred in file {audio}: {e}")


emo_recognition("converted_audio")
