USE [sgfood01]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[compra](
	[Fecha] [nvarchar](100) NULL,
	[CodProveedor] [nvarchar](100) NULL,
	[NombreProveedor] [nvarchar](100) NULL,
	[DireccionProveedor] [nvarchar](200) NULL,
	[NumeroProveedor] [nvarchar](100) NULL,
	[WebProveedor] [nvarchar](100) NULL,
	[CodProducto] [nvarchar](100) NULL,
	[NombreProducto] [nvarchar](100) NULL,
	[MarcaProducto] [nvarchar](100) NULL,
	[Categoria] [nvarchar](100) NULL,
	[SodSuSursal] [nvarchar](100) NULL,
	[NombreSucursal] [nvarchar](100) NULL,
	[DireccionSucursal] [nvarchar](200) NULL,
	[Region] [nvarchar](100) NULL,
	[Departamento] [nvarchar](100) NULL,
	[Unidades] [nvarchar](100) NULL,
	[CostoU] [nvarchar](100) NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[venta](
	[Fecha] [nvarchar](100) NULL,
	[CodigoCliente] [nvarchar](100) NULL,
	[NombreCliente] [nvarchar](100) NULL,
	[TipoCliente] [nvarchar](100) NULL,
	[DireccionCliente] [nvarchar](200) NULL,
	[NumeroCliente] [nvarchar](100) NULL,
	[CodVendedor] [nvarchar](100) NULL,
	[NombreVendedor] [nvarchar](100) NULL,
	[Vacacionista] [nvarchar](100) NULL,
	[CodProducto] [nvarchar](100) NULL,
	[NombreProducto] [nvarchar](100) NULL,
	[MarcaProducto] [nvarchar](100) NULL,
	[Categoria] [nvarchar](100) NULL,
	[SodSuSursal] [nvarchar](100) NULL,
	[NombreSucursal] [nvarchar](100) NULL,
	[DireccionSucursal] [nvarchar](200) NULL,
	[Region] [nvarchar](100) NULL,
	[Departamento] [nvarchar](100) NULL,
	[Unidades] [nvarchar](100) NULL,
	[PrecioUnitario] [nvarchar](100) NULL
) ON [PRIMARY]
GO

