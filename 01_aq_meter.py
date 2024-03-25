import threading
import time
from guizero import App, Text
from aq import AQ

aq = AQ()
num=5010
num1=20



app = App(title="Air Quality", width=900, height=300, layout="grid",)

def update_readings(): 
    while True:
        temp.value=str(num1)
        eco2_feild.value=str(num)
        eco2=num
        
        if eco2<=250 or eco2<=400:
            app.bg="green"
        
        elif eco2<=401 or eco2<=1000:
            app.bg="blue"
        
        elif eco2<=1000 or eco2<=2000:
            app.bg="yellow"
        
        elif eco2<=2001 or eco2<=5000:
            app.bg="orange"
        
        elif eco2>5000:
            app.bg="red"
            

t1 = threading.Thread(target=update_readings)

aq.leds_automatic()


Text(app, text="Temp (C)", grid=[0,2], size=70)
temp = Text(app, text="-", grid=[1,2], size=110)
Text(app, text="eCO2 (ppm)", grid=[0,4], size=70)
eco2_feild= Text(app, text="-", grid=[1,4], size=110)
t1.start()
app.display()
