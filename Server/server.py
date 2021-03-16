import csv
from datetime import datetime


class Server:
    @staticmethod
    def load_from_file(filename):
        db = []
        with open(filename) as csv_file:
            read_csv = csv.reader(csv_file, delimiter=',')
            for row in read_csv:
                db.append(row)
            return db

    @staticmethod
    def load_as_dictionary(filename):
        reader = csv.reader(open(filename, 'r'))
        d = {}
        for row in reader:
            k, v1, v2 = row
            d[k] = v1, v2

        return d

    def __init__(self):
        self.terminals = self.load_from_file('../CSVDatabase/terminals.csv')
        self.employee_cards = self.load_as_dictionary('../CSVDatabase/employee_cards.csv')
        self.employee_cards_uses = self.load_from_file('../CSVDatabase/employee_card_uses.csv')
        self.unknown_card_uses = self.load_from_file('../CSVDatabase/unknown_card_uses.csv')

    @staticmethod
    def update_terminals_file(self):
        with open('../CSVDatabase/terminals.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in self.terminals:
                writer.writerow(row)

    @staticmethod
    def update_em_cards_file(self):
        db = []
        for a, (b, c) in self.employee_cards.items():
            db.append([a, b, c])
        with open('../CSVDatabase/employee_cards.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in db:
                writer.writerow(row)

    @staticmethod
    def update_em_card_uses_file(self):
        with open('../CSVDatabase/employee_card_uses.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in self.employee_cards_uses:
                writer.writerow(row)

    @staticmethod
    def update_u_card_uses_file(self):
        with open('../CSVDatabase/unknown_card_uses.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in self.unknown_card_uses:
                writer.writerow(row)

    def clean_logs(self):
        self.employee_cards_uses.clear()
        self.unknown_card_uses.clear()
        open('../CSVDatabase/employee_card_uses.csv', 'w').close()
        open('../CSVDatabase/unknown_card_uses.csv', 'w').close()

    def add_terminal(self, id_terminal):
        if self.terminals.__contains__([str(id_terminal)]):
            return False
        else:
            self.terminals.append([str(id_terminal)])
            self.update_terminals_file(self)
            return True

    def remove_terminal(self, id_terminal):
        if self.terminals.__contains__([str(id_terminal)]):
            self.terminals.remove([str(id_terminal)])
            self.update_terminals_file(self)
            return True
        else:
            return False

    def add_employee_card_assignment(self, id_card, first_name, surname):
        if str(id_card) in self.employee_cards:
            return False
        else:
            self.employee_cards[str(id_card)] = first_name, surname
            self.update_em_cards_file(self)
            return True

    def remove_employee_card_assignment(self, id_card):
        if str(id_card) not in self.employee_cards:
            return False
        else:
            del self.employee_cards[str(id_card)]
            self.update_em_cards_file(self)
            return True

    def register_card_use(self, id_terminal, id_card):
        if [str(id_terminal)] not in self.terminals:
            return False

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if str(id_card) in self.employee_cards:
            self.employee_cards_uses.append([str(id_terminal), str(id_card), time])
            self.update_em_card_uses_file(self)
        else:
            self.unknown_card_uses.append([str(id_terminal), str(id_card), time])
            self.update_u_card_uses_file(self)

        return True

    def generate_employee_report(self, id_card):
        if str(id_card) not in self.employee_cards:
            return False

        time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        filename = str(id_card) + "_" + str(time) + ".csv"
        appearances = sum(x.count(str(id_card)) for x in self.employee_cards_uses)

        if appearances == 0:
            print("\nEmployee has no record of working")
            return False

        in_out_dates = [0, 0]

        if appearances % 2 != 0:
            appearances -= 1

        file = open(str(filename), "w")
        with open(filename, 'w', newline='') as filee:
            writer = csv.writer(filee)
            for inputs in self.employee_cards_uses:
                if inputs[1] == str(id_card):
                    writer.writerow(inputs)
                    date_obj = datetime.strptime(inputs[2], "%Y-%m-%d %H:%M:%S")
                    in_out_dates[appearances % 2] = date_obj
                    appearances -= 1
                    if appearances % 2 == 0:
                        delta = in_out_dates[1] - in_out_dates[0]
                        writer.writerow(["workspan:", str(delta)])

        file.close()

        return True
