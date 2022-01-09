from typing import Literal
from django.shortcuts import redirect, render,HttpResponse
from .forms import AC, DC_1, DC_2, Channel1, Channel2, POT, Experiment1, ImageForm
from django.contrib import messages
from .getdata import readData
import serial
import time

#Serial begin for arduino
try:
    arduino = serial.Serial('COM3', 9600)
except serial.serialutil.SerialException:
    print('Mega does not connected!!!')

try:
    arduinoNano = serial.Serial('COM5', 9600)
except serial.serialutil.SerialException:
    print('Nano does not connected!!!')

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    form = ImageForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        image = form.save(commit=False)
        image.author = request.user
        image.save()

        messages.success(request,"Image added successfuly")

    return render(request,"dashboard.html",{"form" : form})

def solutions(request):

    data = []

    for i in range(100):
        n = arduino.readline()
        str_n = n.decode()
        string = str_n.rstrip()
        if string != '':
            data.append(int(string))
        time.sleep(0.1)
        #print(string,'\n')

    readData(data)
    
    print("read worked")

    return render(request,"solutions.html")

def getACDC(request):
    form1 = AC(request.POST or None)

    form2 = DC_1(request.POST or None)

    form6 = DC_2(request.POST or None)

    form3 = Channel1(request.POST or None)

    form4 = Channel2(request.POST or None)

    form5 = POT(request.POST or None)

    if request.method == "POST" and "btn1" in request.POST:
        if form1.is_valid():
            data = form1.save(commit=False)
            data.author = request.user
            data.save()
            with open("log.txt","a") as file:
                value = str(data.acInput1)+'\n'
                file.write(value)
    
    if request.method == "POST" and "btn2" in request.POST:
        if form2.is_valid():
            data = form2.save(commit=False)
            data.author = request.user
            data.save()
            with open("log.txt","a") as file:
                value = str(data.dcInput1)+'\n'
                file.write(value)

    if request.method == "POST" and "btn6" in request.POST:
        if form6.is_valid():
            data = form6.save(commit=False)
            data.author = request.user
            data.save()
            with open("log.txt","a") as file:
                value = str(data.dcInput2)+'\n'
                file.write(value)

    if request.method == "POST" and "btn3" in request.POST:
        if form3.is_valid():
            data = form3.save(commit=False)
            data.author = request.user
            data.save()
            with open("log.txt","a") as file:
                value = str(data.Channel1)+'\n'
                file.write(value)
    
    if request.method == "POST" and "btn4" in request.POST:
        if form4.is_valid():
            data = form4.save(commit=False)
            data.author = request.user
            data.save()
            with open("log.txt","a") as file:
                value = str(data.Channel2)+'\n'
                file.write(value)
    
    if request.method == "POST" and "btn5" in request.POST:
        if form5.is_valid():
            data = form5.save(commit=False)
            data.author = request.user
            data.save()
            with open("log.txt","a") as file:
                value = str(data.PotValue)+'\n'
                file.write(value)

    return render(request,"experiments.html",{
    "form1" : form1, 
    "form2" : form2, 
    "form6" : form6, 
    "form3" : form3,
    "form4" : form4, 
    "form5" : form5
    })

def getExperiment1(request):
    form = Experiment1(request.POST or None)

    if request.method == "POST" and "btn2" in request.POST:
        solutions(request)
        return render(request,"solutions.html")

    if request.method == "POST" and "btn1" in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()

            #Flash Messages Condition States
            
            if data.acInput1 > 200000 or data.dcInput1 >7 or data.dcInput2 >7:
                messages.info(request,"Please control max. values that you can enter!!!")

                return render(request,"experiment1.html",{"form" : form})

            if data.Channel1 != 'ab' and data.Channel1 != 'ac' and data.Channel1 !='bd' and data.Channel2 !='e':
                messages.info(request,"Please check nodes that you can select!!!")

                return render(request,"experiment1.html",{"form" : form})

            if data.PotValue != 1000 and data.PotValue != 4400 and data.PotValue != 0:
                messages.info(request,"Please check valid potantiometer values that you can select!!!")

                return render(request,"experiment1.html",{"form" : form})
            
            if data.acInput1 != 0 and data.dcInput1 !=0:
                messages.info(request,"You can not select AC1 and DC1 supplies at the same time!!!")

                return render(request,"experiment1.html",{"form" : form})

            #Data parsing for arduino condition states

            if data.dcInput1 != 0 and data.acInput1 == 0 and data.dcInput2 !=0 and data.Channel1 == 'ac' and data.Channel2 == 'e' and data.PotValue == 0:
                #relay = "01001000" + str(data.dcInput1) + str(data.dcInput2)
                arduino.write(b'0')
                """
                if data.dcInput1 == 1:
                    arduino.write(b'a')
                
                if data.dcInput1 == 2:
                    arduino.write(b'b')

                if data.dcInput1 == 3:
                    arduino.write(b'c')

                if data.dcInput1 == 4:
                    arduino.write(b'd')

                if data.dcInput1 == 5:
                    arduino.write(b'e')

                if data.dcInput1 == 6:
                    arduino.write(b'f')

                if data.dcInput1 == 7:
                    arduino.write(b'g')"""

            if data.dcInput1 != 0 and data.acInput1 ==0 and data.dcInput2 !=0 and data.Channel1 == 'ac' and data.Channel2 == 'e' and data.PotValue == 1000:
                #relay = "01001100" + str(data.dcInput1) + str(data.dcInput2)
                arduino.write(b'1')
                """
                if data.dcInput1 == 1:
                    arduino.write(b'a')
                
                if data.dcInput1 == 2:
                    arduino.write(b'b')

                if data.dcInput1 == 3:
                    arduino.write(b'c')

                if data.dcInput1 == 4:
                    arduino.write(b'd')

                if data.dcInput1 == 5:
                    arduino.write(b'e')

                if data.dcInput1 == 6:
                    arduino.write(b'f')

                if data.dcInput1 == 7:
                    arduino.write(b'g')"""

            if data.dcInput1 != 0 and data.acInput1 ==0 and data.dcInput2 !=0 and data.Channel1 == 'ac' and data.Channel2 == 'e' and data.PotValue == 4400:
                #relay = "01001110"# + str(data.dcInput1) + str(data.dcInput2)
                arduino.write(b'2')
                """
                if data.dcInput1 == 1:
                    arduino.write(b'a')
                
                if data.dcInput1 == 2:
                    arduino.write(b'b')

                if data.dcInput1 == 3:
                    arduino.write(b'c')

                if data.dcInput1 == 4:
                    arduino.write(b'd')

                if data.dcInput1 == 5:
                    arduino.write(b'e')

                if data.dcInput1 == 6:
                    arduino.write(b'f')

                if data.dcInput1 == 7:
                    arduino.write(b'g')"""

            if data.dcInput1 == 0 and data.acInput1 !=0 and data.dcInput2 !=0 and data.Channel1 == 'ac' and data.Channel2 == 'e' and data.PotValue == 0:
                #relay = "11001000"# + str(data.dcInput2) + str(data.acInput1)
                arduino.write(b'3')
                """
                if data.acInput1 == 0:
                    arduinoNano.write(b'a')
                
                if data.acInput1 == 500:
                    arduinoNano.write(b'b')

                if data.acInput1 == 1000:
                    arduinoNano.write(b'c')

                if data.acInput1 == 5000:
                    arduinoNano.write(b'd')

                if data.acInput1 == 10000:
                    arduinoNano.write(b'e')

                if data.acInput1 == 20000:
                    arduinoNano.write(b'f')

                if data.acInput1 == 50000:
                    arduinoNano.write(b'g')

                if data.acInput1 == 75000:
                    arduinoNano.write(b'h')

                if data.acInput1 == 100000:
                    arduinoNano.write(b'k')

                if data.acInput1 == 150000:
                    arduinoNano.write(b'l')

                if data.acInput1 == 200000:
                    arduinoNano.write(b'm')"""

            if data.dcInput1 == 0 and data.acInput1 !=0 and data.dcInput2 !=0 and data.Channel1 == 'ab' and data.Channel2 != 'e' and data.PotValue == 0:
                #relay = "11010000"# + str(data.dcInput2) + str(data.acInput1)
                arduino.write(b'4')
                
                """
                if data.acInput1 == 0:
                    arduino.write(b'a')
                
                if data.acInput1 == 500:
                    arduino.write(b'b')

                if data.acInput1 == 1000:
                    arduino.write(b'c')

                if data.acInput1 == 5000:
                    arduino.write(b'd')

                if data.acInput1 == 10000:
                    arduino.write(b'e')

                if data.acInput1 == 20000:
                    arduino.write(b'f')

                if data.acInput1 == 50000:
                    arduino.write(b'g')

                if data.acInput1 == 75000:
                    arduino.write(b'h')

                if data.acInput1 == 100000:
                    arduino.write(b'k')

                if data.acInput1 == 150000:
                    arduino.write(b'l')

                if data.acInput1 == 200000:
                    arduino.write(b'm')"""

            if data.dcInput1 == 0 and data.acInput1 !=0 and data.dcInput2 !=0 and data.Channel1 == 'bd' and data.Channel2 != 'e' and data.PotValue == 0:
                arduino.write(b'5')
                
                """
                if data.acInput1 == 0:
                    arduino.write(b'a')
                
                if data.acInput1 == 500:
                    arduino.write(b'b')

                if data.acInput1 == 1000:
                    arduino.write(b'c')

                if data.acInput1 == 5000:
                    arduino.write(b'd')

                if data.acInput1 == 10000:
                    arduino.write(b'e')

                if data.acInput1 == 20000:
                    arduino.write(b'f')

                if data.acInput1 == 50000:
                    arduino.write(b'g')

                if data.acInput1 == 75000:
                    arduino.write(b'h')

                if data.acInput1 == 100000:
                    arduino.write(b'k')

                if data.acInput1 == 150000:
                    arduino.write(b'l')

                if data.acInput1 == 200000:
                    arduino.write(b'm')"""

            if data.dcInput1 == 0 and data.acInput1 !=0 and data.dcInput2 ==0 and data.Channel1 == 'ab' and data.Channel2 != 'e' and data.PotValue == 0:
                #relay = "10010000"# + str(data.dcInput2) + str(data.acInput1)
                arduino.write(b'6')
                
                """
                if data.acInput1 == 0:
                    arduino.write(b'a')

                if data.acInput1 == 500:
                    arduino.write(b'b')

                if data.acInput1 == 1000:
                    arduino.write(b'c')

                if data.acInput1 == 5000:
                    arduino.write(b'd')

                if data.acInput1 == 10000:
                    arduino.write(b'e')

                if data.acInput1 == 20000:
                    arduino.write(b'f')

                if data.acInput1 == 50000:
                    arduino.write(b'g')

                if data.acInput1 == 75000:
                    arduino.write(b'h')

                if data.acInput1 == 100000:
                    arduino.write(b'k')

                if data.acInput1 == 150000:
                    arduino.write(b'l')

                if data.acInput1 == 200000:
                    arduino.write(b'm')"""

            if data.dcInput1 == 0 and data.acInput1 !=0 and data.dcInput2 ==0 and data.Channel1 == 'bd' and data.Channel2 != 'e' and data.PotValue == 0:
                #relay = "10110000"# + str(data.dcInput2) + str(data.acInput1)
                arduino.write(b'7')
               
                if data.acInput1 == 0:
                    arduino.write(b'a')
                
                if data.acInput1 == 500:
                    arduino.write(b'b')

                if data.acInput1 == 1000:
                    arduino.write(b'c')

                if data.acInput1 == 5000:
                    arduino.write(b'd')

                if data.acInput1 == 10000:
                    arduino.write(b'e')

                if data.acInput1 == 20000:
                    arduino.write(b'f')

                if data.acInput1 == 50000:
                    arduino.write(b'g')

                if data.acInput1 == 75000:
                    arduino.write(b'h')

                if data.acInput1 == 100000:
                    arduino.write(b'k')

                if data.acInput1 == 150000:
                    arduino.write(b'l')

                if data.acInput1 == 200000:
                    arduino.write(b'm')

            #with open("log.txt","a") as file:
            #    value = str(data.acInput1)+'\n'+str(data.dcInput1)+'\n'+str(data.dcInput2)+'\n'+str(data.Channel1)+'\n'+str(data.Channel2)+'\n'+str(data.PotValue)+'\n'
            #    file.write(value)

    return render(request,"experiment1.html",{"form" : form})
