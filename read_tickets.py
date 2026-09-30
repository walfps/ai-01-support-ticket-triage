import csv

ALLOWED = ["billing", "technical", "delivery", "other"]

def count_categories(filename):
    with open(filename, "r", newline='') as file:
        reader = csv.reader(file)

        header = next(reader)

        counts = {}
        unknown = []

        for row in reader:
            key = row[2]
            if key not in ALLOWED: 
                unknown.append((row[0], key))
            counts[key] = counts.get(key, 0) + 1

    return counts, unknown

def show_output(counts, unknown):
    for ticket in unknown:
        print(f'WARNING: ticket {ticket[0]} has unknown category "{ticket[1]}"')
    for category in counts:
        print(f'{category}: {counts[category]}')
    print(f'Total number of tickets = {sum(counts.values())}')
    print("*****************************************")


counts1, unknown1 = count_categories("tickets.csv")
show_output(counts1, unknown1)

counts2, unknown2 = count_categories("tickets_small.csv")
show_output(counts2, unknown2)

    

