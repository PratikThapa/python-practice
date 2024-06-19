# Initialization of seating arrangement
seats = [[False for _ in range(5)]for _ in range(3)]

while True:
            #Prompt user to enter input
            user_input = input("Please enter to view the seats")

            if user_input.lower() == 'exit':
                print("Warning!!! Please enter to view the seating arrangement.")
                break
            elif user_input.strip() != '':
                 print("Please enter 'exit' or press to continue")
                 continue
             
            #Display the seating arrangement
            for row_index, row in enumerate(seats, start = 1):
                row_display = ''.join(['Booked' if seat else ' Available ' for seat in row])
                print(f"Row {row_index}: {row_display}")
               
            
            try:
                row = int(input("Please choose the row (1-3): ")) - 1
                seat = int(input("Please select the seat (1-5) ")) - 1
                
                #Book seat
                if row < 0 or row>=len(seats) or seat < 0 or seat >= len(seats[row]):
                    print("The selected row or seat number is invalid!!! Please try again.")  

                elif seats[row][seat]:
                    print("The seat has been already booked!!! Please select another seat.")

                else:
                    seats[row][seat] = True
                    print("Seat has been booked successfully.")   

            except(ValueError, IndexError):
                print("Sorry, invalid option!!! Please try again.")



