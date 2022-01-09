import matplotlib.pyplot as plt
import serial
import time

#ser = serial.Serial('COM3', 9600)

def readData(data):
    #data = []

    #ser.write(b'!')
    print("matplot working")
    """
    for i in range(100):
        n = ser.readline()
        str_n = n.decode()
        string = str_n.rstrip()
        if string != '':
            data.append(int(string))
        time.sleep(0.1)
        print(string,'\n')"""
    
    print("Red!!!")

    plt.plot(data)
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude(V)')
    plt.title('Plot solutions of current experiment')
    plt.savefig("C:/Users/berkt/OneDrive/Masaüstü/blog/media/wave.png", dpi=80)

    print("Plotted!!!")
