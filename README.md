# PicoW
Project to realize a weather stadium where the data is displayed on a website. 
A Raspberry Pi PicoW (WLAN) from the Raspberry Pi Foundation UK is used. You need a suitable .UF2 file to be able to use the Pico with Micropython. You will find all relevant information about the PicoW and the commissioning or setup on the Raspberry Pi Foundation website.

The project should make it possible "possibly later" to use measurement data from a sensor and display the data on a website. The website is called up in the browser by calling up the IP address assigned to the PicoW by the router. If necessary, it should also be possible to retrieve data from the Internet. For example, openweathermap can be used to get weather data via an API interface.

A BME280 breakout sensor should be used for the local measurements, since a Micropython library is already available for this. Other sensors such as the BME680 or BME688, etc. cannot currently be used. Reference is made to the special sensor hardware from Pimoroni.com (UK).

For programming the PicoW I recommend the ThonnyIDE, which works well with the Pico via a cable connection. Note: If you use a Chromebook for programming, you must activate the Linux container (developer mode) and ThonnyIDE can then be installed as a Linux version. Furthermore, you must release the interface for Linux every time you connect the Pico or PicoW.

All code used is free (open source) and can be used and adapted as desired. If you install the function to fetch weather data from the Internet, make sure that your API has to be adapted and that your API key is required there. You must also enter the data for the WLAN connection SSID and password in secret.py.

Status of the version 1.0:
Based on an idea and suggestions from Kevin McAleer, among others. 
First, the temperature sensor data of the temperature sensor on the PicoW Paltine is displayed on the website. Later, either data from Openweathermap and/or the Breakout Sensor BME280 should be displayed. Currently, however, only the data measured for the first time is displayed. So there is no update.

The reason for this is that the code for measuring the temperature is integrated in the main.py code for testing, i.e. it precedes the start of the web server via Phew. The PicoW starts this program via a function such as from boardsensor import temp and otherwise stops. Once the server has started, the measurement is no longer updated. Even if it is programmed as a "While TRUE" loop. This is currently being worked on or refined.
