from Server import server
import paho.mqtt.client as mqtt

broker = 'localhost'
client = mqtt.Client()
serv = server.Server()


def on_message(message):
    message_decoded = str(message.payload.decode("utf-8")).split(".")
    if message_decoded[0] != "Client connected" and message_decoded[0] != "Client disconnected":
        if serv.register_card_use(message_decoded[0], message_decoded[1]):
            print("Card use registered.")
        else:
            print("Error while registering card use")
    else:
        print(message_decoded[0])


def connect_to_broker():
    client.connect(broker)
    client.on_message = on_message
    client.loop_start()
    client.subscribe("communication")


def disconnect_from_broker():
    client.loop_stop()
    client.disconnect()


def run_receiver():
    connect_to_broker()
    print_menu()
    disconnect_from_broker()


def action1():
    print("Terminal ID: ")
    number = input()
    if serv.add_terminal(number):
        print("Terminal added.")
    else:
        print("Error while adding terminal.")


def action2():
    print("Terminal ID: ")
    number = input()
    if serv.remove_terminal(number):
        print("Terminal deleted.")
    else:
        print("Error while adding terminal.")


def action3():
    print("Employee first name: ")
    name = input()
    print("Employee surname: ")
    surname = input()
    print("Employee card ID: ")
    number = input()
    if serv.add_employee_card_assignment(number, name, surname):
        print("Employee assigned.")
    else:
        print("Error while assigning employee.")


def action4():
    print("Employee card ID: ")
    number = input()
    if serv.remove_employee_card_assignment(number):
        print("Employee assignment deleted.")
    else:
        print("Error while deleting employee assignment.")


def action5():
    print("Employee card ID: ")
    number = input()
    if serv.generate_employee_report(number):
        print("Report will be generated to a .csv file.")
    else:
        print("Error while generating a report.")


def action6():
    print(serv.terminals)


def action7():
    print(serv.employee_cards)


def action8():
    serv.clean_logs()
    print("Log files cleaned.")


def print_menu():
    while True:
        print("----------------------------------------------------------------")
        print("               Menu             ")
        print("1. Add terminal do the system")
        print("2. Delete terminal from the system")
        print("3. Assign an employee card")
        print("4. Delete an employee card")
        print("5. Generate a work report for a given employee")
        print("6. Print all terminals")
        print("7. Print all employee cards")
        print("8. Clean log files")
        print("9. Exit")
        print("\nChosen number: ")
        choice = input()
        if choice == '1':
            action1()
        if choice == '2':
            action2()
        if choice == '3':
            action3()
        if choice == '4':
            action4()
        if choice == '5':
            action5()
        if choice == '6':
            action6()
        if choice == '7':
            action7()
        if choice == '8':
            action8()
        if choice == '9':
            return 0


if __name__ == "__main__":
    run_receiver()
