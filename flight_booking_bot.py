import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

# Base de conocimiento: lista de destinos y precios
destinos = [
    {"ciudad": "Nueva York", "continente": "América", "precio": 500},
    {"ciudad": "Los Ángeles", "continente": "América", "precio": 450},
    {"ciudad": "Miami", "continente": "América", "precio": 400},
    {"ciudad": "Buenos Aires", "continente": "América", "precio": 600},
    {"ciudad": "Ciudad de México", "continente": "América", "precio": 550},
    {"ciudad": "Toronto", "continente": "América", "precio": 480},
    {"ciudad": "París", "continente": "Europa", "precio": 600},
    {"ciudad": "Londres", "continente": "Europa", "precio": 550},
    {"ciudad": "Madrid", "continente": "Europa", "precio": 500},
    {"ciudad": "Roma", "continente": "Europa", "precio": 520},
    {"ciudad": "Berlín", "continente": "Europa", "precio": 530},
    {"ciudad": "Ámsterdam", "continente": "Europa", "precio": 540},
    {"ciudad": "Tokio", "continente": "Asia", "precio": 700},
    {"ciudad": "Pekín", "continente": "Asia", "precio": 650},
    {"ciudad": "Seúl", "continente": "Asia", "precio": 680},
    {"ciudad": "Bangkok", "continente": "Asia", "precio": 620},
    {"ciudad": "Singapur", "continente": "Asia", "precio": 700},
    {"ciudad": "Delhi", "continente": "Asia", "precio": 640},
    {"ciudad": "Sídney", "continente": "Oceanía", "precio": 800},
    {"ciudad": "Melbourne", "continente": "Oceanía", "precio": 750},
    {"ciudad": "Auckland", "continente": "Oceanía", "precio": 780},
    {"ciudad": "Brisbane", "continente": "Oceanía", "precio": 770},
    {"ciudad": "Perth", "continente": "Oceanía", "precio": 760},
    {"ciudad": "Adelaida", "continente": "Oceanía", "precio": 750}
]

# Filtra los destinos disponibles según el continente y el presupuesto.
def obtener_destinos(continente, presupuesto):
    return [d for d in destinos if d["continente"].lower() == continente.lower() and d["precio"] <= presupuesto]

# Muestra los destinos filtrados según los criterios del usuario.
def mostrar_destinos_filtrados(continente, presupuesto):
    destinos_filtrados = obtener_destinos(continente, presupuesto)
    
    if destinos_filtrados:
        mensaje = "Destinos disponibles según tus criterios:\n"
        for i, destino in enumerate(destinos_filtrados, 1):
            mensaje += f"{i}. {destino['ciudad']} - ${destino['precio']}\n"
    else:
        mensaje = "No hay destinos disponibles que se ajusten a tus criterios."
    
    return destinos_filtrados, mensaje

# Reserva un destino basado en el número seleccionado por el usuario.
def reservar_destino(destinos_filtrados, num_destino):
    if 1 <= num_destino <= len(destinos_filtrados):
        destino_seleccionado = destinos_filtrados[num_destino - 1]
        return f"Has reservado un billete a {destino_seleccionado['ciudad']} por ${destino_seleccionado['precio']}. ¡Buen viaje!"
    else:
        return "Opción no válida."

# Muestra la lista de destinos disponibles en una nueva ventana.
def mostrar_lista_destinos(root, destinos_filtrados):
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Destinos Disponibles")
    ventana_lista.geometry("400x300")
    
    texto = scrolledtext.ScrolledText(ventana_lista, wrap=tk.WORD, width=50, height=15)
    texto.pack(padx=10, pady=10)
    
    mensaje = "Destinos disponibles según tus criterios:\n"
    for i, destino in enumerate(destinos_filtrados, 1):
        mensaje += f"{i}. {destino['ciudad']} - ${destino['precio']}\n"
    
    texto.insert(tk.INSERT, mensaje)
    texto.config(state=tk.DISABLED)
    
    return ventana_lista

# Interactúa con el usuario para obtener el continente, presupuesto y realiza la reserva.
def interactuar_con_bot():
    root = tk.Tk()
    root.withdraw()
    
    tk.messagebox.showinfo("Bienvenido", "Bienvenido al Bot de Reserva de Billetes de Avión")
    
    while True:
        continente = simpledialog.askstring("Continente", "¿A qué continente quieres viajar? (América, Europa, Asia, Oceanía):")
        if continente and continente.lower() in ["américa", "europa", "asia", "oceanía"]:
            break
        else:
            messagebox.showerror("Error", "Por favor, ingresa un continente válido: América, Europa, Asia, Oceanía.")
    
    while True:
        try:
            presupuesto = simpledialog.askfloat("Presupuesto", "¿Cuál es tu presupuesto máximo en dólares?")
            if presupuesto is not None and presupuesto > 0:
                break
            else:
                messagebox.showerror("Error", "Por favor, ingresa un presupuesto válido (número mayor que 0).")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
    
    destinos_filtrados, mensaje = mostrar_destinos_filtrados(continente, presupuesto)
    messagebox.showinfo("Destinos disponibles", mensaje)
    
    if destinos_filtrados:
        while True:
            opcion = simpledialog.askstring("Reserva", "¿Quieres reservar uno de estos destinos? (sí/no):").strip().lower()
            if opcion in ["sí", "si", "SI", "Si", "no"]:
                break
            else:
                messagebox.showerror("Error", "Por favor, responde 'sí' o 'no'.")
        
        if opcion in ["sí", "si", "SI", "Si"]:
            ventana_lista = mostrar_lista_destinos(root, destinos_filtrados)
            while True:
                try:
                    num_destino = simpledialog.askinteger("Número de destino", "Ingresa el número del destino que quieres reservar:", parent=ventana_lista)
                    if num_destino is not None:
                        mensaje_reserva = reservar_destino(destinos_filtrados, num_destino)
                        if "Opción no válida" not in mensaje_reserva:
                            messagebox.showinfo("Reserva", mensaje_reserva, parent=ventana_lista)
                            break
                        else:
                            messagebox.showerror("Error", "Número de destino no válido. Por favor, ingresa un número de la lista.", parent=ventana_lista)
                    else:
                        break
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingresa un número válido.", parent=ventana_lista)
        else:
            messagebox.showinfo("Buscar de nuevo", "Puedes ejecutar el bot de nuevo para buscar otras opciones.")

if __name__ == "__main__":
    interactuar_con_bot()
