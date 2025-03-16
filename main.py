from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('fon.jpg'), (700,500))
game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    clock.tick(fps)
    display.update()