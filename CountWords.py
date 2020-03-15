def CountWords(file):
    # count number of words per audio file
    trans_f = open(file)

    audio_dict = []

    for line in trans_f:
        audio = line.split(' ')
        entry = {'file':audio[0],"count":len(audio)-1}
        audio_dict.append(entry)
    return audio_dict

if __name__ == "__main__":
    # reference transcript file
    trans = "data/LibriSpeech/dev-clean/84/121123/84-121123.trans.txt"
    
    audio_dict = CountWords(trans)
    print(audio_dict)