def log_new_tickets(tickets, new_tickets):
    for t in new_tickets:
        tickets.append(t)
def resolve_tickets(tickets, num_to_resolve):
    resolved = []
    for i in range(min(num_to_resolve, len(tickets))):
        resolved.append(tickets.pop(0))
    return resolved
def close_ticket(tickets, ticket_id):
    if ticket_id in tickets:
        tickets.remove(ticket_id)
        return True
    else:
        return False
def manage_tickets(initial_tickets, new_tickets_to_log, tickets_to_resolve, ticket_to_close):

    tickets = initial_tickets[:]  
    
    log_new_tickets(tickets, new_tickets_to_log)
    close_ticket(tickets, ticket_to_close)
    resolved = resolve_tickets(tickets, tickets_to_resolve)

    return tickets, resolved

print(f"=== IT Help desk ticket System ====")
initial_input = input("Enter initial ticket IDs separafed by space: ")
initial = [int(x) for x in initial_input.split()]
new_input = input("Enter new ticket IDs separateed by space: ")
new_tickets = [int(x) for x in new_input.split()]
resolve_count = int(input("Enter number of tickets to resolve: "))
close_id = int(input("Enter ticket ID to close:"))

final_state, resolved = manage_tickets(initial, new_tickets, resolve_count, close_id)

print(f"\n===== Results =======")
print("final_state:", final_state)
print("resolved:", resolved)
print("OriGinal list (unchanged):", initial)
