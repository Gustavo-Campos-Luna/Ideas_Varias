import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver
def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    driver_path = r"C:\Users\Gustavo Campos\Documents\Programacion\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Función para acceder al sitio y buscar la ciudad
def buscar_ciudad(driver, ciudad):
    driver.get("https://www.meteored.cl/")
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "search_pc"))
    )
    search_box.clear()
    search_box.send_keys(ciudad)
    search_box.send_keys(u'\ue007')  # Presionar Enter

# Función para extraer información y convertirla a un DataFrame
def extraer_informacion(driver):
    try:
        bloque_texto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dias_w"))
        ).text
        lineas = bloque_texto.split("\n")
        dias, fechas, temperaturas, vientos = [], [], [], []
        for i in range(0, len(lineas), 4):
            if i + 3 < len(lineas):  # Asegurar que el bloque está completo
                dias.append(lineas[i])
                fechas.append(lineas[i + 1])
                temperaturas.append(lineas[i + 2])
                vientos.append(lineas[i + 3])
        df = pd.DataFrame({
            "Día": dias,
            "Fecha": fechas,
            "Temperatura": temperaturas,
            "Viento": vientos
        })
        print(df)
        return df
    except Exception as e:
        print(f"Error al extraer información: {e}")
        return pd.DataFrame()

# Función para guardar el DataFrame en un archivo CSV o Excel
def guardar_datos(df, ciudad, archivo_csv=None, archivo_excel=None):
    archivo_csv = archivo_csv if archivo_csv else f"resultados_{ciudad}.csv"
    archivo_excel = archivo_excel if archivo_excel else f"resultados_{ciudad}.xlsx"
    try:
        df.to_csv(archivo_csv, index=False, encoding="utf-8-sig")
        print(f"Datos guardados en {archivo_csv}")
        df.to_excel(archivo_excel, index=False, engine="openpyxl")
        print(f"Datos guardados en {archivo_excel}")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Función principal para ejecutar el flujo
def main():
    try:
        driver = configurar_driver()
        ciudad = input("Ingresa el nombre de la ciudad a buscar: ")
        buscar_ciudad(driver, ciudad)
        time.sleep(5)
        df = extraer_informacion(driver)
        guardar_datos(df, ciudad)
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
