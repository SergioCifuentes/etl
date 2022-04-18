commands = (
        """
        CREATE TABLE REP_PERSONA (ID_PERSONA INT PRIMARY KEY,
DPI VARCHAR(20),
PRIMER_NOMBRE VARCHAR(50),
SEGUNDO_NOMBRE VARCHAR(50),
PRIMER_APELLIDO VARCHAR(50),
SEGUNDO_APELLIDO VARCHAR(50),
APELLIDO_CASADA VARCHAR(50),
ORDEN_CEDULA VARCHAR(50),
REGISTRO_DEDULA VARCHAR(50),
DIRECCION_RESIDENCIA VARCHAR(50),
NIT VARCHAR(15),
GENERO BOOLEAN,
TELEFONO VARCHAR(15),
CORREO_ELECTRONICO VARCHAR(50),
FECHA_NACIMIENTO DATE);
        """,
        """ CREATE TABLE REP_EMPRESA (ID_EMPRESA INT PRIMARY KEY,
NOMBRE_EMPRESA VARCHAR(50),
NIT VARCHAR(15),
CODIGO VARCHAR(15),
DIRECCION VARCHAR(50),
TELEFONO VARCHAR(15)

);
        """,
        """
        CREATE TABLE REP_TRABAJO (ID_TRABAJO INT PRIMARY KEY,
ID_PERSONA INT,
FECHA_INICIAL DATE,
FECHA_FINAL DATE,
ID_EMPRESA INT,
NOMBRE_PUESTO VARCHAR(50),
MES_PLANILLA VARCHAR(10),
SALARIO DECIMAL,
FOREIGN KEY (ID_PERSONA) REFERENCES REP_PERSONA(ID_PERSONA),
FOREIGN KEY (ID_EMPRESA) REFERENCES REP_EMPRESA(ID_EMPRESA)
);
        """)