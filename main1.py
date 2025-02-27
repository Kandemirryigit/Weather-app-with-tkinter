# To send HTTP/HTTPS requests to web servers we should use requests library
import requests 
# From tkinter import everything 
from tkinter import *
# To handle times and dates we should use datetime module
from datetime import datetime
# To opening, editing, and saving images, Supports various image formats 
from PIL import Image, ImageTk
# To create a modern GUI
from tkinter import ttk

window = Tk()  # To define tkinter
window.minsize(800, 550)  # To determine window's size
window.title("Weather")  # To determine window's title

# to create a space for an image
canvas = Canvas(width=800, height=550)
canvas.pack()

# this path is special for my computer.You should write your own path.
img = Image.open("C:/Users/CASPER/Desktop/python_projects/project53/images/blue.png") # Image's path
img = img.resize((800, 550))  # to determine image's size
background_img = ImageTk.PhotoImage(img)

# default center is: center of the screen but in this line I changed it to top left corner
canvas.create_image(0,0,anchor=NW, image=background_img)  # NW: North West
canvas.image = background_img 

# to create an apparence
style = ttk.Style()
style.configure("ModernEntry.TEntry", 
                foreground="black", 
                background="lightblue", 
                font=("Helvetica", 14),
                padding=10)

# to create a search bar
search_entry = ttk.Entry(style="ModernEntry.TEntry", width=50)
search_entry.focus()  # To add a blinking cursor
search_entry.place(x=10, y=10)  # to determine location 
search_entry.insert(0,"Place...")  # To add a default text


# To create texts and determine thir text,font,foreground color,background color and location

location_text=Label(text="Location",font=("Monospace",32,"bold"),fg="red",bg="white")
location_text.place(x=520,y=10)

time_text=Label(text="Time",font=("Monospace",12,"bold"),fg="white",bg="#000080")
time_text.place(x=720,y=10)

date_text=Label(text="Date",font=("Monospace",12,"bold"),fg="white",bg="#000080")
date_text.place(x=720,y=40)

pressure_text=Label(font=("Monospace",15,"bold"),fg="white",bg="#89CFF0")
pressure_text.place(x=525,y=150)

humidity_text=Label(font=("Monospace",15,"bold"),fg="white",bg="#89CFF0")
humidity_text.place(x=525,y=200)

wind_speed_text=Label(font=("Monospace",15,"bold"),fg="white",bg="#89CFF0")
wind_speed_text.place(x=500,y=250)

cloud_status_text=Label(font=("Monospace",15,"bold"),fg="white",bg="#89CFF0")
cloud_status_text.place(x=500,y=300)

celcius_text=Label(font=("Monospace",48,"bold"),fg="#8E2F2F",bg="#89CFF0")
celcius_text.place(x=215,y=190)

feeling_text=Label(font=("Monospace",12,"bold"),fg="white",bg="#89CFF0")
feeling_text.place(x=215,y=270)

two_hours_later_celcius_text=Label(font=("Monospace",24,"bold"),fg="white",bg="#89CFF0")
two_hours_later_celcius_text.place(x=50,y=470)

four_hours_later_celcius_text=Label(font=("Monospace",24,"bold"),fg="white",bg="#89CFF0")
four_hours_later_celcius_text.place(x=195,y=470)

six_hours_later_celcius_text=Label(font=("Monospace",24,"bold"),fg="white",bg="#89CFF0")
six_hours_later_celcius_text.place(x=335,y=470)

eight_hours_later_celcius_text=Label(font=("Monospace",24,"bold"),fg="white",bg="#89CFF0")
eight_hours_later_celcius_text.place(x=475,y=470)

ten_hours_later_celcius_text=Label(font=("Monospace",24,"bold"),fg="white",bg="#89CFF0")
ten_hours_later_celcius_text.place(x=615,y=470)

two_hours_later_text=Label(text="2 hours Later",font=("Monospace",12,"bold"),fg="Black",bg="white")
two_hours_later_text.place(x=50,y=400)

four_hours_later_text=Label(text="4 hours Later",font=("Monospace",12,"bold"),fg="black",bg="white")
four_hours_later_text.place(x=190,y=400)

six_hours_later_text=Label(text="6 hours Later",font=("Monospace",12,"bold"),fg="black",bg="white")
six_hours_later_text.place(x=330,y=400)

eight_hours_later_text=Label(text="8 hours Later",font=("Monospace",12,"bold"),fg="black",bg="white")
eight_hours_later_text.place(x=470,y=400)

ten_hours_later_text=Label(text="10 hours Later",font=("Monospace",12,"bold"),fg="black",bg="white")
ten_hours_later_text.place(x=610,y=400)





weather_images={}  # To store images 

def button():

    place_name = search_entry.get()  # to get search entry's text
    location_text.config(text=place_name.capitalize())  # to capitalize that text
   
    # To send request for location API
    api_key_location =   # your own location API key should be here
    url_location = f"https://api-v2.distancematrix.ai/maps/api/geocode/json?address={place_name}&key={api_key_location}"

    response_location = requests.get(url_location)  # to send requests this specific url
    data = response_location.json()  # To convert response to json type
    
    # To determine the path
    exact_location = data["result"][0]["geometry"]["location"]
    lat = exact_location["lat"]  # To find place_name's lat value
    long = exact_location["lng"] # To find place_name's long value

    # To send request for weather API
    api_key_weather =  # Your own weather API key should be here
    url_weather = f"http://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={long}&type=hour&appid={api_key_weather}"
    
    response_weather = requests.get(url_weather) # to send requests this specific url
    data_weather = response_weather.json()  # To convert response to json type 

    # to find this informations we need this paths
    pressure=data_weather["list"][0]["main"]["pressure"] 
    humidity=data_weather["list"][0]["main"]["humidity"]
    wind_speed=data_weather["list"][0]["wind"]["speed"]
    cloud_status=data_weather["list"][0]["clouds"]["all"]
    weather_id_now=data_weather["list"][0]["weather"][0]["id"]
    kelvin=data_weather["list"][0]["main"]["temp"]
    celcius=kelvin-273.15
    feeling_kelvin=data_weather["list"][0]["main"]["feels_like"]
    feeling_celcius=feeling_kelvin-273.15
    two_hours_later_celcius=(data_weather["list"][2]["main"]["temp"])-273.15
    four_hours_later_celcius=(data_weather["list"][4]["main"]["temp"])-273.15
    six_hours_later_celcius=(data_weather["list"][6]["main"]["temp"])-273.15
    eight_hours_later_celcius=(data_weather["list"][8]["main"]["temp"])-273.15
    ten_hours_later_celcius=(data_weather["list"][10]["main"]["temp"])-273.15

    
    # to change default texts to new texts.
    # Istanbul's text and London's text going to be different we should configure them
    pressure_text.config(text=f"Pressure: {pressure} hPa")
    humidity_text.config(text=f"Humidity: {humidity}%")
    celcius_text.config(text=f"{celcius:.1f} °C")
    feeling_text.config(text=f"Feels {feeling_celcius:.1f} °C")
    wind_speed_text.config(text=f"Wind Speed: {wind_speed} m/sn")
    cloud_status_text.config(text=f"cloud Status: {cloud_status}%")
    # :.1f means show just one chracter after point in float numbers
    two_hours_later_celcius_text.config(text=f"{two_hours_later_celcius:.1f} °C") 
    four_hours_later_celcius_text.config(text=f"{four_hours_later_celcius:.1f} °C")
    six_hours_later_celcius_text.config(text=f"{six_hours_later_celcius:.1f} °C")
    eight_hours_later_celcius_text.config(text=f"{eight_hours_later_celcius:.1f} °C")
    ten_hours_later_celcius_text.config(text=f"{ten_hours_later_celcius:.1f} °C")
    
    
    
    # To send requests for time API
    api_key_time =  # Your own time API key should be here
    url_time = f"http://api.timezonedb.com/v2.1/get-time-zone?key={api_key_time}&format=json&by=position&lat={lat}&lng={long}"
    
    response_time = requests.get(url_time)  # To send requests this specific url
    data_time = response_time.json()  # To converts response json
    exact_time =data_time["formatted"] # Path

    date_object = datetime.strptime(exact_time, "%Y-%m-%d %H:%M:%S")
    year=date_object.year  # To find year information
    month=date_object.month # To find month information
    day=date_object.day  # To find day information
    hour=date_object.hour  # To find hour information
    minute=date_object.minute  # To find minute information

    # To change default text to this specific time informations
    # For example Istanbul and London's time is different
    time_text.config(text=f"{hour}.{minute}")
    date_text.config(text=f"{day}/{month}/{year}")

 
    # To show different pictures in different weather conditions
    image_path = None  # Default image_path is empty
    if weather_id_now >= 200 and weather_id_now <= 232:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/thunderstorm.jpg"
    elif weather_id_now >= 300 and weather_id_now <= 321:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/drizzle.jpg"
    elif weather_id_now >= 500 and weather_id_now <= 531:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/rain.jpg"
    elif weather_id_now >= 600 and weather_id_now <= 622:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/snow.jpg"
    elif weather_id_now >= 701 and weather_id_now <= 781:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/fog.jpg"
    elif weather_id_now == 800:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/clear.jpg"
    elif weather_id_now >= 801 and weather_id_now <= 804:
        image_path = "C:/Users/CASPER/Desktop/python_projects/project53/images/clouds.jpg"

    # If image_path is not in weather_images do this steps and else do not.
    # This is useful for eficciency
    if image_path not in weather_images:
        weather_image = Image.open(image_path)
        resized_image = weather_image.resize((175, 175), Image.LANCZOS)
        weather_images[image_path] = ImageTk.PhotoImage(resized_image)

    label = Label(image=weather_images[image_path], highlightthickness=0)
    label.place(x=15, y=150)


# To create an image
search_image = Image.open("C:/Users/CASPER/Desktop/python_projects/project53/images/search button.jpg")  
resized_search_image = search_image.resize((40, 35), Image.LANCZOS) 
search_photo = ImageTk.PhotoImage(resized_search_image)

# To create a button
label = Button(image=search_photo,highlightthickness=0,command=button)
label.place(x=350,y=10)



window.mainloop()  # If I don't click exit button the screen won't close
