from typing import Dict

from GigaAM import gigaam

model = gigaam.load_model('emo')
emotion2prob: Dict[str, int] = model.get_probs("converted_audio/output_2.wav")

print(", ".join([f"{emotion}: {prob:.3f}" for emotion, prob in emotion2prob.items()]))