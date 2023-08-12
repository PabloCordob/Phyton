import pygame
pygame.init()

#colores
black = (0,0,0)
blanco = (255, 255, 255)

screen_size = (800, 600)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

pygame.display.set_caption("Pong")

fondo=pygame.image.load("imagen.jpg").convert()

player1=pygame.image.load("jugador1.png").convert()
player2=pygame.image.load("jugador2.png").convert()

sonido_de_golpe=pygame.mixer.Sound("beep.ogg")

pantalla_inicio = True
fuente_grande = pygame.font.Font(None, 72)
texto_inicio = fuente_grande.render("Pong Game", True, blanco)
fuente = pygame.font.Font(None, 36)
texto_instrucciones = fuente.render("Presiona ESPACIO para empezar", True, blanco)

#puntuacion de los jugadores
puntuacion_jugador1 = 0
puntuacion_jugador2 = 0
fuente = pygame.font.Font(None, 36)


#velocidad y movimento del jugador
jugador1_y_speed=0
cord_y1=300-45
cord_x1=50

#velocidad y movimiento del jugador2
jugador2_y_speed=0
cord_y2=300-45

cord_x2=750 - 15
#velocidad de la pelota y movimiento
pelota_speed_x = 5
pelota_speed_y = 5
pelota_x = 400
pelota_y = 300

game_over = False

while not game_over:
    for event in pygame.event.get():
        #controles
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                jugador1_y_speed = -4
            if event.key == pygame.K_s:
                jugador1_y_speed = 4
     
            if event.key == pygame.K_UP:
                jugador2_y_speed = -4
            if event.key == pygame.K_DOWN:
                jugador2_y_speed = 4

        if event.type == pygame.KEYUP:
            jugador1_y_speed = 0
            if event.key == pygame.K_w:
                jugador1_y_speed = 0
            if event.key == pygame.K_s:
                jugador1_y_speed = 0
            if event.key == pygame.K_UP:
                jugador2_y_speed = 0
            if event.key == pygame.K_DOWN:
                jugador2_y_speed = 0
    
    #colocacion y posicion de background
    screen.blit(fondo, [0, -100]) 
    
    if pelota_x < 0:
        puntuacion_jugador2 += 1
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1

    # Si la pelota sale de la pantalla por el lado derecho
    if pelota_x > 800:
        puntuacion_jugador1 += 1
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1

    #limite de el jugador 1
    if cord_y1 < 0:
        cord_y1 = 0
    if cord_y1 > 510:
        cord_y1 = 510
    #limite del jugador 2
    if cord_y2 < 0:
        cord_y2 = 0
    if cord_y2 > 510:
        cord_y2 = 510
    #rebote de pelota
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    
    if pelota_x > 800 or pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        #si sale de pantalla invierte la posicion
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    #movimiento de jugadores
    cord_y1 += jugador1_y_speed
    cord_y2 += jugador2_y_speed
    
    #movimiento de la pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y        
    

    #objetos
    jugador1 = pygame.draw.rect(screen , blanco,(cord_x1, cord_y1, 15, 90))#posicion y tamaño del jugador1
    jugador2 = pygame.draw.rect(screen , blanco,(cord_x2, cord_y2, 15, 90))#posicion y tamaño del jugador 2
    pelota = pygame.draw.circle(screen, blanco,(pelota_x, pelota_y), 10)#tamaño de la pelota

    #cualicion y sonido
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1
        sonido_de_golpe.play()
    
    #puntaje
    puntuacion_texto = fuente.render(f"           {puntuacion_jugador1}  Puntos  {puntuacion_jugador2}", True, blanco)
    screen.blit(puntuacion_texto, (250, 10))
    
    #imagen de jugadores
    screen.blit(player1, jugador1)
    screen.blit(player2, jugador2)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


