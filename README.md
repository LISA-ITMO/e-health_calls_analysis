**Experiment on recognizing patients' emotions when contacting a call-center**

The emotional color of patients ' calls to call-centers, both in regional and specific medical institutions, is an important aspect that affects the quality of services provided. In the context of regional call-centers that serve a large number of requests, analyzing the emotional state of patients can not only increase the level of satisfaction, but also optimize service processes. 

As an experiment on speech and emotion recognition, audio recordings of patients' calls to one of the regional centralized call-centers were taken.

Audi recordings were pre-listened and suitable recordings were manually selected with no defects, personal data, or melodies while waiting for a response. The test audio recordings were divided into 4 categories of emotions used in the Dusha dataset: anger, happiness, neutral emotion and sadness. If it was impossible to determine an emotion unambiguously, 2 emotions were set with priority. Then the audio recordings were converted to WAV format using the appropriate Python libraries, and scripts were written to run the speech and emotions recognition using GigaAM and GigaAM-Emo models.

In future research, we plan to use the GigaAM-Emo model to recognize more call-center records. To improve the quality of the model results, it's needed to perform automated preprocessing of audio recordings, such as depersonalization and selection of only patient's responses from the dialogs, without taking into account the responses of voice assistants, operators, and waiting tunes.

The resulting dataset will be used to build models using machine learning to rank the principles of patient-orineted approach (also 4P-medicine) by assessing patient needs and satisfaction.

