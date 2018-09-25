import requests
import json
import mysql.connector
from configbbdd import config
import sys

def get_alluserdata():
    try:
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        cursor.callproc('sp_select_all_user_data')
        for result in cursor.stored_results():
            data = result.fetchall()
        if len(data) > 0:
            print("get_alluserdata - Hay informacion")
            for i in data:
                print(i)
            return(data)
        else:
            print("get_alluserdata - No hay informacion")
            return None
    except Exception as e:
        print("get_alluserdata - Excepcion")
        return None

    finally:
        cursor.close()
        con.close()

def get_alluserfireload():
    try:
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        cursor.callproc('sp_select__all_user_fire_load')
        for result in cursor.stored_results():
            data = result.fetchall()
        if len(data) > 0:
            print("get_alluserfireload - Hay informacion")
            for i in data:
                print(i)
            return(data)
        else:
            print("get_alluserfireload - No hay informacion")
            return None
    except Exception as e:
        print("get_alluserfireload - Excepcion")
        return None

    finally:
        cursor.close()
        con.close()

def get_housesecure():
    houses_firerisk = get_alluserdata()
    houses_fireload = get_alluserfireload()

    # Select the three houses with less fire risk
    houses_less_firerisk = []

    print("get_housesecure - ordenando las casas")
    print(sorted(houses_firerisk, key=lambda house: house[19]))
    print(houses_firerisk)

    houses_firerisk = sorted(houses_firerisk, key=lambda house: house[19])

    house_secure = []
    num_houses = 0
    min_fireload = sys.float_info
    for i in houses_firerisk:
        if num_houses < 3:
            num_houses += 1
            for j in houses_fireload:
                if (i[0]==j[0] and float(j[9]) < min_fireload):
                    print (i)
                    print (j)
                    min_fireload = float(j[9])
                    house_secure = i
        else:
            break

    print ("get_house_secure - the house more secure")
    print(house_secure)
    return house_secure
