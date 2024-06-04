class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        Star_Cinema.__hall_list.append(hall)
    @classmethod
    def get_halls(cls):
        return Star_Cinema.__hall_list

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = []
        for _ in range(self.__rows):
            col = []
            for _ in range(self.__cols):
                col.append(0)
            self.__seats[id].append(col) 

    def book_seats(self, id, seats_to_book):
        show_ids = [show[0] for show in self.__show_list]
        if id not in show_ids:
            print(f"\nInvalid show ID: {id}")
            return

        for (row, col) in seats_to_book:
            if row >= self.__rows or col >= self.__cols:
                print(f"\nInvalid seat ({row}, {col})")
                return
            if self.__seats[id][row][col] == 1:
                print(f"\nSeat ({row}, {col}) is already booked")
                return
        for (row, col) in seats_to_book:
            if 0 <= row < self.__rows and 0 <= col < self.__cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
        print(f"\nSeats {seats_to_book} booked for show {id}")

    def view_show_list(self):
        print("\nCurrent shows running:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"\nInvalid show ID: {id}")
            return
        print(f"\nAvailable seats for show ID {id}:")
        for row in range(self.__rows):
            row_status = []
            for col in range(self.__cols):
                if self.__seats[id][row][col] == 1:
                    seat_status = 1
                elif self.__seats[id][row][col] == 0:
                    seat_status = 0
                row_status.append(seat_status)
            print(row_status)

CinemaHall = Star_Cinema()
auditoriam = Hall(7, 7, 1)

auditoriam.entry_show("111", "Jawan Majhi", "11:00")
auditoriam.entry_show("333", "Sujon Majhi", "2:00")

while True:
    currentUser = "customer"
    run = True
    while run:
        if currentUser == 'customer':
            print("\nOptions: ")
            print("1 : View all shows today")
            print("2 : View available seats")
            print("3 : Book ticket")
            print("4 : Logout")

            ch = int(input("\nEnter Option: "))

            if ch == 1:
                halls = Star_Cinema.get_halls()
                for hall in halls:
                    hall.view_show_list()

            elif ch == 2:
                show_id = input("\nEnter show ID: ")
                halls = Star_Cinema.get_halls()
                for hall in halls:
                    hall.view_available_seats(show_id)

            elif ch == 3:
                show_id = input("\nEnter show ID: ")
                num_seats = int(input("Enter number of seats to book: "))
                seats_to_book = []
                for _ in range(num_seats):
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    seats_to_book.append((row, col))
                halls = Star_Cinema.get_halls()
                for hall in halls:
                    hall.book_seats(show_id, seats_to_book)

            elif ch == 4:
                run = False
                currentUser = None
    if not run:
        currentUser = "admin"
        run = True
        