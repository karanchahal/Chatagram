# Chatagram


![alt text](/Screenshots/new.gif)
A ChatBot for a bank.
Has the following functionalities.
- [x] Balance check
- [x] User login
- [x] Nearest ATM'S plotted on a map
- [x] Account statement through email
- [x] Mobile Recharge
- [x] Funds Tranfer
- [x] Fixed Deposit Account Opener
- [x] Calculators for Fixed Deposit, Compound Interest and EMI
- [x] A feedback system that upsells products at positive sentiment and apologises for negative sentiment and transfers the conversation to a human operator.
- [x] A speech to text feature for seamless communication


Made using the Watson Conversation API.

# How To Build

Requirements are as follows:
* Python 3.5
* flask
* flask_socketio
* watson_developer_cloud
* requests
* fileinput
* json
* urllib
* PIL
* numpy

All these libraries can be installed using the simple ```pip install <library-name>``` command.
Be sure you are using the pip for python 3.5 and not python 2.7.
Use pip3 if you are on Ubuntu.

Use Ubuntu preferably.


# How to Run

After installing all these dependencies. Navigate to the repo folder through the terminal.
``` python3 server.py``` to start the server.
This will run on port 3110 on localhost.

Now you have to start the client framework made in react, that is ,in the Chatagram-client repository.

Head over there to complete the building process.
