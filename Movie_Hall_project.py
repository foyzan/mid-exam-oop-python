class Star_Cinema:
    Hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.Hall_list.append(hall)

class Hall:

    def __init__(self, rows, cols, hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__shows = []
    
    def entry_show(self, id, move_name, time):
       show = (id,move_name,time)
       self.__shows.append(show)
       free_seats = []
       for i in range(self.__rows):
           r = []
           for j in range(self.__cols):
               r.append(0)
           free_seats.append(r) 
           self.__seats[id] = free_seats
    def book_seats(self, id, seat):
        for show in self.__shows:
            if show[0] == id:
                if seat[0] <= self.__rows and seat[1] <= self.__cols:
                    if self.__seats[id][seat[0]-1][seat[1]-1] == 0:
                        self.__seats[id][seat[0]-1][seat[1]-1] = 1  
                        print()
                        for set in self.__seats[id]:
                            print(*set)
                        print(f"\nYou have succesfully book {seat[0]} row {seat[1]}\n")
                        return
                    else:
                        print(f"\n{seat[0]}:{seat[1]} has aready been booked\n")
                        return
                else:
                    print(f"\nrow {seat[0]} colum {seat[1]} out of range\n")
                    return 
        print(f"\nShow id {id} didn't match\n")
    
    def view_show_list(self):
        for show in self.__shows:
            print(*show)

    def view_availabe_seat(self, id):
        for seat in self.__seats[id]:
            print(*seat)
        




Movie_house = Star_Cinema()
Balak = Hall(4,5,1008)
Movie_house.entry_hall(Balak)
animal = Balak.entry_show("111","Animal", "3:00")
jamul = Balak.entry_show("222", "jamul", "6:50")

Run = None
while True:
    print("__Welcome To Movie House__\n")
    if Run == None:
        print(" 1 : view all shows")
        print(" 2 : view available seats")
        print(" 3 : book tickets in a show")
        print(" 4 : Stop")

        ch = int(input("Enter the Option: "))

        if ch == 1:
            Balak.view_show_list()
        elif ch == 2:
            id = input("Enter the show ID: ")
            Balak.view_availabe_seat(id)
        elif ch == 3:
            id = input("Enter the show ID: ")
            row = int(input("Enter the row number: "))
            col = int(input("Enter the colum number: "))
            Balak.book_seats(id,(row,col))
        elif ch == 4:
            break






        