# -*- coding: utf-8 -*-
import pymysql


class DbWorker:
    """
    docs here
    """
    host = ''
    user = ''
    password = ''
    db_name = ''

    def __init__(self, host=host, user=user, password=password,
                 db_name=db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def create_db(self):
        con = self.__get_con()
        cursor = con.cursor()

        cursor.execute(
            """-- auto-generated definition
CREATE TABLE IF NOT EXISTS users
(
  id          BIGINT UNSIGNED AUTO_INCREMENT
    PRIMARY KEY,
  name        VARCHAR(150)                  NULL,
  description VARCHAR(255) DEFAULT 'normal' NOT NULL,
  CONSTRAINT users_id_name_uindex
  UNIQUE (id, name)
)
  ENGINE = InnoDB;

"""
        )
        con.commit()

        cursor.execute(
            """-- auto-generated definition
CREATE TABLE IF NOT EXISTS temperatures
(
  id       BIGINT UNSIGNED AUTO_INCREMENT
    PRIMARY KEY,
  datetime DATETIME             NOT NULL,
  value    FLOAT DEFAULT '36.6' NOT NULL,
  CONSTRAINT temperatures_datetime_value_uindex
  UNIQUE (datetime, value)
)
  ENGINE = InnoDB;

"""
        )
        con.commit()

        cursor.execute(
            """-- auto-generated definition
CREATE TABLE IF NOT EXISTS user_temperatures
(
  user_id        BIGINT UNSIGNED NOT NULL,
  temperature_id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (user_id, temperature_id),
  CONSTRAINT user_temperatures_users_id_fk
  FOREIGN KEY (user_id) REFERENCES users (id),
  CONSTRAINT user_temperatures_temperatures_id_fk
  FOREIGN KEY (temperature_id) REFERENCES temperatures (id)
)
  ENGINE = InnoDB;
"""
        )
        con.commit()

        cursor.execute(
            """CREATE INDEX user_temperatures_temperatures_id_fk
  ON user_temperatures (temperature_id);
        """
        )
        con.commit()

    def __get_con(self):
        con = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

        return con

    def get_all_users(self):
        con = self.__get_con()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        cursor.close()
        con.close()

        return data

    def get_user(self, user_id):
        con = self.__get_con()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id, ))
        data = cursor.fetchone()

        cursor.close()
        con.close()

        return data

    def add_new_user(self, username, desc=None):
        con = self.__get_con()
        cursor = con.cursor()

        try:
            if desc:
                cursor.execute("INSERT INTO users (name, description) "
                               "VALUES (%s, %s)", (username, desc))
            else:
                cursor.execute("INSERT INTO users (name) "
                               "VALUES (%s)", (username, ))

            con.commit()

            cursor.execute("SELECT LAST_INSERT_ID()")
            user_id = cursor.fetchone()['LAST_INSERT_ID()']
        except pymysql.IntegrityError:
            con.rollback()
            user_id = -1
        finally:
            cursor.close()
            con.close()

        return self.get_user(user_id)
