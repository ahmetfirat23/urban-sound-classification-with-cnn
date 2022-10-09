import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def create_spectogram(y):
    spec = librosa.feature.melspectrogram(y=y)
    spec_conv = librosa.amplitude_to_db(spec, ref=np.max)
    return spec_conv

data = pd.read_csv('UrbanSound8K/metadata/UrbanSound8K.csv')
for idx, row in data.iterrows():
    folder = 'fold{}'.format(row.fold)
    filename = row.slice_file_name
    y, sr = librosa.load('UrbanSound8K/audio/{0}/{1}'.format(folder,filename))
    spec = create_spectogram(y)
    img = librosa.display.specshow(spec)
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                        hspace=0, wspace=0)
    print(filename,filename[:-4])
    plt.savefig('images/{0}/{1}.png'.format(row.fold, filename[:-4]))
    plt.clf()