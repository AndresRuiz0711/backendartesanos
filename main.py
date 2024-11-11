from fastapi import FastAPI, HTTPException, Query
from database import get_db_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de Artesanos!"}
    

# Endpoint 1: Listar todos los artesanos (con paginación)
@app.get("/api/artesanos")
def get_artesanos(page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artesanos LIMIT %s OFFSET %s", (size, offset))
    artesanos = cur.fetchall()
    cur.close()
    conn.close()
    if not artesanos:
        raise HTTPException(status_code=404, detail="No se encontraron artesanos")
    return artesanos

# Endpoint 2: Listar los datos del artesano asociado a un ID
@app.get("/api/artesanos/{artesano_id}")
def get_artesano(artesano_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artesanos WHERE id = %s", (artesano_id,))
    artesano = cur.fetchone()
    cur.close()
    conn.close()
    if artesano is None:
        raise HTTPException(status_code=404, detail="Artesano no encontrado")
    return artesano

# Endpoint 3: Listar todos los productos (con paginación)
@app.get("/api/productos")
def get_productos(page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos LIMIT %s OFFSET %s", (size, offset))
    productos = cur.fetchall()
    cur.close()
    conn.close()
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos")
    return productos

# Endpoint 4: Listar los datos del producto asociado a un ID
@app.get("/api/productos/{producto_id}")
def get_producto(producto_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
    producto = cur.fetchone()
    cur.close()
    conn.close()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# Endpoint 5: Relación de imágenes asociadas a un artesano
@app.get("/api/imagenes/artesano/{artesano_id}")
def get_imagenes_artesano(artesano_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM imagenes WHERE artesano_id = %s", (artesano_id,))
    imagenes = cur.fetchall()
    cur.close()
    conn.close()
    if not imagenes:
        raise HTTPException(status_code=404, detail="No se encontraron imágenes para el artesano")
    return imagenes

# Endpoint 6: Relación de imágenes asociadas a un producto
@app.get("/api/imagenes/producto/{producto_id}")
def get_imagenes_producto(producto_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM imagenes WHERE producto_id = %s", (producto_id,))
    imagenes = cur.fetchall()
    cur.close()
    conn.close()
    if not imagenes:
        raise HTTPException(status_code=404, detail="No se encontraron imágenes para el producto")
    return imagenes

# Endpoint 7: Listado de artesanos por departamento (con paginación)
@app.get("/api/artesanos/departamento/{departamento_id}")
def get_artesanos_por_departamento(departamento_id: int, page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artesanos WHERE departamento_id = %s LIMIT %s OFFSET %s", 
                (departamento_id, size, offset))
    artesanos = cur.fetchall()
    cur.close()
    conn.close()
    if not artesanos:
        raise HTTPException(status_code=404, detail="No se encontraron artesanos en este departamento")
    return artesanos



# Endpoint 8: Listado de artesanos por departamento y municipio
@app.get("/api/artesanos/departamento/{departamento_id}/municipio/{municipio_id}")
def get_artesanos_por_departamento_municipio(departamento_id: int, municipio_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM artesanos 
        WHERE departamento_id = %s AND municipio_id = %s
    """, (departamento_id, municipio_id))
    artesanos = cur.fetchall()
    cur.close()
    conn.close()
    if not artesanos:
        raise HTTPException(status_code=404, detail="No se encontraron artesanos en este departamento y municipio")
    return artesanos

# Endpoint 9: Listado de artesanos cuya inicial del nombre inicie por una letra dada
@app.get("/api/artesanos/nombres/{letra}")
def get_artesanos_por_inicial_nombre(letra: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artesanos WHERE nombre ILIKE %s", (letra + '%',))
    artesanos = cur.fetchall()
    cur.close()
    conn.close()
    if not artesanos:
        raise HTTPException(status_code=404, detail="No se encontraron artesanos con esa inicial de nombre")
    return artesanos

# Endpoint 10: Listado de artesanos cuya inicial del apellido inicie por una letra dada (con paginación)
@app.get("/api/artesanos/apellidos/{letra}")
def get_artesanos_por_inicial_apellido(letra: str, page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artesanos WHERE apellido ILIKE %s LIMIT %s OFFSET %s", (letra + '%', size, offset))
    artesanos = cur.fetchall()
    cur.close()
    conn.close()
    if not artesanos:
        raise HTTPException(status_code=404, detail="No se encontraron artesanos con esa inicial de apellido")
    return artesanos

# Endpoint 11: Listado de artesanos por género (con paginación)
@app.get("/api/artesanos/genero/{genero}")
def get_artesanos_por_genero(genero: str, page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artesanos WHERE genero = %s LIMIT %s OFFSET %s", (genero, size, offset))
    artesanos = cur.fetchall()
    cur.close()
    conn.close()
    if not artesanos:
        raise HTTPException(status_code=404, detail="No se encontraron artesanos para este género")
    return artesanos

# Endpoint 12: Listado de productos por artesano
@app.get("/api/productos/artesano/{artesano_id}")
def get_productos_por_artesano(artesano_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos WHERE artesano_id = %s", (artesano_id,))
    productos = cur.fetchall()
    cur.close()
    conn.close()
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos para este artesano")
    return productos

# Endpoint 13: Listado de productos por rango de precio
@app.get("/api/productos/precio")
def get_productos_por_rango_precio(minPrice: float, maxPrice: float):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos WHERE precio BETWEEN %s AND %s", (minPrice, maxPrice))
    productos = cur.fetchall()
    cur.close()
    conn.close()
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos en este rango de precio")
    return productos

# Endpoint 14: Listado de productos por categoría (con paginación)
@app.get("/api/productos/categoria/{categoria_id}")
def get_productos_por_categoria(categoria_id: int, page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos WHERE categoria_id = %s LIMIT %s OFFSET %s", (categoria_id, size, offset))
    productos = cur.fetchall()
    cur.close()
    conn.close()
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos para esta categoría")
    return productos

# Endpoint 15: Listado de productos que contengan una cadena en el nombre o descripción (con paginación)
@app.get("/api/productos/busqueda")
def get_productos_por_busqueda(query: str, page: int = 0, size: int = 10):
    offset = page * size
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM productos 
        WHERE nombre ILIKE %s OR descripcion ILIKE %s
        LIMIT %s OFFSET %s
    """, ('%' + query + '%', '%' + query + '%', size, offset))
    productos = cur.fetchall()
    cur.close()
    conn.close()
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos con la búsqueda especificada")
    return productos
