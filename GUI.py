### CodeFest
##
### Imports
##import tkinter
##
### class definition
##class GUI:
##    def __init__(self):
##    # Main window
##        self.main_window = tkinter.Tk();
##
##    # Create the frame
##        self.grid = tkinter.Frame();
##
##    # Grid for display
##        # Left Column
##        self.header1 = tkinter.Label(self.grid, text = "Speech")
##        self.header1.grid(row = 0, column = 0);
##        self.speech = tkinter.Entry(self.grid, width = 10);
##        self.speech.grid(row = 1, column = 0);
##        
##        # Middle Column
##        self.f_label = tkinter.Label(self.grid, text = "Text Ppt");
##        self.f_label.grid(row = 0, column = 1);
##        self.value = tkinter.StringVar();
##        self.f_output = ScrolledText.Label(self.grid, textvariable = self.value);
##        self.f_output.grid(row = 1, column = 1);
##        
##        # Right Column
##        self.calc_button = tkinter.Label(self.grid, text = "Image");
##        self.calc_button.grid(row = 0, column = 2);
##        #self.quit_button = tkinter.Button(self.grid, text = "Quit", command = self.main_window.destroy);
##        #self.quit_button.grid(row = 1, column = 2);
##        
##    # Pack the frame
##        self.grid.pack();
##
### class instance
##SpeechToText = GUI();


##import tkinter as tk
##import tkinter.scrolledtext as tkst
##
##window = tk.Tk()
##frame1 = tk.Frame(
##    master = window,
##    bg = '#666666'
##)
##frame1.pack(fill='both', expand='yes')
##editArea = tkst.ScrolledText(
##    master = frame1,
##    wrap   = tk.WORD,
##    width  = 20,
##    height = 10
##)
### Don't use widget.place(), use pack or grid instead, since
### They behave better on scaling the window -- and you don't
### have to calculate it manually!
##editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
### Adding some text, to see if scroll is working as we expect it
##editArea.insert(tk.INSERT,
##"""\
##Integer posuere erat a ante venenatis dapibus.
##Posuere velit aliquet.
##Aenean eu leo quam. Pellentesque ornare sem.
##Lacinia quam venenatis vestibulum.
##Nulla vitae elit libero, a pharetra augue.
##Cum sociis natoque penatibus et magnis dis.
##Parturient montes, nascetur ridiculus mus.
##""")
##window.mainloop()

# You need to install pyaudio to run this example
# pip install pyaudio

# Note that you need to record just once. You will not be able to send
# more audio after the initial recording.

from __future__ import print_function
import pyaudio
import tempfile
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback

speech_to_text = SpeechToTextV1(
    username='71dd6be6-883f-40e8-814f-40f37231feed',
    password='Ynn5LyJjrDP6',
    url='https://stream.watsonplatform.net/speech-to-text/api')


# Example using websockets
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_transcription(self, transcript):
        print(transcript)

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

    def on_listening(self):
        print('Service is listening')

    def on_transcription_complete(self):
        print('Transcription completed')

    def on_hypothesis(self, hypothesis):
        print(hypothesis)


mycallback = MyRecognizeCallback()
tmp = tempfile.NamedTemporaryFile()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)

print('recording....')
with open(tmp.name, 'w') as f:
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        f.write(data)

stream.stop_stream()
stream.close()
audio.terminate()
print('Done recording...')

with open(tmp.name) as f:
    speech_to_text.recognize_with_websocket(
        audio=f, recognize_callback=mycallback)
