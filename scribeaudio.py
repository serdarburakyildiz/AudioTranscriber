import whisper 
import os 

# Requires ffmpeg to be in PATH 

model whisper.load_model('base')

if __name__ == "__main__":
  #Process all audio files in the "audio" folder 
  audio_folder = "audio"
  if not os.path.exists(audio_folder):
    print(f"Error: Folder '{audio_folder}' not found.")
  else:
    audio_files [f for f in os.listdir(audio_folder) if f.lower().endswith(('.mp3','.wav','.m4a','.flac','.ogg'))]
    if not audio_files:
      print(f"No audio files have been found under '{audio_folder}'")
    else:
      for audio_file in audio_files:
        audio_path = os.path.join(audio_folder,audio_file)
        print(f'\nProcessing: {audio_file}')
        
  
