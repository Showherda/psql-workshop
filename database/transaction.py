from pypika import PostgreSQLQuery, Table

def get_full_join(conn):
    product = Table('Product')
    transaction = Table('Transaction')
    query = PostgreSQLQuery.from_(product).select('*').outer_join(transaction).on(product.ProductID == transaction.ProductID)
    query = query.get_sql()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_inner_join(conn):
    product = Table('Product')
    transaction = Table('Transaction')
    query = PostgreSQLQuery.from_(product).select('*').join(transaction).on(product.ProductID == transaction.ProductID)
    query = query.get_sql()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    # print(query)
    return result