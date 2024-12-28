import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

class Wallet:
    def __init__(self):
        self.ticks = []
        self.start = None
        self.end = None
        self.data = None

    def set_ticks(self):
        """
        Solicita al usuario que ingrese los ticks y verifica la cantidad ingresada.
        Si hay dos o más ticks, activa la comparación.
        """
        print("Ingresa los ticks de las acciones separados por comas (por ejemplo, 'AAPL, DJI, TSLA').")
        while True:
            user_input = input("Ticks: ")
            self.ticks = [f"^{tick.strip().upper()}" if tick.strip().upper() in ["DJI", "GSPC", "IXIC"] else tick.strip().upper() for tick in user_input.split(",")]
            if len(self.ticks) > 0:
                break
            else:
                print("No ingresaste ningún tick. Por favor, intenta nuevamente.")
        
        if len(self.ticks) == 1:
            print("Se ingresó 1 ticker. No se puede realizar comparación.")
        elif len(self.ticks) == 2:
            print("Se ingresaron 2 tickers. Activando comparación...")
        else:
            print(f"Se ingresaron {len(self.ticks)} tickers. Podrás elegir pares de tickers para comparar.")

    def set_dates(self):
        """
        Solicita las fechas de inicio y fin, validando el formato.
        """
        print("Ingresa las fechas en formato 'YYYY-MM-DD'. Por ejemplo, '2024-01-01'.")
        while True:
            try:
                self.start = input("Fecha de inicio: ")
                self.end = input("Fecha de fin: ")
                # Verificar formato de las fechas
                datetime.strptime(self.start, "%Y-%m-%d")
                datetime.strptime(self.end, "%Y-%m-%d")
                if self.start >= self.end:
                    print("La fecha de inicio debe ser anterior a la fecha de fin. Intenta nuevamente.")
                else:
                    break
            except ValueError:
                print("Formato de fecha inválido. Por favor, usa el formato 'YYYY-MM-DD'.")

    def download_info(self):
        """
        Descarga los datos de los ticks seleccionados.
        """
        try:
            self.data = yf.download(self.ticks, start=self.start, end=self.end)
            if self.data.empty:
                print("No se encontraron datos para los ticks y fechas ingresados. Verifica e inténtalo nuevamente.")
            else:
                print("La información ha sido descargada con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al descargar los datos: {e}")

    def show_ticks(self):
        """
        Muestra los ticks seleccionados.
        """
        print("Los ticks seleccionados son:")
        print(", ".join(self.ticks))

    def show_tick(self, tick):
        """
        Muestra la serie temporal de precios de cierre para un tick específico.
        """
        if tick in self.ticks:
            plt.figure(figsize=(10, 6))
            plt.title(f'Close Time Series for {tick}')
            plt.xlabel("Date")
            plt.ylabel("Price USD")
            plt.plot(self.data["Close"][tick], label=tick)
            plt.legend()
            plt.show()
        else:
            print(f"El tick {tick} no está incluido en la lista actual de ticks.")

    def compare_ticks(self):
        """
        Compara los precios de cierre de dos ticks seleccionados.
        """
        if len(self.ticks) == 2:
            # Si hay exactamente 2 acciones, hacemos la comparación
            tick1 = self.ticks[0]
            tick2 = self.ticks[1]
            plt.figure(figsize=(10, 6))
            plt.title(f'{tick1} versus {tick2}: Close Value')
            plt.xlabel(tick1)
            plt.ylabel(tick2)
            plt.plot(self.data["Close"][tick1], self.data["Close"][tick2], 'x')
            plt.show()
        else:
            print("Se necesitan exactamente 2 tickers para realizar la comparación.")
            return

    def compare_multiple_ticks(self):
        """
        Permite seleccionar pares de tickers para realizar comparaciones si hay más de 2 tickers.
        """
        while True:
            print("\nSelecciona los tickers que deseas comparar.")
            for idx, tick in enumerate(self.ticks, start=1):
                print(f"{idx}. {tick}")
            
            try:
                choice1 = int(input(f"Selecciona el primer ticker (1-{len(self.ticks)}): "))
                if 1 <= choice1 <= len(self.ticks):
                    chosen_tick1 = self.ticks[choice1 - 1]
                else:
                    print("Número fuera de rango. Intenta nuevamente.")
                    continue
                
                choice2 = int(input(f"Selecciona el segundo ticker (1-{len(self.ticks)}): "))
                if 1 <= choice2 <= len(self.ticks) and choice2 != choice1:
                    chosen_tick2 = self.ticks[choice2 - 1]
                else:
                    print("Número fuera de rango o seleccionaste el mismo ticker. Intenta nuevamente.")
                    continue
                
                # Realizar la comparación
                plt.figure(figsize=(10, 6))
                plt.title(f'{chosen_tick1} versus {chosen_tick2}: Close Value')
                plt.xlabel(chosen_tick1)
                plt.ylabel(chosen_tick2)
                plt.plot(self.data["Close"][chosen_tick1], self.data["Close"][chosen_tick2], 'x')
                plt.show()

                # Preguntar si desea comparar otro par
                again = input("¿Quieres comparar otro par de tickers? (S/N): ").strip().upper()
                if again != "S":
                    print("Fin de las comparaciones.")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, selecciona números válidos.")

    def returns(self):
        """
        Pregunta al usuario qué ticker quiere analizar para los retornos y luego calcula y muestra el histograma.
        """
        while True:
            print("Selecciona un ticker para calcular los retornos:")
            for idx, tick in enumerate(self.ticks, start=1):
                print(f"{idx}. {tick}")
            
            try:
                # Elige el ticker por su índice
                choice = int(input(f"Selecciona el número (1-{len(self.ticks)}): "))
                if 1 <= choice <= len(self.ticks):
                    chosen_tick = self.ticks[choice - 1]
                    returns = self.data["Close"][chosen_tick].pct_change().dropna()
                    plt.figure(figsize=(10, 10))
                    plt.title(f'Histogram of {chosen_tick} returns')
                    plt.hist(returns, bins=50)
                    plt.show()
                    break
                else:
                    print("Número fuera de rango. Intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, selecciona un número de la lista.")

        # Preguntar si quiere calcular los retornos de otra acción
        again = input("¿Quieres calcular los retornos de otra acción? (S/N): ").strip().upper()
        if again == "S":
            self.returns()
    
    def analyze_volatility(self):
        # Calcula y visualiza la volatilidad histórica (desviación estándar de retornos diarios)
        # para los tickers seleccionados. Permite al usuario calcular la volatilidad de varias acciones.
        
        if self.data is None or self.data.empty:
            print("No hay datos disponibles. Descarga los datos primero.")
            return   
        
        while True:
            print("\nSelecciona un ticker para calcular la volatilidad:")
            for idx, tick in enumerate(self.ticks, start=1):
                print(f"{idx}. {tick}")
            
            try:
                choice = int(input(f"Selecciona el número (1-{len(self.ticks)}): "))
                if 1 <= choice <= len(self.ticks):
                    chosen_tick = self.ticks[choice - 1]
                    returns = self.data["Close"][chosen_tick].pct_change().dropna()
                    volatility = returns.std() * (252 ** 0.5)  # Escalado anualizado
                    print(f"\nLa volatilidad anualizada de {chosen_tick} es: {volatility:.2%}")
                    
                    # Preguntar si se desea continuar
                    another = input("¿Quieres calcular la volatilidad de otra acción? (S/N): ").strip().upper()
                    if another != 'S':
                        print("Análisis de volatilidad finalizado.")
                        break
                else:
                    print("Número fuera de rango. Intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, selecciona un número de la lista.")

    def export_data(self):
        """
        Permite al usuario exportar los datos descargados o calculados a un archivo CSV o cancelar la operación.
        """
        if self.data is None or self.data.empty:
            print("No hay datos disponibles para exportar. Asegúrate de descargar primero los datos.")
            return
        
        while True:
            print("\n¿Quieres exportar los datos? Elige un formato:")
            print("1. CSV")
            print("2. Cancelar")
            
            try:
                choice = int(input("Selecciona el número (1-2): "))
                if choice == 1:
                    # Exportar a CSV
                    file_name = input("Ingresa el nombre del archivo (sin extensión): ") + ".csv"
                    self.data.to_csv(file_name)
                    print(f"Datos exportados exitosamente a {file_name}.")
                    break
                elif choice == 2:
                    print("Exportación cancelada.")
                    break
                else:
                    print("Opción inválida. Intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, selecciona un número de la lista.")


# 1. Inicialización
w = Wallet()

# 2. Configuración
w.set_ticks()  # Si el usuario ingresa 2 tickers, no se activa la comparación hasta después de descargar los datos
w.set_dates()  # Permite al usuario ingresar las fechas
w.download_info()  # Descarga los datos

# 3. Uso de funcionalidades
w.show_ticks()  # Muestra los ticks seleccionados

# Llamada a la función compare_ticks() solo después de descargar los datos
if len(w.ticks) == 2:
    w.compare_ticks()  # Si hay exactamente 2 tickers, se comparan directamente
elif len(w.ticks) > 2:
    w.compare_multiple_ticks()  # Si hay más de 2 tickers, permite seleccionar pares para comparar

# Llamada a la función returns() para calcular los retornos de un ticker
w.returns()

# Llamada a la función analyze_volatility() para calcular la volatilidad de un ticker
w.analyze_volatility()

# Llamada para exportar data
w.export_data()
