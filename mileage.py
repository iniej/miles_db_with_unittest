import sqlite3


db_url = 'mileage.db'   # Assumes the table miles have already been created.

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles

    If the vehicle is None or new_miles is not a positive number, raise Error
    '''
    if not vehicle:
        raise Exception('Provide a vehicle name')

    if isinstance(new_miles, float) or new_miles < 0:
        raise Exception('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()


def to_upper(vehicle):

    vehicle = vehicle.upper()
    return vehicle

def search_vehicle(vehicle):

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('SELECT* FROM MILES WHERE vehicle = ?', (vehicle,))

    for row in rows_mod:
        if rows_mod.rowcount == 0:
            return None
        else:
            row in rows_mod
            return row[1]


def main():
    while True:
        vehicle = input('Enter vehicle name or q to quit ')
        if vehicle == q:
            break

        miles = int(input('Enter new miles for %s ' % vehicle)) ## TODO input validation
        vehicle = to_upper(vehicle)
        add_miles(vehicle, miles)
        search_vehicle(vehicle)

    # while True:
    #     vehicle = input('Enter vehicle name or q to quit ')
    #     if vehicle == q:
    #         break
    #     try:
    #         miles = int(input('Enter new miles for %s ' % vehicle)) ## TODO input validation
    #
    #     Exception
    #         vehicle = to_upper(vehicle)
    #         add_miles(vehicle, miles)
    #         search_vehicle(vehicle)



if __name__ == '__main__':
    main()
