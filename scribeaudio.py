import whisper 
import os 

# Requires ffmpeg to be in PATH 

model = whisper.load_model('base')

if __name__ == "__main__":
  #Process all audio files in the "audio" folder 
  audio_folder = "audio"
  output_folder = "transcripts"
  os.makedirs(output_folder, exist_ok=True)
  if not os.path.exists(audio_folder):
    print(f"Error: Folder '{audio_folder}' not found.")
  else:
    audio_files = [f for f in os.listdir(audio_folder) if f.lower().endswith(('.mp3','.wav','.m4a','.flac','.ogg'))]
    if not audio_files:
      print(f"No audio files have been found under '{audio_folder}'")
    else:
      for audio_file in audio_files:
        audio_path = os.path.join(audio_folder,audio_file)
        print(f'\nProcessing: {audio_file}')
        result = model.transcribe(audio_path)
        output_file = f'{output_folder}/{os.path.splitext(audio_file)[0]}_transcript.txt'
        with open(output_file,'w',encoding='utf-8') as f:
          f.write("="*80 + "\n")
          f.write(f'TMESTAMPED SEGMETNS:\n')
          f.write("="*80 + "\n\n")
          for segment in result['segments']:
            start = segment['start']
            end = segment['end']
            text = segment['text'].strip()
            f.write(f"[{start:.2f} --> {end:.2f}] {text}\n")
          f.write("AUDIO RAW TRANSCRIPT:\n")
          f.write("="*80 + "\n")
          f.write(result['text'])