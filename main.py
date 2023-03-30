#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Космическое путешествие"
FPS = 30

# Объекты и переменные
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
bullets = []
mode = 'ok'
type1 = Actor("ship", (100, 250))
type2 = Actor("ship-2", (300, 250))
type3 = Actor("ship-3", (500, 250))
count = 0
e = 0
d = 0
first = "a"

# Заполнение списка врагов
for i in range(5):
    p = random.randint(1,2)
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    x1 = random.randint(0, 600)
    y1 = random.randint(-450, -50)
    if p == 1:
        enemy = Actor("enemy", (x, y))
        enemy.speed = random.randint(2, 10)
        enemies.append(enemy)
    elif p == 2:
        meteor = Actor("meteor", (x1, y1))
        meteor.speed = random.randint(2, 10)
        enemies.append(meteor)
        
    


# Отрисовка
def draw():
    # Режим игры
    if first == "a":
        space.draw()
        screen.draw.text('Выберите сложность нажав на цифру', center = (300, 50), color = "white", fontsize = 30)
        screen.draw.text('1 - Легко', center = (300, 100), color = "white", fontsize = 36)
        screen.draw.text('2 - Сложно', center = (300, 150), color = "white", fontsize = 36)
        
    
    if mode == 'menu':
        space.draw()
        screen.draw.text('Выберите корабль', center = (300, 100), color = "white", fontsize = 36)
        type1.draw()
        type2.draw()
        type3.draw()
    if mode == 'game':
        space.draw()
        planets[0].draw()
        #Отрисовка счета
        screen.draw.text(count, (10, 10), color = "white")
        # Отрисовка метеоритов
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        # Отрисовка врагов
        for i in range(len(enemies)):
            enemies[i].draw()
        #Отрисовка пуль
        for i in range(len(bullets)):
            bullets[i].draw()
        
    # Окно проигрыша    
    elif mode == 'end':
        space.draw()
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
        #Итоговый счет
        screen.draw.text(count, center = (300, 250), color = "white", fontsize = 64)
    
# Управление
def on_mouse_move(pos):
    ship.pos = pos

# Добавление в список нового врага
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(e, d)
    enemies.append(enemy)

# Движение врагов
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

# Движение планет
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

# Движение метеоритов
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

# Столкновения
def collisions():
    global mode, count, d, e
    
    
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        #Столкновение с пуями
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[i]) :
                count = count + 1
               
                enemies.pop(i)
                bullets.pop(j)
                new_enemy()
                break
            
def update(dt):
    global first, e, d, mode
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        # Движение пуль
        for i in range(len(bullets)):
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y = bullets[i].y - 10
    elif keyboard.k_1 and first == "a":
        e = 2
        d = 10
        mode = "menu"    
        
    elif keyboard.k_2 and first == "a":
        e = 25
        d = 56
        mode = "menu"
    
        


#Функция обработки кликов
def on_mouse_down(button, pos):
    global mode
    global ship
    if mode == 'menu' and type1.collidepoint(pos):
        ship.image = "ship"
        mode = 'game'
    elif mode == 'menu' and type2.collidepoint(pos):
        ship.image = "ship-2"
        mode = 'game'
    elif mode == 'menu' and type3.collidepoint(pos):
        ship.image = "ship-3"
        mode = 'game'
    #Стрельба
    elif mode == 'game' and button == mouse.LEFT:
        bullet = Actor("bullet")
        bullet.pos = ship.pos
        bullets.append(bullet)
