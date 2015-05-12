
Requires Python 2.7 installed on the system
Tested on Ubuntu Amazon EC2 instances
 (some issues arise when run on windows environment; not tested on OS X)



Functionalities implemented:

	--> Decentralized joining and leaving
	--> Multithreaded peers (upto 10 clients)
	--> notification for individual clients leaving
	--> heartbeat for peer servers

Steps to run:

1. Start the gateway 
	"$ python gateway.py"
	starts on port 10001

2. start the peer server (starts on port 9009) 

	"$ python peer_server.py
note : only one peer server can be run on one machine

3. start the client

	"$ python chat_client.py <IP address of server/localhost> 9009"



To start another client, start a new terminal and enter same command



Enjoy!


Author : Bhakt Vatsal Trivedi a.k.a dArkPrince

