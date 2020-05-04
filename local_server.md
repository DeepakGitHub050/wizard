# wizard
1. **qr_code.png** := this is the screenshot of the output 
2. **server.py** := python program running on RaspberryPi 


Here we have written a code in python to setup a local server on which user's phone will be connected when they will enter into the hotel's vicinty. According to the uniquely generated identification no. of the user, a QR code will be generated which will be displaying on the particular alloted room for the user. When user will scan the QR code then only he/she will be allowed to open or close the door. If scanned QR code didn't matched then that will not allow the opening of door and will display error message.


Here we have taken one user's ID and according to that QR code is generated. 
The whole setup is running on **Raspberry pi** and its acting as a local server. 
