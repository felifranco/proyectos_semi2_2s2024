DIM_PASSENGER = """
    CREATE TABLE dim_passenger(
        passenger_id nvarchar(20),
        first_name nvarchar(50),
        last_name nvarchar(50),
        gender nvarchar(50),
        age int,
        nationality nvarchar(100)
    )
"""

DIM_COUNTRY = """
CREATE TABLE dim_country(
    country_code nvarchar(10),
    country_name nvarchar(100)
)
"""

DIM_CONTINENT = """
CREATE TABLE dim_continent(
    continent_code nvarchar(10),
    continent_name nvarchar(100)
)
"""

DIM_AIRPORT = """
CREATE TABLE dim_airport(
    airport_code nvarchar(100),
    airport_name nvarchar(100)
)
"""

FACT_FLIGHT = """
CREATE TABLE fact_flight(
    passenger_id nvarchar(20),
    country_code nvarchar(10),
    continent_code nvarchar(10),
    airport_code nvarchar(100),
    pilot_name nvarchar(150),
    flight_status nvarchar(100)
)
"""