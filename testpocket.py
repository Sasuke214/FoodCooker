import sys,os
import pyaudio
import wave
 
hmdir = "C:/Python34/Lib/site-packages/pocketsphinx/model/hmm/wsj1"
lmd   = "C:/Python34/Lib/site-packages/pocketsphinx/model/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP"
dictd = "C:/Python34/Lib/site-packages/pocketsphinx/model/lm/wsj/wlist5o.dic"
 
def decodeSpeech(hmmd,lmdir,dictp,wavfile):
 
    import pocketsphinx as ps
    import sphinxbase
 
    speechRec = ps.Decoder(hmm = hmmd, lm = lmdir, dict = dictp)
    wavFile = file(wavfile,'rb')
    wavFile.seek(44)
    speechRec.decode_raw(wavFile)
    result = speechRec.get_hyp()
 
    return result[0]
 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 10
 
for x in range(10):
    fn = "o"+str(x)+".wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(fn, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wavfile = fn
    recognised = decodeSpeech(hmdir,lmd,dictd,wavfile)
    print (recognised)
    cm = 'espeak "'+recognised+'"'
    os.system(cm)
                  
