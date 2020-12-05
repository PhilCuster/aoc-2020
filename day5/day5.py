with open('day5/input.txt') as file:
    passes = file.readlines()

highest = 0
lowest = 1024
seat_ids = []

for p in passes:
    row_id = p[0:7]
    column_id = p[7:10]
    # First determine row
    row_id = row_id.replace("F", "0")
    row_id = row_id.replace("B", "1")
    row_num = int(row_id, 2)
    # Next determine column
    column_id = column_id.replace("L", "0")
    column_id = column_id.replace("R", "1")
    column_num = int(column_id, 2)
    # Determine seat id
    seat_id = (row_num * 8) + column_num
    seat_ids.append(seat_id)

seat_ids.sort()

print("Highest ID: ", seat_ids[len(seat_ids) - 1])
print("Lowest ID: ", seat_ids[0])

i = seat_ids[0]
for id in seat_ids:
    if i != id:
        print("Your seat ID: ", i)
        break
    i += 1


