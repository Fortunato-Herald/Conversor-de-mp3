#  pip install pytube
#  pip install moviepy

from importlib.resources import path
from pytube import YouTube
import moviepy.editor as mp
import re
import os

#  Digite o link do video e o local que deseja salvar o mp3
link = input('Digite o link do video que deseja baixar: ')
path = input('Digite o diretório que deseja salvar o video: ')
yt = YouTube(link)

#  Começa o download  #
print('BAIXANDO...')
ys = yt.streams.filter(only_audio=True).first().download(path)
print('DOWNLOAD COMPLETO!')

#  Converte mp4 para mp3  #
print('CONVERTENDO O ARQUIVO...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('SUCESSO!')