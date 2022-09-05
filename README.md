# PicoW
Project to realize a weather stadium where the data is displayed on a website. 
A Raspberry Pi PicoW (WLAN) from the Raspberry Pi Foundation UK is used. You need a suitable .UF2 file to be able to use the Pico with Micropython. You will find all relevant information about the PicoW and the commissioning or setup on the Raspberry Pi Foundation website.

The project should make it possible "possibly later" to use measurement data from a sensor and display the data on a website. The website is called up in the browser by calling up the IP address assigned to the PicoW by the router. If necessary, it should also be possible to retrieve data from the Internet. For example, openweathermap can be used to get weather data via an API interface.

A BME280 breakout sensor should be used for the local measurements, since a Micropython library is already available for this. Other sensors such as the BME680 or BME688, etc. cannot currently be used. Reference is made to the special sensor hardware from Pimoroni.com (UK).

For programming the PicoW I recommend the ThonnyIDE, which works well with the Pico via a cable connection. Note: If you use a Chromebook for programming, you must activate the Linux container (developer mode) and ThonnyIDE can then be installed as a Linux version. Furthermore, you must release the interface for Linux every time you connect the Pico or PicoW.

All code used is free (open source) and can be used and adapted as desired. If you install the function to fetch weather data from the Internet, make sure that your API has to be adapted and that your API key is required there. You must also enter the data for the WLAN connection SSID and password in secret.py.
