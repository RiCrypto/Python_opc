
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Algorithms developed to provide data from Osprey B1 Temper to SCADA SQL Osprey table
# C:\Users\ralmeida\Documents\Minha Biblioteca\Scripts de programas\Python\SQLite_conn\Osprey_B1_sqlite_sql_
# This Algorithm file was create to provide solutions for programs, classes, methods and functions
# This File was design by Ph.D. Ricardo Augusto de Almeida - 2023 April 12
# Vitrum - Langley - British Columbia - Canada

###################################################################################################
# Created on Thurday July 13 09:58:00 2023
# Changed on 
# Developed by Prof. Ph.D. Ricardo Augusto de Almeida
###################################################################################################
#import counter

import sqlite3
import pyodbc
import sys
#from client_test_12 import newvalue as value01

#***********************************************************************
# 
# Query from Osprey B1 Temper SQLite to send data for
# SQL Scada Osprey table
#***********************************************************************

# Create a connection to SQLite Osprey B1 temper database
while True:

    con = sqlite3.connect("R:\LS3D_LITES_DB.sqlite3")

    cur = con.cursor()

    # The result of a "cursor.execute" can be iterated over by row
    for row in cur.execute('SELECT [procDT] ,[liteNum] ,[custID] ,[thickMM] ,[lowE] ,[centerX] ,[centerY] ,[lane] ,[area] ,[width] ,[length] ,[avgMidPV] ,[wavelength] ,[warnQA] ,[failQA] ,[alarmQA] ,[batchSNum] ,[batchY] ,[skew] ,[tempC] ,[QATestDef8] ,[QATestVal8] ,[QATestDef9] ,[QATestVal9] ,[QATestDef10] ,[QATestVal10] ,[QATestDef11] FROM liteData ORDER BY procDT DESC LIMIT 1;'):
        print(row)
        print("Time Stamp =", row[0],"\n")
        print("Glass Lite Number =", row[1],"\n")
        print("SUMP number =", row[2],"\n")
        print("Thickness in milimeters =", row[3],"\n")
        print("LowE bit true=", row[4],"\n")
        print("Center X =", row[5],"\n")
        print("Center Y =", row[6],"\n")
        print("Lite area =", row[7],"\n")
        print("Lite width =", row[8],"\n")
        print("Lite length =", row[10],"\n")
        print("Avareage Midle Point Value =", row[11],"\n")
        print("Wave length =", row[12],"\n")
        print("Warn quality =", row[13],"\n")    
        print("Fail quality bit true =", row[14],"\n")
        print("Alarm quality bit =", row[15],"\n")
        print("Batch sumatory number =", row[16],"\n")
        print("Batch Y =", row[17],"\n")
        print("Skew =", row[18],"\n")
        print("Celsius temperature =", row[19],"\n")
        print("QATestDef8 =", row[20],"\n")
        print("QATestVal8 =", row[21],"\n")
        print("QATestDef9 =", row[22],"\n")
        print("QATestVal9 =", row[23],"\n")
        print("QATestDef10 =", row[24],"\n")
        print("QATestVal10 =", row[25],"\n")
        print("QATestDef11 =", row[26],"\n")
        

    # Be sure to close the SQLite connection
    con.close()


    # Create a connection to SQL SCADA database

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.1.45.7;Database=Scada;Port=1433;UID=Scada;PWD=S$cada1')

    cursor = cnxn.cursor()


    row_0 = row[0]
    row_1 = row[1]
    row_2 = row[2]
    row_3 = row[3]
    row_4 = row[4]
    row_5 = row[5]
    row_6 = row[6]
    row_7 = row[7]
    row_8 = row[8]
    row_9 = row[9]
    row_10 = row[10]
    row_11 = row[11]
    row_12 = row[12]
    row_13 = row[13]
    row_14 = row[14]
    row_15 = row[15]
    row_16 = row[16]
    row_17 = row[17]
    row_18 = row[18]
    row_19 = row[19]
    row_20 = row[20]
    row_21 = row[21]
    row_22 = row[22]
    row_23 = row[23]
    row_24 = row[24]
    row_25 = row[25]
    row_26 = row[26]


    cursor.execute ("INSERT INTO dbo.Osprey_B1 ([procDT] ,[liteNum] ,[custID] ,[thickMM] ,[lowE] ,[centerX] ,[centerY] ,[lane] ,[area] ,[width] ,[length] ,[avgMidPV] ,[wavelength] ,[warnQA] ,[failQA] ,[alarmQA] ,[batchSNum] ,[batchY] ,[skew] ,[tempC] ,[QATestDef8] ,[QATestVal8] ,[QATestDef9] ,[QATestVal9] ,[QATestDef10] ,[QATestVal10] ,[QATestDef11]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (row_0,row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9,row_10,row_11,row_12,row_13,row_14,row_15,row_16,row_17,row_18,row_19,row_20,row_21,row_22,row_23,row_24,row_25,row_26))

    cnxn.commit()

    print('last values =',row_0,row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9,row_10,row_11,row_12,row_13,row_14,row_15,row_16,row_17,row_18,row_19,row_20,row_21,row_22,row_23,row_24,row_25,row_26,"\n")

    print('SCADA Database table Osprey B1 is updated')
    #import counter_1


    cnxn.close

   

    #option = input('Waiting status',value01 == True)
    #option = input()
    option = input('Press Enter to repeat or C to close: ')

    if option.upper().strip() == "C":
        sys.exit()
        break


