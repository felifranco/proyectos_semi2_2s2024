CREATE TABLE sgfood02.compra (
	Fecha varchar(100) NULL,
	CodProveedor varchar(100) NULL,
	NombreProveedor varchar(100) NULL,
	DireccionProveedor varchar(200) NULL,
	NumeroProveedor varchar(100) NULL,
	WebProveedor varchar(100) NULL,
	CodProducto varchar(100) NULL,
	NombreProducto varchar(100) NULL,
	MarcaProducto varchar(100) NULL,
	Categoria varchar(100) NULL,
	SodSuSursal varchar(100) NULL,
	NombreSucursal varchar(100) NULL,
	DireccionSucursal varchar(200) NULL,
	Region varchar(100) NULL,
	Departamento varchar(100) NULL,
	Unidades varchar(100) NULL,
	CostoU varchar(100) NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;


CREATE TABLE sgfood02.venta (
	Fecha varchar(100) NULL,
	CodigoCliente varchar(100) NULL,
	NombreCliente varchar(100) NULL,
	TipoCliente varchar(100) NULL,
	DireccionCliente varchar(200) NULL,
	NumeroCliente varchar(100) NULL,
	CodVendedor varchar(100) NULL,
	NombreVendedor varchar(100) NULL,
	Vacacionista varchar(100) NULL,
	CodProducto varchar(100) NULL,
	NombreProducto varchar(100) NULL,
	MarcaProducto varchar(100) NULL,
	Categoria varchar(100) NULL,
	SodSuSursal varchar(100) NULL,
	NombreSucursal varchar(100) NULL,
	DireccionSucursal varchar(200) NULL,
	Region varchar(100) NULL,
	Departamento varchar(100) NULL,
	Unidades varchar(100) NULL,
	PrecioUnitario varchar(100) NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;
