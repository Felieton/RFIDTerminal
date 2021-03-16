# RFIDTerminal
This project is a simple simulation of a system registrating work times of some company's employees.

# About
The system simulates a worker (a RFID card) and a terminal. When RFID card use is registered, system starts measuring working time of the employee. System stores all the data in .csv files. To communicate between client and the server, system uses MQTT Mosquitto broker. The communication is encrypted with TLS protocol using generated certificates both for the client and the server.


*The project was created between Aprill and May 2020.*
