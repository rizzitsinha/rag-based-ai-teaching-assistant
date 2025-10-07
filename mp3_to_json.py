import whisper
import json
import os

model = whisper.load_model('small')

audios = os.listdir('audios')


for audio in audios:
    print(f"{audio} started!!")
    num = audio.split('_')[0]
    title = audio.split('_')[1][:-4]
    result = model.transcribe(audio=f'audios/{audio}',
                            word_timestamps=False,
                            task='translate',
                            language='hi')
    chunks=[]
    for segment in result['segments']:
        chunks.append({'start': segment['start'], 'end': segment['end'], 'id':segment['id'], 'text': segment['text']})

    chunks_with_metadata = {'chunks': chunks, 'text': result['text']}

    with open(f'jsons/{audio}.json', 'w') as f:
        json.dump(chunks_with_metadata, f)
