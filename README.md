# Friday-Voice-Assistant-BETA
Friday - is a conversational, digital, voice assistant that performs actions based on user's requests and provides with contextual information. 

Friday uses Artificial Inteligence (AI) technologies, such as NLP (natural language processing) and Machine Learning to understand user's requests and fulfill them.


# Prerequisites
## For Windows
```
pip install joblib  
pip install scikit-learn  
pip install pygame  
pip install vosk  
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
git clone https://github.com/sbatman61/Friday-Voice-Assistant.git 
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
Run the __main.py__ to launch Friday. First launch will be the longest, as it will install a few dependencies like transformers models. As default, you can wake Friday by pressing __'alt+q'__, but you can change it in __main.py__ in the __wake_up()__ function. Furthermore, you can even change the mechanics of this function if you want. 

# Note
If you want to retrain this model by yourself, you can use __model_training.py__ file to do that. The only thing you would need to provide is a path to training dataset.
