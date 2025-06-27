from tkinter import *
import tkinter as tk
# tkinter used for GUIs

import requests
# requests used for making https connects and for apis
import time

def getWeather(canvas):
  city=textfield.get()
  api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0213edf0f6147fa817136a0b92ee7e89"
  json_data=requests.get(api).json()
  condition=json_data['weather'][0]['main']
  temperature=int(json_data['main']['temp']-273.15)
  min_temperature=int(json_data['main']['temp_min']-273.15)
  max_temperature=int(json_data['main']['temp_max']-273.15)
  pressure=json_data['main']['pressure']
  humidity=json_data['main']['humidity']
  wind=json_data['wind']['speed']
  sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-20700))
  sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-20700))

  final_info_temp=condition+ "\n"+str(temperature) +"°C"
  final_data_minmax="\n"+"Max temperature:"+str(max_temperature)+"\n"+"Minimum temperature:" +str(min_temperature)+"\n" +"Pressure:"+ str(pressure)+"\n"+ "humidity:"+str(humidity)+"\n"+"Wind speed:"+str(wind)+"\n"+"Sunrise:"+str(sunrise)+"/n"+"Sunset:"+str(sunset)
  label1.config(text=final_info_temp)
  label2.config(text=final_data_minmax)






canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Whether app")

#setting us some fonts
f=("poppins",10,"bold")
t=("poppins",20,"bold")

#when you enter some value its not stored in textfield, you have to do textfield.get()
textfield=tk.Entry(canvas,font= t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1=tk.Label(canvas ,font=t)
label1.pack()
label2=tk.Label(canvas, font=f)
label2.pack()


canvas.mainloop()

  




