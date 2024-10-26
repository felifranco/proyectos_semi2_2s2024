--USE master;
-- CREATE DATABASE data_warehouse;

USE [data_warehouse];

/****** ----- DIMENSION TIEMPO ----- ******/

CREATE TABLE [dbo].[dim_tiempo](
	[id_tiempo] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[fecha] [date] NOT NULL,
	[ano] [smallint] NOT NULL,
	[semestre] [smallint] NOT NULL,
	[mes] [smallint] NOT NULL,
	[dia] [smallint] NOT NULL
 CONSTRAINT [PK_dim_tiempo] PRIMARY KEY CLUSTERED 
(
	[id_tiempo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION PROVEEDOR ----- ******/

CREATE TABLE [dbo].[dim_proveedor](
	[id_proveedor] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[codigo_proveedor] [varchar](100) NOT NULL,
	[nombre_proveedor] [varchar](100) NOT NULL,
	[direccion_proveedor] [varchar](200) NOT NULL,
	[numero_proveedor] [varchar](50) NULL,
	[web_proveedor] [varchar](200) NULL
 CONSTRAINT [PK_dim_proveedor] PRIMARY KEY CLUSTERED 
(
	[id_proveedor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION PRODUCTO ----- ******/

CREATE TABLE [dbo].[dim_producto](
	[id_producto] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[codigo_producto] [varchar](100) NOT NULL,
	[nombre_producto] [varchar](100) NOT NULL,
	[marca_producto] [varchar](100) NOT NULL,
	[categoria] [varchar](100) NOT NULL,
 CONSTRAINT [PK_dim_producto] PRIMARY KEY CLUSTERED 
(
	[id_producto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION SUCURSAL ----- ******/

CREATE TABLE [dbo].[dim_sucursal](
	[id_sucursal] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[sod_su_sucursal] [varchar](50) NOT NULL,
	[nombre_sucursal] [varchar](100) NOT NULL,
	[direccion_sucursal] [varchar](200) NOT NULL,
 CONSTRAINT [PK_dim_sucursal] PRIMARY KEY CLUSTERED 
(
	[id_sucursal] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION REGION ----- ******/

CREATE TABLE [dbo].[dim_region](
	[id_region] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[nombre_region] [varchar](100) NOT NULL,
 CONSTRAINT [PK_dim_region] PRIMARY KEY CLUSTERED 
(
	[id_region] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION DEPARTAMENTO ----- ******/

CREATE TABLE [dbo].[dim_departamento](
	[id_departamento] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[nombre_departamento] [varchar](50) NOT NULL,
 CONSTRAINT [PK_dim_departamento] PRIMARY KEY CLUSTERED 
(
	[id_departamento] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION CLIENTE ----- ******/

CREATE TABLE [dbo].[dim_cliente](
	[id_cliente] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[codigo_cliente] [varchar](100) NOT NULL,
	[nombre_cliente] [varchar](100) NOT NULL,
	[tipo_cliente] [varchar](100) NOT NULL,
	[direccion_cliente] [varchar](200) NOT NULL,
	[numero_cliente] [varchar](50) NOT NULL,
 CONSTRAINT [PK_dim_cliente] PRIMARY KEY CLUSTERED 
(
	[id_cliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- DIMENSION VENDEDOR ----- ******/

CREATE TABLE [dbo].[dim_vendedor](
	[id_vendedor] [int] IDENTITY(1,1) NOT NULL UNIQUE,
	[codigo_vendedor] [varchar](100) NOT NULL,
	[nombre_vendedor] [varchar](100) NOT NULL,
	[vacacionista] [bit] NOT NULL,
 CONSTRAINT [PK_dim_vendedor] PRIMARY KEY CLUSTERED 
(
	[id_vendedor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** ----- HECHOS COMPRA ----- ******/

CREATE TABLE [dbo].[hechos_compra](
	[id_tiempo] [int] NOT NULL,
	[id_proveedor] [int] NOT NULL,
	[id_producto] [int] NOT NULL,
	[id_sucursal] [int] NOT NULL,
	[id_region] [int] NOT NULL,
	[id_departamento] [int] NOT NULL,
	[unidades] [int] NOT NULL,
	[costo_unitario] [numeric](18, 0) NOT NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[hechos_compra]  WITH CHECK ADD  CONSTRAINT [FK_hechos_compra_dim_departamento] FOREIGN KEY([id_departamento])
REFERENCES [dbo].[dim_departamento] ([id_departamento])
GO

ALTER TABLE [dbo].[hechos_compra] CHECK CONSTRAINT [FK_hechos_compra_dim_departamento]
GO

ALTER TABLE [dbo].[hechos_compra]  WITH CHECK ADD  CONSTRAINT [FK_hechos_compra_dim_producto] FOREIGN KEY([id_producto])
REFERENCES [dbo].[dim_producto] ([id_producto])
GO

ALTER TABLE [dbo].[hechos_compra] CHECK CONSTRAINT [FK_hechos_compra_dim_producto]
GO

ALTER TABLE [dbo].[hechos_compra]  WITH CHECK ADD  CONSTRAINT [FK_hechos_compra_dim_proveedor] FOREIGN KEY([id_proveedor])
REFERENCES [dbo].[dim_proveedor] ([id_proveedor])
GO

ALTER TABLE [dbo].[hechos_compra] CHECK CONSTRAINT [FK_hechos_compra_dim_proveedor]
GO

ALTER TABLE [dbo].[hechos_compra]  WITH CHECK ADD  CONSTRAINT [FK_hechos_compra_dim_region] FOREIGN KEY([id_region])
REFERENCES [dbo].[dim_region] ([id_region])
GO

ALTER TABLE [dbo].[hechos_compra] CHECK CONSTRAINT [FK_hechos_compra_dim_region]
GO

ALTER TABLE [dbo].[hechos_compra]  WITH CHECK ADD  CONSTRAINT [FK_hechos_compra_dim_sucursal] FOREIGN KEY([id_sucursal])
REFERENCES [dbo].[dim_sucursal] ([id_sucursal])
GO

ALTER TABLE [dbo].[hechos_compra] CHECK CONSTRAINT [FK_hechos_compra_dim_sucursal]
GO

ALTER TABLE [dbo].[hechos_compra]  WITH CHECK ADD  CONSTRAINT [FK_hechos_compra_dim_tiempo] FOREIGN KEY([id_tiempo])
REFERENCES [dbo].[dim_tiempo] ([id_tiempo])
GO

ALTER TABLE [dbo].[hechos_compra] CHECK CONSTRAINT [FK_hechos_compra_dim_tiempo]
GO


/****** ----- HECHOS VENTA ----- ******/

CREATE TABLE [dbo].[hechos_venta](
	[id_tiempo] [int] NOT NULL,
	[id_cliente] [int] NOT NULL,
	[id_vendedor] [int] NOT NULL,
	[id_producto] [int] NOT NULL,
	[id_sucursal] [int] NOT NULL,
	[id_region] [int] NOT NULL,
	[id_departamento] [int] NOT NULL,
	[unidades] [int] NOT NULL,
	[precio_unitario] [numeric](18, 0) NOT NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_departamento] FOREIGN KEY([id_departamento])
REFERENCES [dbo].[dim_departamento] ([id_departamento])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_departamento]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_vendedor] FOREIGN KEY([id_vendedor])
REFERENCES [dbo].[dim_vendedor] ([id_vendedor])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_vendedor]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_producto] FOREIGN KEY([id_producto])
REFERENCES [dbo].[dim_producto] ([id_producto])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_producto]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[dim_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_cliente]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_region] FOREIGN KEY([id_region])
REFERENCES [dbo].[dim_region] ([id_region])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_region]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_sucursal] FOREIGN KEY([id_sucursal])
REFERENCES [dbo].[dim_sucursal] ([id_sucursal])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_sucursal]
GO

ALTER TABLE [dbo].[hechos_venta]  WITH CHECK ADD  CONSTRAINT [FK_hechos_venta_dim_tiempo] FOREIGN KEY([id_tiempo])
REFERENCES [dbo].[dim_tiempo] ([id_tiempo])
GO

ALTER TABLE [dbo].[hechos_venta] CHECK CONSTRAINT [FK_hechos_venta_dim_tiempo]
GO