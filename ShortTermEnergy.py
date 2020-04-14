import librosa
import numpy as np
import matplotlib.pyplot as plt

class ShortTermEnergy:

    @staticmethod
    def CountWords(data, threshold):
        S, phase = librosa.magphase(librosa.stft(data))
        rms = np.squeeze(librosa.feature.rms(S=S))

        rms = rms/max(rms)

        above_thresh = np.ones(len(rms))
        above_thresh[rms<threshold] = 0

        in_thresh = np.where(np.diff(above_thresh.T)>0)

        return len(in_thresh[0])