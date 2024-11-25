# # Here's the source code for a basic Railway Management System in Python using SQLite for the database. The system includes functionality for booking tickets, canceling tickets, viewing train schedules, and an admin panel to manage train data.


# # ---

# # Direcilway_system.py

# import sqlite3
# from tabulate import tabulate

# # Database connection
# def connect_db():
#     return sqlite3.connect("database.db")

# # Initialize database
# def init_db():
#     conn = connect_db()
#     cursor = conn.cursor()
#     # Train table
#     cursor.execute('''CREATE TABLE IF NOT EXISTS trains (
#                         train_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         train_name TEXT,
#                         source TEXT,
#                         destination TEXT,
#                         seats INTEGER
#                     )''')
#     # Ticket table
#     cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
#                         ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         train_id INTEGER,
#                         passenger_name TEXT,
#                         FOREIGN KEY (train_id) REFERENCES trains (train_id)
#                     )''')
#     conn.commit()
#     conn.close()

# # Admin functionality
# def add_train():
#     conn = connect_db()
#     cursor = conn.cursor()
#     train_name = input("Enter train name: ")
#     source = input("Enter source station: ")
#     destination = input("Enter destination station: ")
#     seats = int(input("Enter number of seats: "))
#     cursor.execute("INSERT INTO trains (train_name, source, destination, seats) VALUES (?, ?, ?, ?)",
#                    (train_name, source, destination, seats))
#     conn.commit()
#     print("Train added successfully!")
#     conn.close()

# def view_trains():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM trains")
#     trains = cursor.fetchall()
#     print(tabulate(trains, headers=["Train ID", "Train Name", "Source", "Destination", "Seats"], tablefmt="grid"))
#     conn.close()

# # User functionality
# def book_ticket():
#     conn = connect_db()
#     cursor = conn.cursor()
#     passenger_name = input("Enter your name: ")
#     view_trains()
#     train_id = int(input("Enter the train ID to book: "))
#     cursor.execute("SELECT seats FROM trains WHERE train_id = ?", (train_id,))
#     train = cursor.fetchone()
#     if train and train[0] > 0:
#         cursor.execute("INSERT INTO tickets (train_id, passenger_name) VALUES (?, ?)", (train_id, passenger_name))
#         cursor.execute("UPDATE trains SET seats = seats - 1 WHERE train_id = ?", (train_id,))
#         conn.commit()
#         print("Ticket booked successfully!")
#     else:
#         print("No seats available or invalid train ID.")
#     conn.close()

# def cancel_ticket():
#     conn = connect_db()
#     cursor = conn.cursor()
#     ticket_id = int(input("Enter your ticket ID to cancel: "))
#     cursor.execute("SELECT train_id FROM tickets WHERE ticket_id = ?", (ticket_id,))
#     ticket = cursor.fetchone()
#     if ticket:
#         cursor.execute("DELETE FROM tickets WHERE ticket_id = ?", (ticket_id,))
#         cursor.execute("UPDATE trains SET seats = seats + 1 WHERE train_id = ?", (ticket[0],))
#         conn.commit()
#         print("Ticket canceled successfully!")
#     else:
#         print("Invalid ticket ID.")
#     conn.close()

# def view_tickets():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""SELECT tickets.ticket_id, tickets.passenger_name, trains.train_name 
#                       FROM tickets 
#                       JOIN trains ON tickets.train_id = trains.train_id""")
#     tickets = cursor.fetchall()
#     print(tabulate(tickets, headers=["Ticket ID", "Passenger Name", "Train Name"], tablefmt="grid"))
#     conn.close()

# # Menu
# def main():
#     init_db()
#     while True:
#         print("\n--- Railway Management System ---")
#         print("1. View Train Schedule")
#         print("2. Book Ticket")
#         print("3. Cancel Ticket")
#         print("4. View My Tickets")
#         print("5. Admin Panel (Add Train)")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             view_trains()
#         elif choice == "2":
#             book_ticket()
#         elif choice == "3":
#             cancel_ticket()
#         elif choice == "4":
#             view_tickets()
#         elif choice == "5":
#             add_train()
#         elif choice == "6":
#             print("Thank you for using the Railway Management System!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()


# # ---

# # How It Works

# # 1. Database Initialization:

# # The init_db function creates two tables:

# # trains: Stores train details.

# # tickets: Stores booked tickets.




# # 2. Admin Features:

# # add_train: Adds a new train to the system.

# # view_trains: Displays all trains with details.



# # 3. User Features:

# # book_ticket: Allows users to book a ticket for a selected train if seats are available.

# # cancel_ticket: Cancels a ticket and updates seat availability.

# # view_tickets: Displays all booked tickets with passenger and train details.



# # 4. Menu System:

# # The main menu allows users to navigate through the options.





# # ---

# # Running the Project

# # 1. Save the file as railway_system.py.


# # 2. Install dependencies (if not already installed):

# # pip install tabulate


# # 3. Run the script:

# # python railway_system.py




# # ---

# # Let me know if you need additional features or modifications!