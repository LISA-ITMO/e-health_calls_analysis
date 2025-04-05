from pydub import AudioSegment

# Specify input MP3 and output WAV file paths
mp3_file = file
wav_file = file_1

# Load the MP3 file
audio = AudioSegment.from_mp3(mp3_file)

# Export as WAV file
audio.export(wav_file, format="wav")

print(f"Converted {mp3_file} to {wav_file}")
