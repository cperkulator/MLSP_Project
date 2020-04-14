# This is to read all .flac files in the subdirectory 5536/43363
# python read all files in directory and subdirectories

import os
import fnmatch
##from pathlib import path
## create a new directory https://realpython.com/working-with-files-in-python/#making-directories

audio_file = []
for root, subdirs, filenames in os.walk('/Users/mininga/Documents/MATLAB/MLSP_project/LibriSpeech-dev-clean/dev-clean/5536/43363/'):#ok

    for file in filenames:

        if '.flac' in file:
            audio_file = root + '/' + file
        
            print 'file=', audio_file
            print '\n'

            data, samplerate = sf.read(audio_file)
            print 'data=', data
            print 'samplerate=', samplerate
            
            N = len(data)
            print 'length of the data N=', N
            
            n= data.size #np.linspace(0,N-1,N) #[0:N-1]
            timestep = 1./samplerate
            freq = np.fft.fftfreq(n,d = timestep)#ang_freq = samplerate*n/N

            fft_data = np.fft.fft(data) # calculates fft of the sound files from the path above
            plot3 = plt.figure(3)
            
            plt.subplot(411)

            plt.plot(data)
            plt.title('Titles: Original data, FFT of data, Spectogram, Gaussian filter of Hilber Transform Envelope of Coefficient A of DWT for ' + file) #Original from dev-clean/5536/43363/5536-43363/' + file, fontsize=7)#dev-clean/5536/43363/5536-43363')

            plt.subplot(412)
            plt.plot(freq, abs(fft_data))
            plt.xlabel('Frequency')
            plt.ylabel('Amplitude')
           
            plt.subplot(413)
            Pxx, freqs, bins, im = plt.specgram(data, Fs=samplerate) # calculates the spectrogram of the sound file data from the path above
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
            
            plt.subplot(414)
            dwt_data = pywt.dwt(data, 'db1', 'smooth') # calculates single level discrete wavelet transform, here Daubechie's 1
        
            [cA_5536_43363, cD_5536_43363] = dwt_data
         
        #plt.subplot(515)
            ## Gaussian filter of Hilber Transform Envelope (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html)
            analytic_signal = hilbert(cA_5536_43363)
            amplitude_envelope = np.abs(analytic_signal)
            gauss_hilber = sp.ndimage.filters.gaussian_filter1d(amplitude_envelope, sigma = 50, order = 0) # ideal is 35
            
            #peaks,_ = find_peaks(gauss_hilber,width = 800)#prominence=1)#,distance=1000)#, height=.025)
            #print 'number of peaks = ', peaks

			plt.plot(gauss_hilber) #plt.plot(y_gauss)
            
            plt.xlabel('Sampling Points')
            plt.ylabel('Amplitude')

            plt.show()

