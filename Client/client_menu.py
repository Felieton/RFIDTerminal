import paho.mqtt.client as mqtt

broker = 'localhost'
client_m = mqtt.Client()
terminal_id = "0"


def call_server(message):
    client_m.publish("communication", message)


def connect_to_broker():
    client_m.connect(broker)
    call_server("Client connected")


def disconnect_from_broker():
    call_server("Client disconnected")
    client_m.disconnect()


def action1():
    print("Card ID: ")
    card_id = input()
    call_server(terminal_id + "." + card_id)
    print("Card use has been simulated.")


def print_menu():
    while True:
        print("1. Simulate card use")
        print("2. Exit")
        choice = input()
        if choice == '1':
            action1()
        if choice == '2':
            return 0


def run_sender():
    connect_to_broker()
    print_menu()
    disconnect_from_broker()


if __name__ == "__main__":
    run_sender()