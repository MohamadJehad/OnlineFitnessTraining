from app.database import mysql,mysql_config
#search from member by id
def search_by_id(id):
        try:
            db = mysql.connector.connect(**mysql_config)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM members where member_id={id}")
            members = cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving members: {str(e)}")
        finally:
            cursor.close()
#if nothing found it will return empty []
        return members

#search from member by name
def search_by_name(name):
    try:
        db = mysql.connector.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM members where name='{name}'")
        members = cursor.fetchall()
    except Exception as e:
        print(f"Error retrieving members: {str(e)}")
#if nothing found it will return empty []
    return members

