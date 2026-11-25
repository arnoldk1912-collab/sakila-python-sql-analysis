import mysql.connector
from secrets_config import DB_PASSWORD

def get_high_rental_film():
    # # 1. Connect to your local MySQL Sakila database
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = DB_PASSWORD,
        database = 'sakila'
    )  
    
    cursor = db.cursor()
    
    # 2. Write and run your SQL query
    query = '''
    SELECT title, length, rental_rate
    FROM film
    WHERE rental_rate > 3
    LIMIT 5;
    '''
    
    cursor.execute(query)
    
    # 3. Grab all rows and return them
    results = cursor.fetchall()
    
    # 4. Clean up connections
    cursor.close()
    db.close()
    
    return results

# Call your function and loop through the results
customers = get_high_rental_film()
for title, length, rate in customers:
    print(f'Film: {title} | Length: {length} mins | Rate: ${rate}')