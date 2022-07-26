
# Server/Client Simple Network
## End of Module Assignment

### Project Description

This project provides an application solution to run a simple client/server network where the user has the ability to send either dictionary (in form of JSON, XML of binary format) or text file to the server. Also, the user has an option to choose whether the dictionary should be encrypted.

### How to Install and Run the Project
Requirements file contains all of the software components required for this project to work as intended. 
The file name is:
```
requirements.txt
```
The main code is in the below directory path.

folder:
```
src
```
files:
```
client.py
server.py
english_wikipedia.txt
```

To run the network code, change directory to "src" folder on your terminal (Git Bash, command line etc.)  and execute the following:
```
$ python server.py
```
Server should be initiated now. 
Open a new terminal (Git Bash, command line etc.) and execute the following:
```
$ python client.py
```
The client should now be connected to your server. Follow the instruction messages on the terminal. 



### Test
Test code runs Python unit test and automated test

Code is in the below directory path.

folder:
```
test 
```
Unit test files:
```
Unit_test_client.py
Unit_test_Server.py
```

Automated test folder
```
test\Automated_test
```
Automated test files:
```
automated_test_sikuli.jar
client.py
server.py
sikulixide-2.0.5.jar
```
Please note due to size limitation on GitHub , sikulixide-2.0.5.jar is not available. You may download directly from sikuli website.
https://raiman.github.io/SikuliX1/downloads.html

Sikuli is generally an open-sourced OCR tool designed for automation. Details of Sikuli can be found on : http://sikulix.com/


#### Credits

Application has been built based on the following resources:

Jennings, N. (2022) Socket Programming in Python (Guide). Available at: https://realpython.com/python-sockets/

Loffer, D. (2020) "Building a Socket Server and Client with Python". Available at: https://morioh.com/p/1d5fd6c04b58
https://realpython.com/python-sockets/


Rockikz, A. (2022) "How to Transfer Files in the Network using Sockets in Python". Available at: https://www.thepythoncode.com/article/send-receive-files-using-sockets-python


### License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2022 Chun Wong, Amr Ibrahim, Barbara Surowiecka


