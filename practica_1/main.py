import csv
import db
import table
import datetime

csvContent = None

def main():

    exit = False

    while not exit:
        print("\n┌─────────────────────────────────────────────┐")
        print("│             --- PROCESO ETL ---             │")
        print("│ Seleccione una de las siguientes opciones:  │")
        print("│\t 1. Borrar modelo                     │")
        print("│\t 2. Crear modelo                      │")
        print("│\t 3. Extraer información               │")
        print("│\t 4. Cargar información                │")
        print("│\t 5. Realizar consultas                │")
        print("│\t                                      │")
        print("│\t 0. Salir                             │")
        print("└─────────────────────────────────────────────┘")

        option = input(f"\tOpción: ")

        if option == "1":
            borrarModelo()
        elif option == "2":
            crearModelo()
        elif option == "3":
            extraerInformacion()
        elif option == "4":
            cargarInformacion()
        elif option == "5":
            realizarConsultas()
        elif option == "0":
            print("Saliendo...")
            exit = True
        else:
            print("Opción inválida, vuelva a intentarlo. Si desea salir ingrese 'exit'")

def borrarModelo():
    #db.ddl("DROP TABLE CSV")
    print("\n\t-> Tabla 'CSV' eliminada.")

    db.ddl("DROP TABLE dim_passenger")
    print("\n\t-> Tabla 'dim_passenger' eliminada.")

    db.ddl("DROP TABLE dim_country")
    print("\n\t-> Tabla 'dim_country' eliminada.")

    db.ddl("DROP TABLE dim_continent")
    print("\n\t-> Tabla 'dim_continent' eliminada.")

    db.ddl("DROP TABLE dim_airport")
    print("\n\t-> Tabla 'dim_airport' eliminada.")

    db.ddl("DROP TABLE fact_flight")
    print("\n\t-> Tabla 'fact_flight' eliminada.")

def crearModelo():
    db.ddl(table.DIM_PASSENGER)
    print("\n\t-> Tabla 'dim_passenger' creada.")

    db.ddl(table.DIM_COUNTRY)
    print("\n\t-> Tabla 'dim_country' creada.")

    db.ddl(table.DIM_CONTINENT)
    print("\n\t-> Tabla 'dim_continent' creada.")

    db.ddl(table.DIM_AIRPORT)
    print("\n\t-> Tabla 'dim_airport' creada.")

    db.ddl(table.FACT_FLIGHT)
    print("\n\t-> Tabla 'fact_flight' creada.")

def extraerInformacion():
    try:
        #path = input(f"\tIngrese la ubicación del archivo CSV: ")

        #file = open(path)

        file = open("/home/feli/Documentos/USAC/SEM2_2024/Seminario2/Lab/data/Airline Dataset Updated - v2.csv")

        csvContent = csv.reader(file, delimiter=",")
        print("\n\t-> Información extraída del archivo y cargada en memoria.")

        db.ddl("CREATE TABLE CSV(Passenger_ID nvarchar(100),First_Name nvarchar(100),Last_Name nvarchar(100),Gender nvarchar(100),Age nvarchar(100),Nationality nvarchar(100),Airport_Name nvarchar(100),Airport_Country_Code nvarchar(100),Country_Name nvarchar(100),Airport_Continent nvarchar(100),Continents nvarchar(100),Departure_Date nvarchar(100),Arrival_Airport nvarchar(100),Pilot_Name nvarchar(100),Flight_Status nvarchar(100))")
        print("\t-> Tabla temporal 'CSV' creada en la base de datos.")
        
        print("\t-> Cargando de datos en lote en la tabla 'CSV'...")
        print("\t-> Hora de inicio: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #TODO: Quitar la fila 0
        db.bulkInsert(
            'INSERT INTO master.dbo.CSV (Passenger_ID, First_Name, Last_Name, Gender, Age, Nationality, Airport_Name, Airport_Country_Code, Country_Name, Airport_Continent, Continents, Departure_Date, Arrival_Airport, Pilot_Name, Flight_Status) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            csvContent)
        print("\t-> Hora final: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("\t-> Proceso finalizado, información disponible en la base de datos.")
    except Exception as error:
        print("extraerInformacion: ", error)

def cargarInformacion():
    print("\n\t-> Poblar dimensiones:")

    passengers = db.select("SELECT DISTINCT(Passenger_ID), First_Name, Last_Name, Gender, CONVERT(int, Age), Nationality FROM CSV")
    db.bulkInsert("""
    INSERT INTO master.dbo.dim_passenger
    (passenger_id, first_name, last_name, gender, age, nationality)
    VALUES(?, ?, ?, ?, ?, ?);
    """, passengers)
    print("\t\t* Tabla 'dim_passenger' poblada")

    countries = db.select("SELECT DISTINCT(Airport_Country_Code), Country_Name FROM CSV")
    db.bulkInsert("""
    INSERT INTO master.dbo.dim_country
    (country_code, country_name)
    VALUES(?, ?);
    """, countries)
    print("\t\t* Tabla 'dim_country' poblada")

    continents = db.select("SELECT DISTINCT (Airport_Continent), Continents FROM CSV")
    db.bulkInsert("""
    INSERT INTO master.dbo.dim_continent
    (continent_code, continent_name)
    VALUES(?, ?);
    """, continents)
    print("\t\t* Tabla 'dim_continent' poblada")

    airports = db.select("SELECT DISTINCT (CASE WHEN Arrival_Airport = '0' THEN Airport_Name ELSE Arrival_Airport END), Airport_Name FROM CSV")
    db.bulkInsert("""
    INSERT INTO master.dbo.dim_airport
    (airport_code, airport_name)
    VALUES(?, ?);
    """, airports)
    print("\t\t* Tabla 'dim_airport' poblada")
    
    flights = db.select("SELECT Passenger_ID, Airport_Country_Code, Airport_Continent, CASE WHEN Arrival_Airport = '0' THEN Airport_Name ELSE Arrival_Airport END, Pilot_Name, Flight_Status FROM CSV")
    db.bulkInsert("""
    INSERT INTO master.dbo.fact_flight
    (passenger_id, country_code, continent_code, airport_code, pilot_name, flight_status)
    VALUES(?, ?, ?, ?, ?, ?);
    """, flights)
    print("\t-> Tabla de hechos poblada")
    '''
    if csvContent != None:
        #print("\t-> Cargando en lote...")
        #print("\t-> Hora de inicio: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #db.bulkInsert(
        #    'INSERT INTO master.dbo.CSV (Passenger_ID, First_Name, Last_Name, Gender, Age, Nationality, Airport_Name, Airport_Country_Code, Country_Name, Airport_Continent, Continents, Departure_Date, Arrival_Airport, Pilot_Name, Flight_Status) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        #    csvContent)
        #print("\t-> Hora final: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

       
        #index = 0
        #for row in csvContent:
        #    if index > 0:
        #        splitInformation(row, index)
        #        #break
        #    if index == 10000:
        #        break
        #    index += 1
    else:
        print("\t-> Antes de continuar debe extraer la información.")
    '''
    
def realizarConsultas():
    
    #CONSULTA 1
    print("\n\t-> Consulta 1")
    query_1 = "SELECT COUNT(*) as total FROM CSV"
    result_1 = db.select(query_1)
    print(f"\n\t\t{query_1}: ", result_1[0][0])

    #CONSULTA 2
    print("\n\t-> Consulta 2")
    query_2 = "SELECT COUNT(*) as total FROM CSV"
    result_2 = db.select(query_2)
    print(f"\n\t\t{query_2}: ", result_2[0][0])

    #CONSULTA 3
    print("\n\t-> Consulta 3")
    query_3 = "SELECT COUNT(*) as total FROM CSV"
    result_3 = db.select(query_3)
    print(f"\n\t\t{query_3}: ", result_3[0][0])

    #CONSULTA 4
    print("\n\t-> Consulta 4")
    query_4 = "SELECT COUNT(*) as total FROM CSV"
    result_4 = db.select(query_4)
    print(f"\n\t\t{query_4}: ", result_4[0][0])

    #CONSULTA 5
    print("\n\t-> Consulta 5")
    query_5 = "SELECT COUNT(*) as total FROM CSV"
    result_5 = db.select(query_5)
    print(f"\n\t\t{query_5}: ", result_5[0][0])

    #CONSULTA 6
    print("\n\t-> Consulta 6")
    query_6 = "SELECT COUNT(*) as total FROM CSV"
    result_6 = db.select(query_6)
    print(f"\n\t\t{query_6}: ", result_6[0][0])

    #CONSULTA 7
    print("\n\t-> Consulta 7")
    query_7 = "SELECT COUNT(*) as total FROM CSV"
    result_7 = db.select(query_7)
    print(f"\n\t\t{query_7}: ", result_7[0][0])

    #CONSULTA 8
    print("\n\t-> Consulta 8")
    query_8 = "SELECT COUNT(*) as total FROM CSV"
    result_8 = db.select(query_8)
    print(f"\n\t\t{query_8}: ", result_8[0][0])

    #CONSULTA 9
    print("\n\t-> Consulta 9")
    query_9 = "SELECT COUNT(*) as total FROM CSV"
    result_9 = db.select(query_9)
    print(f"\n\t\t{query_9}: ", result_9[0][0])

    #CONSULTA 10
    print("\n\t-> Consulta 10")
    query_10 = "SELECT COUNT(*) as total FROM CSV"
    result_10 = db.select(query_10)
    print(f"\n\t\t{query_10}: ", result_10[0][0])

main()