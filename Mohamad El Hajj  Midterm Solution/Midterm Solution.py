import datetime
from collections import Counter

class Ticket:
    ticket_count = 100  # Initialize ticket count
    @staticmethod #https://stackoverflow.com/
    def write_tickets_to_file(filename, tickets):
      with open(filename, 'w') as file:
        for ticket in tickets:
            file.write(f"{ticket.ticket_id}, {ticket.event_id}, {ticket.username}, {ticket.timestamp}, {ticket.priority}\n")

    # Constructor for the Ticket class
    def __init__(self, event_id, username, timestamp, priority=0):
        Ticket.ticket_count += 1  # Increment ticket count for each new ticket
        self.ticket_id = f'tick{Ticket.ticket_count}'  # Create a unique ID for each ticket
        self.event_id = event_id  # Event ID for the ticket
        self.username = username  # Username of the person who booked the ticket
        self.timestamp = timestamp  # Timestamp of the event
        self.priority = priority  # Priority of the ticket (default is 0)

    # Static method to read tickets from a file
    @staticmethod #https://stackoverflow.com/
    def read_tickets_from_file(filename):
        tickets_list = []  # Initialize an empty list to store tickets
        with open(filename, 'r') as file: 
            for line in file:
                # Split each line in the file into its components
                ticket_info = line.strip().split(', ')
                if len(ticket_info) == 5:  # Check if there are enough components
                    _, event_id, username, timestamp, priority = ticket_info
                    # Create a new Ticket object and add it to the list
                    ticket = Ticket(event_id, username, timestamp, int(priority))
                    tickets_list.append(ticket)
            # Return the list of tickets
            return tickets_list


class TicketingSystem:
    # Constructor for the TicketingSystem class
    def __init__(self):
        # Initialize the list of tickets by reading from a file
        self.tickets = Ticket.read_tickets_from_file("tickets.txt")

    # Method to display statistics about the tickets
    def display_statistics(self):
        if not self.tickets:  # Check if the list of tickets is empty
            print("No tickets found in the system.")
        else:
            # Count the number of tickets for each event
            event_counter = Counter(ticket.event_id for ticket in self.tickets)
            # Find the event with the most tickets
            most_common_event_id, _ = event_counter.most_common(1)[0]
            # Print the event with the most tickets
            print(f"The event ID with the highest number of tickets is {most_common_event_id}")

    # Method to book a ticket
    def book_ticket(self, username, admin=False):
        event_id = input("Enter event id: ")  # Prompt the user to enter the event ID
        event_id = "ev" + event_id #to add ev before event id as requested
        date_of_event_str = input("Enter date of event in YYYYMMDD format: ")  # Prompt the user to enter the date of the event
        try:
            #https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
            date_of_event = datetime.datetime.strptime(date_of_event_str, '%Y%m%d')  # Convert the date string to a datetime object
        except ValueError:  # Catch any ValueError exceptions
            print("Incorrect date format, should be YYYYMMDD")  # Print an error message
            return  # Exit the method
        if admin:  # If the user is an admin
            priority = int(input("Enter priority: "))  # Prompt the user to enter the priority
            if priority < 0:  # If the priority is less than 0
                print("Priority should be a positive integer")  # Print an error message
                return  # Exit the method
        else:  # If the user is not an admin
            priority = 0  # Set the priority to 0
        # Create a new Ticket object
        new_ticket = Ticket(event_id, username, date_of_event.strftime('%Y%m%d'), priority)
        # Add the new ticket to the list of tickets
        self.tickets.append(new_ticket)
        Ticket.write_tickets_to_file("tickets.txt", self.tickets)  # Write tickets to the file after a new ticket has been booked
        # Print a success message with the ID of the new ticket
        print(f"Ticket booked successfully with Ticket ID: {new_ticket.ticket_id}")

    # Method to display all valid tickets
    def display_all_tickets(self):
        today = datetime.datetime.now().strftime('%Y%m%d')  # Get today's date
        # Get a list of all tickets that are still valid
        valid_tickets = [ticket for ticket in self.tickets if ticket.timestamp >= today]
        # Sort the list of valid tickets by timestamp and event ID
        valid_tickets.sort(key=lambda x: (x.timestamp, x.event_id))
        # Loop through the sorted list of valid tickets
        for ticket in valid_tickets:
            # Print information about each ticket
            print(f"Ticket ID: {ticket.ticket_id}, Event ID: {ticket.event_id}, Username: {ticket.username}, Date: {ticket.timestamp}, Priority: {ticket.priority}")

    # Method to change the priority of a ticket
    def change_ticket_priority(self):
        ticket_id = input("Enter ticket id to change priority: ")  # Prompt the user to enter the ticket ID
        new_priority = int(input("Enter new priority: "))  # Prompt the user to enter the new priority
        if new_priority < 0:  # If the new priority is less than 0
            print("Priority should be a positive integer")  # Print an error message
            return  # Exit the method
        # Loop through the list of tickets
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:  # If the ID of the current ticket matches the entered ID
                ticket.priority = new_priority  # Change the priority of the ticket
                # Print a success message
                print(f"Priority changed successfully for Ticket ID: {ticket_id}")
                return  # Exit the method
        # If no ticket was found with the entered ID, print an error message
        print(f"Ticket ID: {ticket_id} not found")

    # Method to disable a ticket
    def disable_ticket(self):
        ticket_id = input("Enter ticket id to disable: ")  # Prompt the user to enter the ticket ID
        # Remove the ticket with the entered ID from the list of tickets
        self.tickets = [ticket for ticket in self.tickets if ticket.ticket_id != ticket_id]
        # Print a success message
        print(f"Ticket ID: {ticket_id} has been disabled")

    # Method to run events for today
    def run_events(self):
        today = datetime.datetime.now().strftime('%Y%m%d')  # Get today's date
        # Get a list of all tickets for events today
        today_tickets = [ticket for ticket in self.tickets if ticket.timestamp == today]
        # Sort the list of today's tickets by priority (highest first)
        today_tickets.sort(key=lambda x: x.priority, reverse=True)
        # Loop through the sorted list of today's tickets
        for ticket in today_tickets:
            # Print information about each ticket
            print(f"Event ID: {ticket.event_id}, Username: {ticket.username}, Priority: {ticket.priority}")
        # Remove all of today's tickets from the list of all tickets
        self.tickets = [ticket for ticket in self.tickets if ticket.timestamp != today]

    # Method to show the admin menu
    def admin_menu(self):
        # Loop forever (until the method is exited)
        while True:
            # Print the options for the admin menu
            print("1. Display Statistics")
            print("2. Book a Ticket")
            print("3. Display all Tickets")
            print("4. Change Ticket’s Priority")
            print("5. Disable Ticket")
            print("6. Run Events")
            print("7. Exit")
            # Prompt the admin to choose an option
            choice = int(input("Enter your choice: "))
            # Run the corresponding method based on the chosen option
            if choice == 1:
                self.display_statistics()
            elif choice == 2:
                self.book_ticket("admin", admin=True)
            elif choice == 3:
                self.display_all_tickets()
            elif choice == 4:
                self.change_ticket_priority()
            elif choice == 5:
                self.disable_ticket()
            elif choice == 6:
                self.run_events()
            elif choice == 7:
                return  # Exit the method
            else:
                print("Invalid Input")  # Print an error message if the input is not valid

    # Method to show the user menu
    def user_menu(self):
        # Loop forever (until the method is exited)
        while True:
            # Print the options for the user menu
            print("1. Book a ticket")
            print("2. Exit")
            # Prompt the user to choose an option
            choice = int(input("Enter your choice: "))
            username = input("Enter username: ")  # Prompt the user to enter their username
            # Run the corresponding method based on the chosen option
            if choice == 1:
                self.book_ticket(username)
            elif choice == 2:
                return  # Exit the method
            else:
                print("Invalid Input")  # Print an error message if the input is not valid

    # Method to run the ticketing system
    def run(self):
    # Infinite loop to keep the program running
      while True:
        # Prompt the user to enter their user type (admin or user)
        user_type = input("Enter 'admin' for admin access, anything else for user access: ")
        # Show the corresponding menu based on the user type
        if user_type == 'admin':
            self.admin_menu()
        else:
            self.user_menu()



# Main function to run the ticketing system
def main():
    ts = TicketingSystem()  # Create a new TicketingSystem object
    ts.run()  # Run the ticketing system

main()  # Run the main function
