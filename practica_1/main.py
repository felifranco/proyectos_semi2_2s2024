import csv
import db
import table
import datetime
from tabulate import tabulate

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
    db.ddl("DROP TABLE CSV")
    print("\n\t-> Tabla 'CSV' eliminada.")

    db.ddl("DROP TABLE fact_flight")
    print("\n\t-> Tabla 'fact_flight' eliminada.")

    db.ddl("DROP TABLE dim_passenger")
    print("\n\t-> Tabla 'dim_passenger' eliminada.")

    db.ddl("DROP TABLE dim_country")
    print("\n\t-> Tabla 'dim_country' eliminada.")

    db.ddl("DROP TABLE dim_continent")
    print("\n\t-> Tabla 'dim_continent' eliminada.")

    db.ddl("DROP TABLE dim_airport")
    print("\n\t-> Tabla 'dim_airport' eliminada.")

    db.ddl("DROP TABLE dim_time")
    print("\n\t-> Tabla 'dim_time' eliminada.")

def crearModelo():
    db.ddl(table.DIM_PASSENGER)
    print("\n\t-> Tabla 'dim_passenger' creada.")

    db.ddl(table.DIM_COUNTRY)
    print("\n\t-> Tabla 'dim_country' creada.")

    db.ddl(table.DIM_CONTINENT)
    print("\n\t-> Tabla 'dim_continent' creada.")

    db.ddl(table.DIM_AIRPORT)
    print("\n\t-> Tabla 'dim_airport' creada.")

    db.ddl(table.DIM_TIME)
    print("\n\t-> Tabla 'dim_time' creada.")

    db.ddl(table.FACT_FLIGHT)
    print("\n\t-> Tabla 'fact_flight' creada.")

def extraerInformacion():
    try:
        path = input(f"\tIngrese la ubicación del archivo CSV: ")

        file = open(path)

        #file = open("/home/feli/Documentos/USAC/SEM2_2024/Seminario2/Lab/data/Airline Dataset Updated - v2.csv")

        csvContent = csv.reader(file, delimiter=",")
        print("\n\t-> Información extraída del archivo y cargada en memoria.")

        db.ddl("CREATE TABLE CSV(Passenger_ID nvarchar(100),First_Name nvarchar(100),Last_Name nvarchar(100),Gender nvarchar(100),Age nvarchar(100),Nationality nvarchar(100),Airport_Name nvarchar(100),Airport_Country_Code nvarchar(100),Country_Name nvarchar(100),Airport_Continent nvarchar(100),Continents nvarchar(100),Departure_Date nvarchar(100),Arrival_Airport nvarchar(100),Pilot_Name nvarchar(100),Flight_Status nvarchar(100))")
        print("\t-> Tabla temporal 'CSV' creada en la base de datos.")
        
        print("\t-> Cargando de datos en lote en la tabla 'CSV'...")
        print("\t-> Hora de inicio: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        importContent = list(csvContent)
        importContent.pop(0)
        
        db.bulkInsert(
            'INSERT INTO master.dbo.CSV (Passenger_ID, First_Name, Last_Name, Gender, Age, Nationality, Airport_Name, Airport_Country_Code, Country_Name, Airport_Continent, Continents, Departure_Date, Arrival_Airport, Pilot_Name, Flight_Status) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            importContent)
        
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

    airports = db.select("SELECT DISTINCT (Arrival_Airport), Airport_Name FROM CSV")
    db.bulkInsert("""
    INSERT INTO master.dbo.dim_airport
    (airport_code, airport_name)
    VALUES(?, ?);
    """, airports)
    print("\t\t* Tabla 'dim_airport' poblada")

    dates = db.select("""
    SELECT
        t.fecha as departure_date,
        datepart(yyyy, t.fecha) year,
        datepart(mm, t.fecha) month,
        datepart(dd, t.fecha) day
    FROM 
    (
        SELECT DISTINCT CONVERT(Date, Departure_Date) fecha FROM CSV
    ) t
    """)
    db.bulkInsert("""
    INSERT INTO master.dbo.dim_time
    (departure_date, [year], [month], [day])
    VALUES(?, ?, ?, ?);
    """, dates)
    print("\t\t* Tabla 'dim_time' poblada")
    
    flights = db.select("""
    SELECT dp.id_passenger, dc2.id_country, dc.id_continent, da.id_airport, dt.id_time, c.Pilot_Name, c.Flight_Status 
    FROM CSV c
    INNER JOIN dim_continent dc ON c.Airport_Continent = dc.continent_code AND c.Continents = dc.continent_name 
    INNER Join dim_time dt ON CONVERT(Date, c.Departure_Date) = dt.departure_date 
    INNER JOIN dim_country dc2 ON c.Airport_Country_Code = dc2.country_code AND c.Country_Name = dc2.country_name 
    INNER JOIN dim_airport da ON c.Airport_Name = da.airport_name
    INNER JOIN dim_passenger dp ON c.Passenger_ID = dp.passenger_id AND c.First_Name = dp.first_name AND c.Last_Name = dp.last_name AND c.Gender = dp.gender AND CONVERT(int, c.Age) = dp.age AND C.Nationality = dp.nationality
    """)
    db.bulkInsert("""
    INSERT INTO master.dbo.fact_flight
    (id_passenger, id_country, id_continent, id_airport, id_time, pilot_name, flight_status)
    VALUES(?, ?, ?, ?, ?, ?, ?);
    """, flights)
    print("\t-> Tabla de hechos poblada")
    
def realizarConsultas():
    
    #CONSULTA 1
    query_1 = """
    SELECT 'CSV' as Tabla, COUNT('x') as Registros FROM CSV
    UNION
    SELECT 'dim_passenger' as Tabla, COUNT('x') as Registros FROM dim_passenger
    UNION
    SELECT 'dim_airport' as Tabla, COUNT('x') as Registros FROM dim_airport
    UNION
    SELECT 'dim_continent' as Tabla, COUNT('x') as Registros FROM dim_continent
    UNION
    SELECT 'dim_country' as Tabla, COUNT('x') as Registros FROM dim_country
    UNION
    SELECT 'dim_time' as Tabla, COUNT('x') as Registros FROM dim_time
    UNION
    SELECT 'fact_flight' as Tabla, COUNT('x') as Registros FROM fact_flight
    """
    result_1 = db.select(query_1)
    prettyPrint("Consulta 1", query_1, result_1, ["Tabla", "Registros"])

    #CONSULTA 2
    query_2 = """
    SELECT gender Genero, total/all_passenger Porcentaje FROM (
	SELECT 
		gender,
		COUNT(gender)*100 total,
		(SELECT COUNT(*) as total FROM dim_passenger dp) all_passenger
	FROM dim_passenger 
	GROUP BY gender
    ) as data
    """
    result_2 = db.select(query_2)
    prettyPrint("Consulta 2", query_2, result_2, ["Genero", "Porcentaje"])

    #CONSULTA 3
    query_3 = "SELECT COUNT(*) as total FROM CSV"
    result_3 = db.select(query_3)
    prettyPrint("Consulta 3", query_3, result_3, ["Total"])

    #CONSULTA 4
    query_4 = """
    SELECT dc.country_name Pais, COUNT(ff.id_country) Vuelos
    FROM fact_flight ff
    INNER JOIN dim_country dc ON ff.id_country = dc.id_country 
    GROUP BY dc.country_name
    ORDER BY dc.country_name ASC
    """
    result_4 = db.select(query_4)
    prettyPrint("Consulta 4", query_4, result_4, ["País", "Vuelos"])

    #CONSULTA 5
    query_5 = """
    SELECT TOP 5 da.airport_name Aereopuerto, COUNT(ff.id_passenger) Pasajeros
    FROM fact_flight ff 
    INNER JOIN dim_airport da ON ff.id_airport = da.id_airport 
    GROUP BY da.airport_name
    ORDER BY Pasajeros DESC
    """
    result_5 = db.select(query_5)
    prettyPrint("Consulta 5", query_5, result_5, ["Aereopuerto", "Pasajeros"])

    #CONSULTA 6
    query_6 = """
    SELECT flight_status 'Estado de vuelo', COUNT(flight_status) Total
    FROM fact_flight ff 
    GROUP BY flight_status
    ORDER BY flight_status ASC
    """
    result_6 = db.select(query_6)
    prettyPrint("Consulta 6", query_6, result_6, ["Estado de vuelo", "Total"])

    #CONSULTA 7
    query_7 = """
    SELECT TOP 5 dc.country_name Pais, COUNT(dc.country_name) Visitas
    FROM fact_flight ff 
    INNER JOIN dim_country dc ON ff.id_country = dc.id_country 
    GROUP BY dc.country_name 
    ORDER BY Visitas DESC
    """
    result_7 = db.select(query_7)
    prettyPrint("Consulta 7", query_7, result_7, ["Pais", "Visitas"])

    #CONSULTA 8
    query_8 = """
    SELECT TOP 5 dc.continent_name Continente, COUNT(dc.continent_name) Visitas
    FROM fact_flight ff 
    INNER JOIN dim_continent dc ON ff.id_continent = dc.id_continent 
    GROUP BY dc.continent_name 
    ORDER BY Visitas DESC
    """
    result_8 = db.select(query_8)
    prettyPrint("Consulta 8", query_8, result_8, ["Continente", "Visitas"])

    #CONSULTA 9
    query_9 = """
    SELECT TOP 5 dp.age Edad, dp.gender Genero, COUNT(dp.age) Visitas
    FROM fact_flight ff
    INNER JOIN dim_passenger dp ON ff.id_passenger = dp.id_passenger 
    GROUP BY dp.age, dp.gender 
    ORDER BY Visitas DESC
    """
    result_9 = db.select(query_9)
    prettyPrint("Consulta 9", query_9, result_9, ["Edad", "Genero", "Visitas"])

    #CONSULTA 10
    query_10 = """
    SELECT CONCAT(dt.month, '-', dt.year) as 'MM-YYYY', COUNT(CONCAT(dt.month, '-', dt.year)) as Vuelos
    FROM fact_flight ff 
    INNER JOIN dim_time dt ON ff.id_time = dt.id_time
    GROUP BY CONCAT(dt.month, '-', dt.year)
    ORDER BY Vuelos DESC
    """
    result_10 = db.select(query_10)
    prettyPrint("Consulta 10", query_10, result_10, ["MM-YYYY", "Vuelos"])

def prettyPrint(title, query, data, headers):
    print(f"\n\n\n──────────────────────────────────> {title} <──────────────────────────────────\n")
    print(query)
    content = tabulate(data, headers, tablefmt='psql')
    print(content)
    f = open(f"{title}.txt", "w")
    f.write(content)
    f.close()

main()