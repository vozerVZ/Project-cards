#TYPE:DEV
#CODE:Project:cards
import pygame
import card
import layout
import random
import sys


def collide_check():
    for p in enemy_hand:
        if p.get_rect().collidepoint(mouse_x, mouse_y):
            return True

    for p in enemy_table:
        if p.get_rect().collidepoint(mouse_x, mouse_y):
            return True

    for p in player_hand:
        if p.get_rect().collidepoint(mouse_x, mouse_y):
            return True

    for p in player_table:
        if p.get_rect().collidepoint(mouse_x, mouse_y):
            return True

    if pygame.Rect(screen_width//6*5, 0, screen_width//6, screen_height//5).collidepoint(mouse_x, mouse_y):
        return True

    return False


def collide_object():
    for o in enemy_hand:
        if o.get_rect().collidepoint(mouse_x, mouse_y):
            return [o, 0]

    for o in enemy_table:
        if o.get_rect().collidepoint(mouse_x, mouse_y):
            return [o, 1]

    for o in player_hand:
        if o.get_rect().collidepoint(mouse_x, mouse_y):
            return [o, 2]

    for o in player_table:
        if o.get_rect().collidepoint(mouse_x, mouse_y):
            return [o, 3]

    if pygame.Rect(screen_width//6*5, 0, screen_width//6, screen_height//5).collidepoint(mouse_x, mouse_y):
        return [-1, 4]

    return [-1, -1]


def draw_ground():
    screen.fill([255, 255, 255])

    layout.draw(screen, screen_width, screen_height)

    opponent_mana_text = font1.render(str(enemy_mana), 1, [0, 0, 255])
    screen.blit(opponent_mana_text, (screen_width // 100 * 24, screen_height // 70))

    player_mana_text = font1.render(str(player_mana), 1, [0, 0, 255])
    screen.blit(player_mana_text, (screen_width // 100 * 77, screen_height * 0.965))

    enemy_hp_text = font1.render(str(enemy_hp), 1, [255, 0, 0])
    screen.blit(enemy_hp_text, (screen_width // 6 * 5, 0))

    player_hp_text = font1.render(str(player_hp), 1, [255, 0, 0])
    screen.blit(player_hp_text, (0, screen_height - screen_height // 5))

    for i in range(0, len(enemy_hand)):
        enemy_hand[i].update(screen, font1, screen_width, screen_height, 0, i)

    for i in range(0, len(enemy_table)):
        enemy_table[i].update(screen, font1, screen_width, screen_height, 1, i)

    for i in range(0, len(player_hand)):
        player_hand[i].update(screen, font1, screen_width, screen_height, 2, i)

    for i in range(0, len(player_table)):
        player_table[i].update(screen, font1, screen_width, screen_height, 3, i)

    if turn == 0:
        pygame.draw.rect(screen, [0, 165, 80], (screen_width // 20 * 18, screen_height // 80 * 41, screen_width // 12, screen_height // 20))
    else:
        pygame.draw.rect(screen, [255, 0, 51], (screen_width // 20 * 18, screen_height // 80 * 41, screen_width // 12, screen_height // 20))


pygame.init()
resolution = pygame.display.Info()
screen_width = resolution.current_w
screen_height = resolution.current_h

clock = pygame.time.Clock()

size = [screen_width, screen_height]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

HAND_MAX_SIZE = 6
TABLE_MAX_SIZE = 7
MAX_MANA_VALUE = 10

enemy_max_hp = 30
enemy_hp = enemy_max_hp
enemy_max_mana = 0
enemy_mana = enemy_max_mana
enemy_deck = []
enemy_hand = []
enemy_table = []
for i in range(3):
    enemy_deck.append(card.Card(0))
    enemy_deck.append(card.Card(1))
    enemy_deck.append(card.Card(2))
    enemy_deck.append(card.Card(3))
    enemy_deck.append(card.Card(4))
    enemy_deck.append(card.Card(5))

enemy_deck.append(card.Card(6))
enemy_deck.append(card.Card(7))

for i in range(2):
    rand_obj = random.choice(enemy_deck)
    enemy_hand.append(rand_obj)
    enemy_deck.remove(rand_obj)

player_max_hp = 30
player_hp = player_max_hp
player_max_mana = 0
player_mana = player_max_mana
player_deck = []
player_hand = []
player_table = []

for i in range(3):
    player_deck.append(card.Card(0))
    player_deck.append(card.Card(1))
    player_deck.append(card.Card(2))
    player_deck.append(card.Card(3))
    player_deck.append(card.Card(4))
    player_deck.append(card.Card(5))

player_deck.append(card.Card(6))
player_deck.append(card.Card(7))

for i in range(2):
    rand_obj = random.choice(player_deck)
    player_hand.append(rand_obj)
    player_deck.remove(rand_obj)

font1 = pygame.font.Font(None, 35)

isDANActivate = False  # DAN - Drag N Drop
chosenObj = -1
targetObj = -1
cardFrom = -1  # 0 - table 1 - hand

turn = 0  # 0 - player turn 1 - opponent turn
game_status = 0  # 0 - game 1 - player win 2 - bot win

done = False

while not done:
    turn = 0
    flag = False
    #PLAYER TURN
    if player_max_mana < MAX_MANA_VALUE:
        player_max_mana += 1
    player_mana = player_max_mana

    if len(player_deck) > 0:
        rand_obj = random.choice(player_deck)
        if len(player_hand) < HAND_MAX_SIZE:
            player_hand.append(rand_obj)
        player_deck.remove(rand_obj)
    else:
        player_hp -= 1

    while not flag:
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif i.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                obj, stat = collide_object()
                if stat == 2 and not isDANActivate:
                    isDANActivate = True
                    chosenObj = obj
                    cardFrom = 1
                elif stat == 3 and not isDANActivate:
                    isDANActivate = True
                    chosenObj = obj
                    cardFrom = 0

            elif i.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                obj, stat = collide_object()
                for z in enemy_table:
                    z.set_target_status(0)
                if isDANActivate and stat == 1 and cardFrom == 0:
                    collide_object()[0].set_target_status(2)

            elif i.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if pygame.Rect(screen_width // 20 * 18, screen_height // 80 * 41, screen_width // 12, screen_height // 20).collidepoint(mouse_x, mouse_y):
                    flag = True
                if isDANActivate:
                    if not collide_check():
                        if chosenObj.get_manacost() <= player_mana and cardFrom == 1 and len(player_table) < TABLE_MAX_SIZE:
                            player_mana -= chosenObj.get_manacost()
                            player_table.append(chosenObj)
                            player_hand.remove(chosenObj)
                            chosenObj.set_attacked_status(True)
                    elif cardFrom == 0 and not chosenObj.get_attacked_status():
                        obj, stat = collide_object()
                        if stat == 4:
                            enemy_hp -= chosenObj.get_damage()
                            chosenObj.set_attacked_status(True)
                        elif stat == 1:
                            targetObj = obj
                            targetObj.damaged(chosenObj.get_damage())
                            chosenObj.damaged(targetObj.get_damage())
                            chosenObj.set_attacked_status(True)

                    chosenObj = -1
                    isDANActivate = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if collide_check() and not isDANActivate and collide_object()[0] != -1:
            collide_object()[0].set_target_status(1)

        if not isDANActivate:
            if not collide_check():
                for i in range(0, len(enemy_hand)):
                    enemy_hand[i].set_target_status(0)
                for i in range(0, len(enemy_table)):
                    enemy_table[i].set_target_status(0)
                for i in range(0, len(player_hand)):
                    player_hand[i].set_target_status(0)
                for i in range(0, len(player_table)):
                    player_table[i].set_target_status(0)

        draw_ground()

        for i in enemy_table:
            if i.get_hp() <= 0:
                enemy_table.remove(i)

        for i in player_table:
            if i.get_hp() <= 0:
                player_table.remove(i)

        pygame.display.flip()
        clock.tick(60)

        if enemy_hp <= 0:
            game_status = 1
            done = True
            flag = True
        elif player_hp <= 0:
            game_status = 2
            done = True
            flag = True
        #END OF PLAYER TURN
    for i in player_table:
        i.set_attacked_status(False)

    #BOT TURN
    if game_status == 0:
        turn = 1
        if enemy_max_mana < MAX_MANA_VALUE:
            enemy_max_mana += 1
        enemy_mana = enemy_max_mana
        if len(enemy_deck) > 0:
            rand_obj = random.choice(enemy_deck)
            if len(enemy_hand) < HAND_MAX_SIZE:
                enemy_hand.append(rand_obj)
            enemy_deck.remove(rand_obj)
        else:
            enemy_hp -= 1

        for q in enemy_table:
            number_of_choices = len(player_table)
            choice = random.randint(0, number_of_choices)
            if choice == number_of_choices:
                player_hp -= q.get_damage()
            else:
                player_table[choice].damaged(q.get_damage())
                q.damaged(player_table[choice].get_damage())

            for j in enemy_table:
                if j.get_hp() <= 0:
                    enemy_table.remove(j)

            for j in player_table:
                if j.get_hp() <= 0:
                    player_table.remove(j)

            q.set_attacked_status(True)

        for j in enemy_hand:
            if len(enemy_table) >= TABLE_MAX_SIZE:
                break
            else:
                curr_obj = j
                if curr_obj.get_manacost() <= enemy_mana:
                    enemy_mana -= curr_obj.get_manacost()
                    enemy_table.append(curr_obj)
                    enemy_hand.remove(curr_obj)

            draw_ground()

            pygame.display.flip()
            clock.tick(60)

            pygame.time.wait(random.randint(300, 1500))

            if enemy_hp <= 0:
                game_status = 1
                done = True
            elif player_hp <= 0:
                game_status = 2
                done = True
    #END OF BOT TURN
    for i in enemy_table:
        i.set_attacked_status(False)

    if enemy_hp <= 0:
        game_status = 1
        done = True
    elif player_hp <= 0:
        game_status = 2
        done = True

done = False

while not done:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                done = True

    if game_status == 1:
        screen.fill([0, 255, 0])
    else:
        screen.fill([255, 0, 0])

    pygame.display.flip()
    clock.tick(60)
