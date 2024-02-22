import psycopg2
def get_notes_from_db()->list:
    result = []
    return result

def createdb()-> None:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='test'
    )
    with conn.cursor() as cursor:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
	number serial PRIMARY KEY,
	content varchar(1000) NOT NULL) 
        """)
    conn.close()


if __name__=='__main__':
    createdb()