import pathlib
import whisper


WHISPER_ROOT = pathlib.Path.home() / 'models' / 'openai' / 'whisper'
AUDIO_ROOT = pathlib.Path.home() / 'Projects' / 'talk-to-sql' / 'test_audio'


if __name__ == '__main__':
	model = whisper.load_model('large', device='mps', download_root=str(WHISPER_ROOT))
	for audio_file in AUDIO_ROOT.iterdir():
		script = model.transcribe(str(audio_file))
		print(script['text'])
