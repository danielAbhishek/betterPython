import string
import random
from typing import List


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:

    def __init__(self, processing_strategy='fifo'):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        if len(self.tickets) == 0:
            print("There are no tickets to be processed")
            return

        if self.processing_strategy == 'fifo':
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif self.processing_strategy == 'filo':
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif self.processing_strategy == 'random':
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("=============================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("=============================")


app = CustomerSupport('filo')

app.create_ticket("John Smith", "My Computer makes strange sounds!")
app.create_ticket("Linus Sebastican",
                  "I can't upload any videos, please help!")
app.create_ticket("Arjan Eggs", "VSCode does not work")

app.process_tickets()
