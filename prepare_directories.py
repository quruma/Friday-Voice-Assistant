import os

os.mkdir('settings')
with open('settings/OpenWeatherMapApiKey.txt','w') as file:file.close()

os.mkdir('shared_storage')
os.mkdir('shared_storage/Music')
os.mkdir('shared_storage/Photos')
os.mkdir('shared_storage/Videos')
os.mkdir('shared_storage/Documents')