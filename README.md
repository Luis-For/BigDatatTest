# Proyecto Big Data con Apache Spark, PySpark y Jupyter

Este proyecto es una configuración mínima para trabajar con **Apache Spark** y analizar datasets grandes usando **PySpark** y **SQL**, con un entorno reproducible gracias a **Docker Compose**. Incluye un contenedor con Spark standalone y Jupyter Notebook para desarrollo interactivo.

---

## Estructura del proyecto

├── data/ # Dataset CSV o Parquet para análisis
│ └── data.csv
├── notebooks/ # Jupyter notebooks con análisis PySpark
│ └── análisis.ipynb
├── scripts/ # Scripts PySpark ejecutables
│ └── query.py
├── docker-compose.yml # Orquestador de contenedores
└── README.md # Este archivo


---

## Tecnologías usadas

- Apache Spark 3.x (Standalone)
- PySpark
- Jupyter Notebook
- Docker & Docker Compose

---

## Cómo usar el proyecto

### 1. Clonar este repositorio

```bash ```
```git clone https://github.com/tu_usuario/tu_repositorio.git```
```cd tu_repositorio ```

2. Coloca tus datos

Pon tu dataset (por ejemplo data.csv) dentro de la carpeta data/.
3. Levanta el entorno con Docker Compose

docker-compose up -d

Esto levantará:

   ``` Contenedor Spark standalone```

    ```Contenedor Jupyter Notebook accesible en http://localhost:8888```

4. Accede a Jupyter Notebook

Abre el navegador y ve a http://localhost:8888. El token aparecerá en la consola del contenedor o puedes configurarlo para no pedir token.

Dentro del notebook, podrás importar PySpark y cargar los datos desde /data/data.csv.
