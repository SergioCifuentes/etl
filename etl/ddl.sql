CREATE TABLE IF NOT EXISTS REP_PERSONA (ID_PERSONA SERIAL PRIMARY KEY,
DPI VARCHAR(20),
PRIMER_NOMBRE VARCHAR(50) NULL,
SEGUNDO_NOMBRE VARCHAR(50) NULL,
PRIMER_APELLIDO VARCHAR(50) NULL,
SEGUNDO_APELLIDO VARCHAR(50) NULL,
APELLIDO_CASADA VARCHAR(50) NULL,
ORDEN_CEDULA VARCHAR(50) NULL,
REGISTRO_DEDULA VARCHAR(50) NULL,
DIRECCION_RESIDENCIA VARCHAR(50) NULL,
NIT VARCHAR(15) NULL,
GENERO BOOLEAN NULL,
TELEFONO VARCHAR(15) NULL,
CORREO_ELECTRONICO VARCHAR(50) NULL,
FECHA_NACIMIENTO DATE NULL) ;


    
CREATE TABLE IF NOT EXISTS REP_EMPRESA (ID_EMPRESA SERIAL PRIMARY KEY,
NOMBRE_EMPRESA VARCHAR(50),
NIT VARCHAR(15),
CODIGO VARCHAR(15),
DIRECCION VARCHAR(50),
TELEFONO VARCHAR(15)

);


CREATE TABLE IF NOT EXISTS REP_TRABAJO (ID_TRABAJO SERIAL PRIMARY KEY,
ID_PERSONA INT,
FECHA_INICIAL DATE,
FECHA_FINAL DATE,
ID_EMPRESA INT,
NOMBRE_PUESTO VARCHAR(50),
MES_PLANILLA VARCHAR(25),
SALARIO DECIMAL,
FOREIGN KEY (ID_PERSONA) REFERENCES REP_PERSONA(ID_PERSONA),
FOREIGN KEY (ID_EMPRESA) REFERENCES REP_EMPRESA(ID_EMPRESA)
);
    

