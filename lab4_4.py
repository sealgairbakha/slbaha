import json

with open('c:/Users/Nursat/Desktop/Study/PP2/Lab 4/sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<7} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs["dn"]
    descr = attrs["descr"]
    speed = attrs["speed"]
    mtu = attrs["mtu"]
    print("{:<50} {:<20} {:<7} {:<6}".format(dn, descr, speed, mtu))