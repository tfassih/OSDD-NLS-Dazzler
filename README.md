<h1><p align=center> Open Source Domestic Defense (OSDD) - Non-Lethal Solutions (NLS)  </p></h1>

<h1><p align=center> The Dazzler  </p></h1>

<h2>The dazzler is a tried and true less-than-lethal device that uses lasers to temporarily blind and/or disorient a malicious attacker when given a clear line-of-sight to the target. This allows those that are under potential attack to, at worst, have more time to either escalate with appropriate force relative to the situation, or at best, end a hostile situation without having to use lethal force. This device uses computer vision to detect faces, and is able to discern between different parts of the face. The targeting algorithm focuses on the eyes, and uses a single laser device to "jitter" back and forth between the two eyes of a given target, replicating the same effect as that of a commercial dazzler.</h2>  

The parts required are as follows:

1. An Arduino-capable microcontroller (this includes MEGA2560 and similar)
2. (x2) Servo Motors, doesn't really matter, but I always recommend one with a metal gearbox
3. A breadboard or protoboard (if using a protoboard, you'll be soldering, keep that in mind)
4. At least (x10) solid-core male-to-male wires
5. A USB-A to USB-B cable to transfer data to and power the Arduino
6. A PC with Arduino IDE installed, or VS Code with the Arduino plugin installed; you will need C++ 11 or higher, the Arduino Servo and Serial libraries installed, as well as Numpy and OpenCV for Python
7. A camera setup, doesn't really matter so long as it's internet connected or wired to the host device. It is important to know the field-of-view in degrees and the resolution of the camera in order for the algorithm to accurately calculate relative angles to the video input

<h2>ROADMAP</h2>

~~1. The device is capable of tracking faces, is able to discern the eyes from the rest of the face, and use that data accordingly to set the targeting data for the servos that aim the laser device~~  
~~2. The platform is fully autonomous~~  (WIP: 85%)  
~~3. The source code can be fine-tuned for various camera systems and laser devices~~  
4. The software allows for the uploading of "friendlies" to be excluded from the defense protocol  
5. The software automatically accounts for known entities such as parcel and mail delivery people, the police, EMS and firefighters, etc  
6. The software allows for customization of how "aggressive" the laser jitter behaves  
7. Integration with major IoT providers  

<h2>Test Machine (HOST):</h2>  

OS: **Windows 11**  
CPU: **AMD Ryzen 9 5900X 12-core @ 3.7GHz**  
RAM: **32GB DDR4 CL15**  
GPU: **Nvidia RTX2080 Super 8GB**  
STORAGE: **x2 Samsung m.2 NVMe 4TB**  

<h2>Test Microcontroller</h2>  

Brand: **Elegoo**  
Board: **ATMEGA2560 R3 Arduino-enabled**  

<h2>Test Servo Motors</h2>  

Brand: **TIANKONGRC**  
Model: **MG995**  










