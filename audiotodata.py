import wave
import shutil
import os
import tensorflow

dataArray = [100]
counter0 = 0
counter1 = 0

for x in os.listdir("./training"):
    temp = wave.open("./training/" + x, "rb")
    tempArray = [temp.readframes(temp.getnframes()), temp.getnchannels(), temp.getsampwidth(), temp.getframerate()]
    
    with open("./generated/txt/" + str(counter1),"wb") as f:
            print("Saving " + str(counter1) + "...")
            f.write(tempArray[0])

for a in range(len(dataArray)):
    temp = wave.open("./generated/wav/" + str(counter1) + ".wav", "wb")
    temp.setnchannels(tempArray[1])
    temp.setsampwidth(tempArray[2])
    temp.setframerate(tempArray[3])
    temp.writeframesraw(tempArray[0])
