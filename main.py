
from multiprocessing import current_process
import threading
import joblib # module for model loading
import os
import requests
import random
import time


# the first line in the file is your OpenWeaterMap API which you can get here:
# the second line is your timezone, which is writen as region/city: for example: Asia/Tokyo https://openweathermap.org/
# for temperature functions
with open("settings\OpenWeatherMapApiKey.txt","r") as file:
    API_KEY = file.readlines()[0].strip('\n')
with open('settings\OpenWeatherMapApiKey.txt','r') as file:
    myTimezone = file.readlines()[1].strip('\n')




# transformers

#  for question answering
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
tokenizer_qa = AutoTokenizer.from_pretrained("csarron/bert-base-uncased-squad-v1")
model_qa = AutoModelForQuestionAnswering.from_pretrained("csarron/bert-base-uncased-squad-v1")
qa_pipeline = pipeline(
    "question-answering",
    model=model_qa,
    tokenizer=tokenizer_qa
)
# for music 
from sentence_transformers import SentenceTransformer, util
model_music = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')
import pygame
pygame.mixer.init()

MyMusicList = os.listdir('shared_storage/Music') # All songs



# for text to speech function
import pyttsx3


# for sppech recognition offline
import argparse
import sounddevice
import webbrowser
import vosk
import sys
import queue
q = queue.Queue()

# loading the model
model_name = 'finalized_model.sav'
my_model = joblib.load(model_name)
modelForMusic = joblib.load('system/Models/forMusic/modelForMusic.sav')


def prepare_voice_recognition():
        global args
        global model
        global dump_fn
        global parser
                
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        def int_or_str(text):
            """Helper function for argument parsing."""
            try:
                return int(text)
            except ValueError:
                return text
        args, remaining = parser.parse_known_args()
        if args.list_devices:
            # print(sounddevice.query_devices())
            parser.exit(0)
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[parser])
        parser.add_argument(
            '-f', '--filename', type=str, metavar='FILENAME',
            help='audio file to store recording to')
        parser.add_argument(
            '-m', '--model', type=str, metavar='MODEL_PATH',
            help='Path to the model')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        args = parser.parse_args(remaining)
        if args.model is None:
            args.model = "model"
            if not os.path.exists(args.model):
                print(args.model)
                print ("Please download a model for your language from https://alphacephei.com/vosk/models")
                print ("and unpack as 'model' in the current folder.")
                parser.exit(0)
            if args.samplerate is None:
                device_info = sounddevice.query_devices(args.device, 'input')
                # soundfile expects an int, sounddevice provides a float:
                args.samplerate = int(device_info['default_samplerate'])

            model = vosk.Model(args.model)

            if args.filename:
                dump_fn = open(args.filename, "wb")
            else:
                dump_fn = None
def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))


# what the user said
def getVoice(toSay = None):
    if toSay:say(toSay)
    global dump_fn
    global args
    global model
    global parser
    with sounddevice.RawInputStream(samplerate=args.samplerate, blocksize = 8000 , device=args.device, dtype='int16',
                            channels=1, callback=callback):
        print('Listening....')
        rec = vosk.KaldiRecognizer(model, args.samplerate)
        while True:
        
            data = q.get()
            # print(len(data))
            if rec.AcceptWaveform(data):
                request = rec.Result()
                print(request)
                if 'text' in request:
                    request =  request[request.index(':')+1:].strip()
                    request = request[1:-3]
                    return (request)
            if dump_fn is not None:
                dump_fn.write(data)
prepare_voice_recognition()                       
    
# while i am speaking, it is True
speaking = False

def getPhrase(type_of_phrase:str):
    phrases = ['None','null']
    if type_of_phrase=='completed':
        phrases = ['it is done',
        'yes, sir',
        'sure',
        'i got you',
        'ok sir',
        'all righty'
    ]
    elif type_of_phrase=='greatings':
        phrases = ['Hello, sir, i am all set up',
        'Hello, sir, i am ready to work',
        'Hey, sir, now i am ready',
        "Let's get to work, i am ready to listen"]
    elif type_of_phrase=='offline':
        phrases = ['sorry sir, to do this you should be connected to the internet',
        'Execuse me, but you are not online',
        'Sorry sir, it is available only online',
        'Sorry sir, but you are offline',
        'Unfortunately, it is not possible now due to offline mode'
        ]
    
    return random.choice(phrases)




# meow functions

# text to speech transformer
def say(sentence): 
    engine = pyttsx3.init()

    engine.say(sentence)
    engine.runAndWait()
    engine.stop()
INTERNET_STATUS = False
# check internet status online=True/offline=False
# it is always running on the background 
def checkOnlineStatus():
    global INTERNET_STATUS
    try:
        if requests.get('https://www.google.com/',timeout=3).status_code==200:
            INTERNET_STATUS= True
        else:
            INTERNET_STATUS = False
    except:    
        INTERNET_STATUS = False


# removes specific redundant words from user_query 
# specifically for function in order to get more accurate results 
def remove_words(stop_words:list, query):
    for word in stop_words:
        if word in query:
            query = query.replace(word, '')
    while '  ' in query:
        query = query.replace('  ',' ')
    return query.strip()



# functions that you can implement to model 
# (if theare is existing dataset with the given function's keywords)


# for example: remebmer this number one two three four
def Remember_CMD():
    query = remove_words(['yo','hey','friday','remember','write','write down','write it down','write down that','write that','note','note that'],user_query)
    with open('system/text/context.txt', 'a') as f:
        f.write(query+'. ')
    current_phrase = 'i remembered this, sir' 
    say(current_phrase)
    return current_phrase

# for example: answer what was that number
def QuestionAnswering_CMD():
    query = remove_words(['yo','hey','friday','answer'],user_query)
    with open('system/text/context.txt', 'r') as f:
        remembered_context = f.read()

    predictions = qa_pipeline({
    'context': remembered_context,
    'question': query
})
    
    current_phrase = predictions.get('answer')
    say(current_phrase)
    return current_phrase
# for example: search what is imaginary number
# for example: search what are two types of current
def BrowserSearch_CMD():
    query = remove_words(['open','search','search for','tell me','tell'],user_query)
    try:
        webbrowser.open(f'https://www.google.com/search?q={query}')
        current_phrase =  getPhrase('completed')
    except:
        current_phrase = getPhrase('offline')
    say(current_phrase)
    return current_phrase
current_state = '' # current state of music, for example: playing, paused, resumed, stoped
# for example: play sweater weather please
# for example: friday, you can now resume
def Music_CMD():
    global current_state
    query = remove_words(['play'],user_query)
    predicted_state = modelForMusic.predict([user_query])[0]
    if predicted_state=='STOP_CMD':
        current_state = 'stop'
        return ('stop')
        
    elif predicted_state=='PAUSE_CMD':
        current_state = 'pause'
        return ('pause')
    elif predicted_state=='RESUME_CMD':
        current_state = 'resume'
        return('unpause')
    else:
        if len(MyMusicList)==0:
            current_phrase =  'I did not find any song in your storage, sir'
            say(current_phrase)
            return current_phrase
        filename = ''
        current_state = 'playing'
        say('playing')
        if predicted_state == 'PLAY_RANDOM_CMD':
            filename = random.choice(MyMusicList)
        else:
            #Encode query and documents
            query_emb = model_music.encode(query)
            doc_emb = model_music.encode(MyMusicList)

            #Compute dot score between query and all document embeddings
            scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()

            #Combine MyMusicList & scores
            doc_score_pairs = list(zip(MyMusicList, scores))

            #Sort by decreasing score
            doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

            filename = doc_score_pairs[0][0]

        pygame.mixer.music.load(f'shared_storage/Music/{filename}')

        if speaking==False:
            print('playing')
            pygame.mixer.music.play()
            while True:
                if speaking:
                    pygame.mixer.music.pause()
                else:
                    if current_state == 'stop':
                        pygame.mixer.music.stop()
                        break
                    elif current_state == 'pause':
                        pygame.mixer.music.pause()
                    else :
                        pygame.mixer.music.unpause()


# for example: what is the weather like today
# for example: what about the temperature
def Temperature_CMD():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = myTimezone.split('/')[1]

    # upadt ing the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    if INTERNET_STATUS:

        try:
            response = requests.get(URL)
            # checking the status code of the request
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']
            current_phrase =  f"It is {report[0]['description']} today, temperature is {round(temperature-273.15,2)} celsius"
            say(current_phrase)
            return current_phrase
        except:
            return 'som'
    else:
        current_phrase = getPhrase('offline')
        say(current_phrase)
        return (current_phrase)


# run the stopwatch please
stopwatch_postition = [0,0,0]
stopwatch_state = ''
def Stopwatch_CMD():
    global stopwatch_postition
    global stopwatch_state
    second = 0
    minute = 0
    hour = 0
    stopwatch_state = True
    if 'stop' in user_query.split():
        stopwatch_state = False
    else:
        stopwatch_state = True
    while stopwatch_state:
        showClock = [hour, minute,second]
        stopwatch_postition=showClock
        print(showClock, end ='\r')
        time.sleep(1)
        if second==59:
            second = 0
            if minute==59:
                minute=0
                hour+=1
            else:
                minute+=1
        else:
            second+=1
    current_phrase = getPhrase('completed')
    say(current_phrase)
    return (current_phrase)
    



# main function to proceed all above

# run selected function
def processing(function_name:str):
    function_result = globals()[str(function_name)]()
    return function_result

# the main functions
def get_prediction():
    function_name = my_model.predict([user_query])[0]
    print(f"Function name: {function_name}")
    print(f"Output: {processing(function_name=function_name)}")


def make_request():
    global user_query
    speaking = True    
    user_query = getVoice()
    speaking = False


# Function to activate Friday's main functions
def wake_up(keys:str):
    import keyboard
    if keyboard.is_pressed(keys):
        return True
    return False

say(getPhrase('greatings'))
checkOnlineStatus()
while True:
    if wake_up('alt+q'):
        # always check internet status
        
        speaking = True #mute all sounds to listnet to user's request
        make_request()
        speaking = False
        
        a = threading.Thread(target = get_prediction)
        a.start()
        internet_check = threading.Thread(target = checkOnlineStatus(),daemon=True)
        internet_check.start()