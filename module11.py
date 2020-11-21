# Introduction to Programming
# Module 11 Assignment #1
# 11/20/20

class Attendee:
    def _init_(self, name, company, state,email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_state(self):
        return self.email

    def _str_(self):
        return 'Name: ' + self.name + '\n' + \
               'Email: ' + self.email

class AttendeeApp:
    def _init_(self, interface, filename):
        self.interface = interface
        self.filename = filename

    def choose(self):
        choice = self.interface.choose()
        [self.add, self.disp_info, self.delete, self.list_all,
         self.list_state, self.quit][choice - 1]()
        if choice != 6:
            return True
        else:
            return False

    def add(self):
        n, c, s, e = self.interface.add()
        self.attendees.append(Attendee(n, c, s,e))

    def disp_info(self):
        self.interface.disp_info(self.attendees)

    def list_all(self):
        self.interface.delete(self.attendees)

    def list_state(self):
        self.interface.list_state(self.attendees)

    def quit(self):
        self.interface.quit()

    def load_attendees(self):
        try:
            file0bj = open(self.filename, 'r')
        except FileNotFoundError:
            file0bj = open(self.filename, 'w')
            file0bj = open(self.filename, 'r')
        lst = []
        for line in file0bj:
            n,c,s,e = line.split('\t')
            e = e.rstrip('\n')
            lst.append(Attendee(n, c, s, e))
        file0bj.close()
        return lst

    def save attendees(self):
        file0bj = open(self, filename, 'w')
        wirte_string = ''
        for person in self.attendees:
            for func in [person.get_name, person.get_company, person.get_state, person.get_email]:
                write_string += func() + '\t'
            write_string = write_string[:-1] + '\n'
        file0bj.write(write_string[:-1])
        file0bj.close()

    def run(self):
        self.attendees = self.load_attendees()
        cont = True
        while cont:
            self.interface.menu()
            cont = self.choose()
        self.save_attendees()

    class Interface:
        def menu(self):
            print('\nMenu:')
            print('(1) Add an attendee')
            print('(2) Display info on an attendee')
            print('(3) Delete an attendee')
            print('(4) List all attendees')
            print('(5) List all attendees from a state')
            print('(6) Quit')

        def choose(self):
            choice = eval(input('\nSelect 1 - 5: '))\
            return choice
        

    
