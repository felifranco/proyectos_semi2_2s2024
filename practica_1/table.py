DIM_PASSENGER = """
CREATE TABLE dim_passenger(
    id_passenger int IDENTITY(1,1) PRIMARY KEY,
    passenger_id varchar(20) NOT NULL,
    first_name varchar(50),
    last_name varchar(50),
    gender varchar(50),
    age int,
    nationality varchar(100)
)
"""

DIM_COUNTRY = """
CREATE TABLE dim_country(
    id_country int IDENTITY(1,1) PRIMARY KEY,
    country_code varchar(10),
    country_name varchar(100)
)
"""

DIM_CONTINENT = """
CREATE TABLE dim_continent(
    id_continent int IDENTITY(1,1) PRIMARY KEY,
    continent_code varchar(10) NOT NULL,
    continent_name varchar(100)
)
"""

DIM_AIRPORT = """
CREATE TABLE dim_airport(
    id_airport int IDENTITY(1,1) PRIMARY KEY,
    airport_code varchar(100) NOT NULL,
    airport_name varchar(100)
)
"""

DIM_TIME = """
CREATE TABLE dim_time(
    id_time int IDENTITY(1,1) PRIMARY KEY,
    departure_date date,
    year int,
    month int,
    day int,
)
"""

FACT_FLIGHT = """
CREATE TABLE fact_flight(
    id_passenger int NOT NULL,
    id_country int NOT NULL,
    id_continent int NOT NULL,
    id_airport int NOT NULL,
    id_time int NOT NULL,
    pilot_name varchar(150),
    flight_status varchar(100),
    CONSTRAINT fact_dim_passenger_FK FOREIGN KEY (id_passenger) REFERENCES dim_passenger(id_passenger),
    CONSTRAINT fact_dim_dim_country_FK FOREIGN KEY (id_country) REFERENCES dim_country(id_country),
    CONSTRAINT fact_dim_continent_FK FOREIGN KEY (id_continent) REFERENCES dim_continent(id_continent),
    CONSTRAINT fact_dim_airport_FK FOREIGN KEY (id_airport) REFERENCES dim_airport(id_airport),
    CONSTRAINT fact_dim_time_FK FOREIGN KEY (id_time) REFERENCES dim_time(id_time)
)
"""