from ShortTermEnergy import ShortTermEnergy
import soundfile
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np
from CountWords import CountWords
from pathlib import Path
import GradDescent

speechDict = CountWords("data/LibriSpeech/dev-clean/84/121123/84-121123.trans.txt")
print("Number of words:{}".format(speechDict[2]["count"]))

x, fs = soundfile.read("data/LibriSpeech/dev-clean/84/121123/84-121123-0002.flac")

initial = 1
thresh = GradDescent.gradient_descent(x, initial, 0.01, 49)

count = ShortTermEnergy.CountWords(x, thresh)
print(count)
