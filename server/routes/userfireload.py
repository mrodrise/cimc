import requests
import json
import mysql.connector
from configbbdd import config

class userFireLoad(object):

    def __init__(self, username):
        self.username = username

    def insert_userfireload(self, data_list):
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()

            print("insert_userfireload - Voy a hacer la llamada para insertar")
            cursor.callproc('sp_create_user_fire_load', (self.username, data_list[0], data_list[1],
                    data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7], data_list[8],))

            for result in cursor.stored_results():
                data = result.fetchall()

            if len(data[0][0]) is 0:
                print("insert_userfireload - Voy a hacer el commit")
                con.commit()
                return True
            else:
                return False

        except Exception as e:
            print("insert_userfireload - Estoy en la excepcion")
            return None

        finally:
            cursor.close()
            con.close()


    def update_userfireload(self, data_list):
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            print("update_userfireload - Voy a hacer la llamada para updatear")

            cursor.callproc('sp_update_user_fire_load', (self.username, data_list[0], data_list[1], data_list[2],
                    data_list[3], data_list[4], data_list[5], data_list[6], data_list[7], data_list[8],)
            )

            for result in cursor.stored_results():
                data = result.fetchall()

            if len(data[0][0]) is 0:
                con.commit()
                print("update_userfireload - Se ha updateado")
                return True
            else:
                return False

        except Exception as e:
            return None

        finally:
            cursor.close()
            con.close()

    def get_userfireload(self):
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()

            cursor.callproc('sp_select_user_fire_load', (self.username,))

            for result in cursor.stored_results():
                data = result.fetchall()

            if len(data) > 0:
                print("get_userfireload - El usuario existe")
                return(data[0])
            else:
                print("get_userfireload - El usuario no existe")
                return None

        except Exception as e:
            print(self.username)
            return None

        finally:
            cursor.close()
            con.close()
