from pypika import PostgreSQLQuery, Table

def get_all_customers(conn):
    customer = Table('Customer')
    query = PostgreSQLQuery.from_(customer).select('*')
    query = query.get_sql()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result