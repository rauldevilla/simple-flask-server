import json
import random

clients = []
for i in range(1000):
    client = {
        'id': i + 1,
        'name': f'Client{i+1}',
        'age': random.randint(18, 65),
        'email': f'client{i+1}@example.com',
        'address': f'123 Main St, City{i+1}, State{i+1}',
        'phone': f'555-1234-{i:04}',
        'account_balance': round(random.uniform(1000, 100000), 2)
    }
    clients.append(client)

with open('data.json', 'w') as f:
    json.dump(clients, f, indent=4)
