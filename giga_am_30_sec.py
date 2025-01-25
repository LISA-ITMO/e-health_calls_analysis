# Базовое использование - распознование речи на коротких аудиозаписях (до 30 секунд)
from GigaAM import gigaam
#
# model = gigaam.load_model("ctc")
# print(model)


def giga_transcript_30_sec(audio):
    model_name = "ctc"  # Options: "v2_ctc" or "ctc", "v2_rnnt" or "rnnt", "v1_ctc", "v1_rnnt"
    model = gigaam.load_model(model_name)
    transcription = model.transcribe(audio)

    return transcription
