all_cars = ['bmw', 'seat', 'nissan', 'skoda', 'honda', 'lada', 'jeep', 'reno', 'audi', 'vw', 'chevrolet']
german_cars = ['bmw', 'vw', 'audi']

# Loop with conditional commands
# printed for us only the cars that are on the german_cars list
for x in all_cars:
    if x in german_cars:
        print(x + ': is German Car')
