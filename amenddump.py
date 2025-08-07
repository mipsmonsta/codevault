# Scripts for use if dumpdata from Cockroach inserted spacing for every even index
withoutspace = None
with open('datadump.json', 'r') as file:
    data = file.read()
    withoutspace = [ data[i] for i in range(len(data)) if i % 2 == 0 ]
    withoutspace ="".join(withoutspace)

with open('datadump_withoutspace.json', 'w') as file:
    file.write(withoutspace)


