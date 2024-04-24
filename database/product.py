from pypika import PostgreSQLQuery, Table

def get_left_join(conn):
    product = Table('Product')
    transaction = Table('Transaction')
    query = PostgreSQLQuery.from_(product).select('*').left_join(transaction).on(product.ProductID == transaction.ProductID)
    query = query.get_sql()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_right_join(conn):
    product = Table('Product')
    transaction = Table('Transaction')
    query = PostgreSQLQuery.from_(product).select('*').right_join(transaction).on(product.ProductID == transaction.ProductID)
    query = query.get_sql()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result