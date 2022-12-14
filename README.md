# Friday-Voice-Assistant-BETA
Friday - is a conversational, digital, voice assistant that performs actions based on user's requests and provides with contextual information. 

Friday uses Artificial Intelligence (AI) technologies, such as NLP (natural language processing) and Machine Learning to understand user's requests and fulfill them.


# Prerequisites
## For Windows
Make sure to have suitable version of modules:
```
Python (>=3.5)
NumPy (>= 1.11.0)
Scipy (>= 0.17.0)li.
Joblib (>= 0.11)
Matplotlib (>= 1.5. 1)
Pandas (>= 0.18. 0)
```

I have these versions installed:
```
vosk (0.3.42)  
pyttsx3 (2.90)  
PyAudio (0.2.12)  
pygame (2.1.2)  
joblib (1.1.0)
matplotlib (3.5.2)
scipy (1.9.1)
scikit-learn (1.1.2)
pandas (1.4.2)
transformers (4.17.0)
sentence-transformers (2.2.2)
numpy (1.23.2)
sounddevice (0.4.5)


```

```
pip install pyaudio
pip install joblib  
pip install scikit-learn  
pip install pygame  
pip install vosk  
pip install transofmers
pip install sentence-transformers  
pip install sounddevice  
pip install pyttsx3  
pip install keyboard  
pip install requests
```

# Instalation

## Step 1
You should get an API key from [https://openweathermap.org/](https://openweathermap.org/) (It is free, you just need to sign up 😺).  
It will allow Friday to get weather forecasts.  

## Step 2
Clone repository to your directory:
```
cd <YOUR_DIRECTORY>
git clone https://github.com/quruma/Friday-Voice-Assistant.git
```
## Step 3
Run the file __prepare_directories.py__ to create all necessary files and folders.

## Step 4
Open __Friday-Voice-Assistant/settings/OpenWeatherMapApiKey.txt__ and write in the first line your API key and your region/city (Asia/Baku) in the second line. For example:  
```
<YOUR API KEY>  
Asia/Tokyo  
```

## Step 5
Run the file __main.py__  to launch Friday. First launch will be the longest, as it will install a few dependencies like transformers models. The size of files exceeds 500 MB. As default, you can wake up Friday by pressing __'alt+q'__, but you can change it in __main.py__ in the __wake_up()__ function. Furthermore, you can even change the mechanics of this function if you want. 


# How to use it?

This is just brief description of Friday's functions. You can check full documentation of Friday on the [official site](https://quruma.wixsite.com/friday/documentaiton) 
Yet, there are only 6 functions that Friday is capable to execute:<br><br/>

>1. **Remember_CMD**  
>
(Remembers context information from query)  
for example: __remember__ this address please Branton street one two three (Branton street 123)

>2. **QuestionAnswering_CMD**  
>
(Answer to the question based on what was remembred)  
for example: __answer__ what was that adress

>3. **BrowserSearch_CMD** 
>
(Use query as request of browser search)  
for example: __search__ what is ip adress

>4. **Music_CMD**  
>
(can play the songs by name, play random songs, stop, pause and resume them)  
for example: __play__ sweater weather, __play__ anything, __stop__ the music, __pause__ it for a second, now you can **resume** the song

>5. **Temperature_CMD**  
>
(Using OpenWeatherMap API this function gets needed information about weather forecasts in your region)  
for example: what about the __weather__ today

>6. **Stopwatch_CMD**  
>
(Sets or stops a stopwatch)  
for example: set a stopwatch please, stop a stopwatch  
  
Every function has its own keywords which will make it easier for model to make more accurate predictions of needed function. You can read about them in the [documentaion](https://quruma.wixsite.com/friday/documentaiton) 

# Notes  

## Adapt ML model to your own needs
If you want to retrain the model used in Friday for your own uses, you can use __model_training.py__ file to do that. The only thing you will need to provide is a path to training dataset (which is have to be a csv file). You can read more about this in [documentation]()
## About future updates of Friday
The Friday will use more complex models to calculate the needed functions to be executed. Additionally, it will use more sophisticated NLP technologies to get as more accurate understanding of user's speech as it can without considerable losses in time. Obviously, there will be more functions to execute. However, the most surprising point will be implementing Computer Vision in Friday, which will greatly increase its capabilities.   


Keep all files in the same directories.

Thank you!:3

If you have any problems with instalation or with reposity itself, feel free to cantact me: **_mizu2guruma@gmail.com_**
