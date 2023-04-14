# -*- coding: utf-8 -*-

import sqlite3
import os

class ChatGee_DB:

    def __init__(self):
        self.db_prefix = "ChatGee"
        self.user_db_name = "_User.db"
        self.chat_db_name = "_Chat.db"
        self.token_db_name = "_Tokens.db"
    
    def init_db(self, db_prefix):
        self.db_prefix = db_prefix
        self.user_db_name = db_prefix + "_User.db"
        self.chat_db_name = db_prefix + "_Chat.db"
        self.token_db_name = db_prefix + "_Tokens.db"

        # User databasse
        if os.path.isfile(self.user_db_name):
            print("ChatGee DB : User Database exists!")
        else:
            # create a connection to the database
            conn_init = sqlite3.connect(self.user_db_name)

            # create a new table to store conversation data
            cursor_init = conn_init.cursor()
            cursor_init.execute("CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, room TEXT NOT NULL, member BOOL NOT NULL, count INTEGER NOT NULL, total_count INTEGER NOT NULL)")
            conn_init.commit()

            # close the database connection when finished
            cursor_init.close()
            conn_init.close()

        # Prompt database
        if os.path.isfile(self.chat_db_name):
            print("ChatGee DB : Chat History Database exists!")
        else:
            # create a connection to the database
            conn_init = sqlite3.connect(self.chat_db_name)

            # create a new table to store conversation data
            cursor_init = conn_init.cursor()
            cursor_init.execute("CREATE TABLE conversation (id INTEGER PRIMARY KEY AUTOINCREMENT, speaker TEXT NOT NULL, room TEXT NOT NULL, message TEXT NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
            conn_init.commit()

            # close the database connection when finished
            cursor_init.close()
            conn_init.close()

        if os.path.isfile(self.token_db_name):
            print("ChatGee DB : Token Usage Database exists!")
        else:
            # create a connection to the database
            conn_init = sqlite3.connect(self.token_db_name)
            # create a new table to store conversation data
            cursor_init = conn_init.cursor()
            cursor_init.execute("CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, prompt_tokens INTEGER NULL, response_tokens INTEGER NULL, total_tokens INTEGER NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
            conn_init.commit()
            # close the database connection when finished
            cursor_init.close()
            conn_init.close()

    # Define a function to save conversation data
    def save_conversation_data(self, speaker, room, message):
        conn = sqlite3.connect(self.chat_db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO conversation (speaker, room, message) VALUES (?, ?, ?)", (speaker, room, message))
        cursor.execute("DELETE FROM conversation WHERE id NOT IN (SELECT id FROM conversation ORDER BY id DESC LIMIT 20)")
        conn.commit()
        cursor.close()
        conn.close()

    def en_save_conversation_data(self, speaker, room, message):
        conn = sqlite3.connect(self.chat_en_db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO conversation (speaker, room, message) VALUES (?, ?, ?)", (speaker, room, message))
        cursor.execute("DELETE FROM conversation WHERE id NOT IN (SELECT id FROM conversation ORDER BY id DESC LIMIT 20)")
        conn.commit()
        cursor.close()
        conn.close()

    # Define a function to save conversation data not at the end but somewhere in the middle
    def save_conversation_one_above(self, speaker, room, message):
        conn = sqlite3.connect(self.chat_db_name)
        cursor = conn.cursor()

        # Get the id of the last row
        cursor.execute("SELECT id FROM conversation ORDER BY id DESC LIMIT 1")
        last_id = cursor.fetchone()

        new_id = last_id[0] + 2 if last_id else 1
        
        # Shift the ids of all rows with an id >= new_id
        cursor.execute("UPDATE conversation SET id = id + 2 WHERE id >= ?", (new_id,))

        # Insert the new row with the desired id
        cursor.execute("INSERT INTO conversation (id, speaker, room, message) VALUES (?, ?, ?, ?)", (new_id, speaker, room, message))

        conn.commit()
        cursor.close()
        conn.close()

    def en_save_conversation_one_above(self, speaker, room, message):
        conn = sqlite3.connect(self.chat_en_db_name)
        cursor = conn.cursor()

        # Get the id of the last row
        cursor.execute("SELECT id FROM conversation ORDER BY id DESC LIMIT 1")
        last_id = cursor.fetchone()

        new_id = last_id[0] + 2 if last_id else 1
        
        # Shift the ids of all rows with an id >= new_id
        cursor.execute("UPDATE conversation SET id = id + 2 WHERE id >= ?", (new_id,))

        # Insert the new row with the desired id
        cursor.execute("INSERT INTO conversation (id, speaker, room, message) VALUES (?, ?, ?, ?)", (new_id, speaker, room, message))

        conn.commit()
        cursor.close()
        conn.close()


    def delete_conversation_data(self, room):
        conn = sqlite3.connect(self.chat_db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM conversation WHERE room=?", (room,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_conversation_data(self, room, limit=100):
        conn = sqlite3.connect(self.chat_db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM conversation WHERE room=? ORDER BY id ASC LIMIT ?", (room, limit))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_conversation_latest(self, room, limit=1):
        conn = sqlite3.connect(self.chat_db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM conversation WHERE room=? ORDER BY id DESC LIMIT ?", (room, limit))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    # Define a function to save user data
    def save_user_data(self, room, member, count, total_count):
        conn = sqlite3.connect(self.user_db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM data WHERE room=?", (room,))
        count_row = cursor.fetchone()
        if count_row[0] == 0:
            cursor.execute("INSERT INTO data (room, member, count, total_count) VALUES (?, ?, ?, ?)", (room, member, count, total_count))
        else:
            cursor.execute("UPDATE data SET member=?, count=?, total_count=?  WHERE room=?", (member, count, total_count, room))
        conn.commit()
        cursor.close()
        conn.close()

    # Define a function to retrieve user data
    def get_user_data_by_room(self, room):
        conn = sqlite3.connect(self.user_db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data WHERE room=?", (room,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def save_token_usage(self, prompt_tokens, response_tokens):
        conn = sqlite3.connect(self.token_db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data (prompt_tokens, response_tokens, total_tokens) VALUES (?, ?, ?)", (prompt_tokens, response_tokens, prompt_tokens + response_tokens))
        cursor.close()
        conn.commit()
        conn.close()