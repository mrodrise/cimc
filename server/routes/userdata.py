import requests
import json
import mysql.connector
from configbbdd import config

class userData(object):

    def __init__(self, username):
        self.username = username

    def insert_userdata(self, address, city, postal_code, data_list, home_risk):
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()

            cursor.callproc('sp_create_user_data', (self.username, address, city, postal_code,
                data_list[0], data_list[1], data_list[2], data_list[3], data_list[4],
                data_list[5], data_list[6], data_list[7], data_list[8], data_list[9],
                data_list[10], data_list[11], data_list[12], data_list[13], data_list[14], home_risk)
            )

            for result in cursor.stored_results():
                data = result.fetchall()

            if len(data[0][0]) is 0:
                con.commit()
                return True
            else:
                return False

        except Exception as e:
            return None

        finally:
            cursor.close()
            con.close()


    def update_userdata(self, address, city, postal_code, data_list, home_risk):
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            print("Voy a hacer la llamada para updatear")

            cursor.callproc('sp_update_user_data', (self.username, address, city, postal_code,
                data_list[0], data_list[1], data_list[2], data_list[3], data_list[4],
                data_list[5], data_list[6], data_list[7], data_list[8], data_list[9],
                data_list[10], data_list[11], data_list[12], data_list[13], data_list[14], home_risk)
            )

            for result in cursor.stored_results():
                data = result.fetchall()

            if len(data[0][0]) is 0:
                con.commit()
                print("Se ha updateado")
                return True
            else:
                return False

        except Exception as e:
            return None

        finally:
            cursor.close()
            con.close()

    def get_userdata(self):
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()

            cursor.callproc('sp_select_user_data', (self.username,))

            for result in cursor.stored_results():
                data = result.fetchall()

            if len(data) > 0:
                print("El usuario existe")
                return(data[0])
            else:
                print("El usuario no existe")
                return None

        except Exception as e:
            print("Estoy en la excepcion dentro de user_data")
            print(self.username)
            return None

        finally:
            cursor.close()
            con.close()
