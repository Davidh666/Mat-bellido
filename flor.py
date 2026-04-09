from turtle import *
import colorsys
import random
import math

# --- Configuración Inicial ---
setup(900, 900)
bgcolor("black")
tracer(0) 

# --- Tortugas Independientes ---
flor_t = Turtle()
flor_t.hideturtle()

# Lista para gestionar los mensajes y poder borrarlos cuando haya muchos
tortugas_texto = []

celeste_t = Turtle()
celeste_t.hideturtle()
celeste_t.penup()

# --- Datos ---
mensajes = [
    "Te quiero",
    "No es mucho pero para iniciar el día...",
    "Quiero que sepas que ahí estaré yo",
    "Como tú estuviste para mí en el pasado",
    "Apóyate en mí como una leona hacia su león",
    "Como dos signos leonádicos juntos",
    "Como una luna a la que siempre veré en las noches",
    "Y yo el sol que alumbre tus mañanas"
]

fuentes = ["Times New Roman", "Georgia", "Palatino"]
colores_texto = ["mistyrose", "lavenderblush", "lightpink", "gold", "white"]

# --- Variables de Estado ---
h = 0
angulo_celeste = 0
fase_celeste = "luna"

# --- Funciones de Animación ---

def mostrar_mensajes(indice=0):
    # Si la pantalla tiene demasiados mensajes (ej. más de 12), borramos el primero
    if len(tortugas_texto) > 12:
        t_vieja = tortugas_texto.pop(0)
        t_vieja.clear()
        t_vieja.hideturtle()

    nueva_t = Turtle()
    nueva_t.hideturtle()
    nueva_t.penup()
    
    # Posiciones seguras para no tapar el centro de la flor ni el sol arriba
    x = random.choice([random.randint(-400, -200), random.randint(200, 400)])
    y = random.randint(-380, 250) # Evitamos el extremo superior para el Sol
    
    nueva_t.goto(x, y)
    fuente = random.choice(fuentes)
    color_sel = random.choice(colores_texto)
    nueva_t.color(color_sel)
    nueva_t.write(mensajes[indice % len(mensajes)], font=(fuente, 14, "italic"))
    
    tortugas_texto.append(nueva_t)
    
    # Bucle infinito de mensajes cada 2.5 segundos
    ontimer(lambda: mostrar_mensajes(indice + 1), 2500)

def cambiar_fase():
    global fase_celeste
    fase_celeste = "sol" if fase_celeste == "luna" else "luna"
    ontimer(cambiar_fase, 12000)

def dibujar_sol_mejorado(t, x, y):
    # Sol con degradado radial de naranja a amarillo
    for r in range(45, 0, -5):
        t.goto(x, y - r)
        t.begin_fill()
        t.color(1, 0.7 + (0.3 * (1 - r/45)), 0) 
        t.circle(r)
        t.end_fill()
    
    # Rayos finos y elegantes
    t.color("gold")
    t.width(1)
    for i in range(12):
        t.penup()
        t.goto(x, y)
        t.setheading(i * 30 + (angulo_celeste * 2)) 
        t.forward(50)
        t.pendown()
        t.forward(15)
        t.penup()

def dibujar_fondo_animado():
    global angulo_celeste
    celeste_t.clear()
    
    # Órbita alta y amplia para que el Sol luzca mejor
    radio_x = 380
    radio_y = 300
    x = radio_x * math.cos(math.radians(angulo_celeste))
    y = 300 + (radio_y * math.sin(math.radians(angulo_celeste))) # Elevado en el cielo
    
    if fase_celeste == "luna":
        celeste_t.goto(x, y)
        celeste_t.dot(65, "lightgray")
        celeste_t.dot(60, "white")
        celeste_t.goto(x + 18, y + 12)
        celeste_t.dot(65, "black")
    else:
        dibujar_sol_mejorado(celeste_t, x, y)

    angulo_celeste += 0.3 
    ontimer(dibujar_fondo_animado, 30)

# --- Bucle de la Flor ---
def dibujar_flor_paso_a_paso(i=0, j=0, h_val=0):
    if i < 16:
        if j < 18:
            c = colorsys.hsv_to_rgb(h_val, 1, 1)
            flor_t.color(c)
            
            flor_t.rt(90)
            flor_t.circle(150 - j * 6, 90)
            flor_t.lt(90)
            flor_t.circle(150 - j * 6, 90)
            flor_t.rt(180)
            
            update() 
            ontimer(lambda: dibujar_flor_paso_a_paso(i, j + 1, h_val + 0.005), 1)
        else:
            flor_t.circle(40, 24)
            ontimer(lambda: dibujar_flor_paso_a_paso(i + 1, 0, h_val), 1)
    else:
        # Cuando termine la flor, que no haga nada más pero el fondo siga
        pass

# --- Iniciar Todo ---
colormode(1.0)
mostrar_mensajes()
cambiar_fase()
dibujar_fondo_animado()
dibujar_flor_paso_a_paso()

done()