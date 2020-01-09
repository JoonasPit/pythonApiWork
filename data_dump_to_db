import mysql.connector
def insert_user(id, username, email, phone):
    conn = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database=""
    )

    query = "INSERT into usertable(id, username, email, phone) VALUES(%s, %s, %s, %s)"
    args = (id, username, email, phone)
    cursor = conn.cursor()
    cursor.execute(query,args)
    conn.commit()
    conn.close()


def main():
    insert_user(1, "username", "my@email.com", "0400040040")


if __name__ == "__main__":
    main()
