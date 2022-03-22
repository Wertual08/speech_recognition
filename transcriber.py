import os
from pocketsphinx import AudioFile, get_model_path



class Transcriber:
    def __init__(self, path: str, lang: str):
        model_path = get_model_path()

        if lang == 'ru':
            config = {
                'verbose': False,
                'audio_file': path,
                'buffer_size': 2048,
                'no_search': False,
                'full_utt': False,
                'hmm': os.path.join(model_path, 'zero_ru.cd_cont_4000'),
                'lm': os.path.join(model_path, 'ru.lm'),
                'dict': os.path.join(model_path, 'ru.dic')
            }
        else:
            config = {
                'verbose': False,
                'audio_file': path,
                'buffer_size': 2048,
                'no_search': False,
                'full_utt': False,
                'hmm': os.path.join(model_path, 'en-us'),
                'lm': os.path.join(model_path, 'en-us.lm.bin'),
                'dict': os.path.join(model_path, 'cmudict-en-us.dict')
            }

        self.__audio = AudioFile(**config)

    def audio(self):
        return self.__audio