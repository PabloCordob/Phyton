import pygame
pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600

# Crear la pantalla
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Cubo con Cámara")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
# Tamaño y posición inicial del cubo
cube_size = 26
cube_x = 50
cube_y = 470
initial_cube_y = cube_y

# Velocidad del cubo y de la cámara
speed = 5
camera_speed = 5

# Variables de salto
is_jumping = False
jump_count = 10

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variable para controlar la cámara
camera_x = 0
camera_moving = False

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                camera_moving = True
    
    keys = pygame.key.get_pressed()
    
    # Realizar el salto
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            cube_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10
    
    # Mover el cubo hacia adelante
    cube_x += speed

    # Lógica de caída del cubo
    if cube_y < initial_cube_y:
        cube_y += 10

    # Mover la cámara si es necesario
    if camera_moving:
        camera_x += camera_speed
    
    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar el cubo
    cubo=pygame.draw.rect(screen, blue, (cube_x - camera_x, cube_y, cube_size, cube_size))
    plataforma=pygame.draw.rect(screen, red, (10, 500, 200, 20))
    

    
    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)  # Limitar a 60 FPS

pygame.quit()