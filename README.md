# IoT_Esp32_AWS
ESP32 connection to AWS services (IoT and Alexa)

# HARDWARE
+ ESP32 board, include wifi module
+ BME280/BMP temperature sensor (scl 22, sda 21)
+ Alexa isn't requiered

# SOFTWARE REQUISITES
+ Micropython as supported language for ESP32 (2.15 >= current)
+ IDE - I suggest VSCode and Pymakr extension installed because of the ease of upload entire projects in the board (set extension global settings to the correct port)
+ Linux is suggested because easily manageable and flexible (this guide was developed in Ubuntu 18.04 LTS)

# Projects
+ Alpha donat
First project. It receives boolean values to certain objects, in this case leds. It works if alexa and the ESP32 board are in the same network. In the console will be displayed the temperature data. It doesn't need connection to AWS. The board needs to be connected through the Alexa app, in Devices, '+', Add Device, type Other.


+ Alpha AWS Iot
Project that uses only original firmware modules. The main connects only to the mqtt server we want. It doesn't work with AWS IoT because of TLS (SSL ERROR: "mbedtls_ssl_handshake error: -10") but probably is the best solution for connecting to another server with authentication. In the cert directory there are 3 obsolete not-working certificates connected to the main.py, substitute them with working ones.


+ Alpha firmware donat
Project that uses a custom firmware with added Aws Iot modules. It was made by following [Hackster.io guide](https://www.hackster.io/user3282664/micropython-to-aws-iot-cc1c20). This project needs you to build your own [micropython firmware](https://github.com/micropython/micropython). Linux is highly suggested, follow always documentation and READMEs. Read the notes in boot.py if going in trouble with py module dependecies.


+ Modules and Examples
Contains the bme280 module in py and mpy format and also the boot.py example for connection to the network. 
