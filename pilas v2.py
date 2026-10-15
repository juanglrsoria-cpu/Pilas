
import tkinter as tk
from tkinter import messagebox

pila = []
MAX_ELEMENTOS = 10

# Ventana principal
ventana = tk.Tk()
ventana.title("Visualizador de Pila - LIFO")
ventana.geometry("600x600")
ventana.configure(bg="#101827")
ventana.resizable(False, False)

# Titulo
tk.Label(
    ventana,
    text="VISUALIZADOR DE PILA",
    font=("Arial", 20, "bold"),
    bg="#101827",
    fg="white"
).pack(pady=15)

tk.Label(
    ventana,
    text="LIFO: Ultimo en entrar, primero en salir",
    font=("Arial", 11),
    bg="#101827",
    fg="#93c5fd"
).pack()

# Entrada de datos
entrada = tk.Entry(
    ventana,
    font=("Arial", 13),
    justify="center"
)
entrada.pack(pady=10)

# Lienzo grafico
canvas = tk.Canvas(
    ventana,
    width=400,
    height=300,
    bg="#0b1220",
    highlightthickness=0
)
canvas.pack(pady=10)

estado = tk.Label(
    ventana,
    text="Pila vacia",
    font=("Arial", 11),
    bg="#101827",
    fg="white"
)
estado.pack(pady=5)


def dibujar_pila():
    canvas.delete("all")

    x1, x2 = 100, 300
    base = 270
    altura = 25

    # Estructura de la pila
    canvas.create_line(
        x1, 25, x1, base,
        fill="white", width=4
    )
    canvas.create_line(
        x2, 25, x2, base,
        fill="white", width=4
    )
    canvas.create_line(
        x1 - 10, base, x2 + 10, base,
        fill="white", width=5
    )

    canvas.create_text(
        200, 15,
        text="CIMA",
        fill="#fbbf24",
        font=("Arial", 12, "bold")
    )

    # Dibujar los elementos
    for i, valor in enumerate(pila):
        y2 = base - i * altura
        y1 = y2 - altura + 2

        if i == len(pila) - 1:
            color = "#f59e0b"
        else:
            color = "#2563eb"

        canvas.create_rectangle(
            x1 + 5, y1,
            x2 - 5, y2 - 2,
            fill=color,
            outline="white"
        )

        texto = str(valor)
        if len(texto) > 20:
            texto = texto[:17] + "..."

        canvas.create_text(
            200, (y1 + y2) / 2,
            text=texto,
            fill="white",
            font=("Arial", 10, "bold")
        )

    if not pila:
        canvas.create_text(
            200, 240,
            text="Pila vacia",
            fill="#94a3b8",
            font=("Arial", 14)
        )

    cima = pila[-1] if pila else "Ninguna"

    estado.config(
        text=f"Elementos: {len(pila)} | Cima: {cima}"
    )


def apilar():
    valor = entrada.get().strip()

    if not valor:
        messagebox.showwarning(
            "Aviso", "Escribe un valor primero."
        )
        return

    if len(pila) >= MAX_ELEMENTOS:
        messagebox.showwarning(
            "Pila llena", "La pila alcanzo su limite."
        )
        return

    pila.append(valor)
    entrada.delete(0, tk.END)
    dibujar_pila()


def desapilar():
    if not pila:
        messagebox.showinfo(
            "Aviso", "La pila esta vacia."
        )
        return

    valor = pila.pop()
    dibujar_pila()

    messagebox.showinfo(
        "Elemento eliminado",
        f"Se elimino: {valor}"
    )


def ver_cima():
    if not pila:
        messagebox.showinfo(
            "Aviso", "La pila esta vacia."
        )
    else:
        messagebox.showinfo(
            "Cima de la pila",
            f"El elemento superior es: {pila[-1]}"
        )


def vaciar():
    pila.clear()
    dibujar_pila()


# Botones
marco = tk.Frame(ventana, bg="#101827")
marco.pack(pady=10)

tk.Button(
    marco, text="Apilar",
    command=apilar,
    bg="#2563eb", fg="white",
    width=10
).grid(row=0, column=0, padx=5)

tk.Button(
    marco, text="Desapilar",
    command=desapilar,
    bg="#dc2626", fg="white",
    width=10
).grid(row=0, column=1, padx=5)

tk.Button(
    marco, text="Ver cima",
    command=ver_cima,
    bg="#7c3aed", fg="white",
    width=10
).grid(row=0, column=2, padx=5)

tk.Button(
    marco, text="Vaciar",
    command=vaciar,
    bg="#475569", fg="white",
    width=10
).grid(row=0, column=3, padx=5)

entrada.bind("<Return>", lambda evento: apilar())

dibujar_pila()
ventana.mainloop()
