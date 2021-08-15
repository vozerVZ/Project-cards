import pygame
#type, manacost, hp, damage for creature
#type, manacost, name for cast
cards_arr = [
    ["creature", 1, 1, 1],
    ["creature", 2, 2, 2],
    ["creature", 2, 3, 1],
    ["creature", 3, 3, 3],
    ["creature", 3, 4, 2],
    ["creature", 5, 4, 4],
    ["creature", 7, 7, 1],
    ["creature", 10, 8, 6],
    ["cast", 2, "arrow"]
]


class Card:
    def __init__(self, idd):
        self.id = idd
        self.type = cards_arr[self.id][0]
        self.manacost = cards_arr[self.id][1]
        if self.type == "creature":
            self.hp = cards_arr[self.id][2]
            self.damage = cards_arr[self.id][3]
            self.name = ""
        elif self.type == "cast":
            self.hp = 0
            self.damage = 0
            self.name = cards_arr[self.id][2]
        self.status = 0  # 0 - in deck 1 - destroyed 2 - in hand 3 - on table
        self.target_status = 0  # 0 - not in target 1 - chosen 2 - target
        self.x = -1
        self.y = -1
        self.width = -1
        self.height = -1
        self.isAttacked = False

    def set_status(self, status_id):
        self.status = status_id

    def get_status(self):
        return self.status

    def set_target_status(self, target_status_id):
        self.target_status = target_status_id

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_manacost(self):
        return self.manacost

    def damaged(self, dmg):
        self.hp -= dmg

    def get_damage(self):
        return self.damage

    def get_attacked_status(self):
        return self.isAttacked

    def set_attacked_status(self, attacked_status):
        self.isAttacked = attacked_status

    def get_hp(self):
        return self.hp

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def draw(self, sc, font, sc_w, sc_h, up_down):
        pygame.draw.rect(sc, [187, 187, 187], (self.x, self.y, self.width, self.height))

        if self.type == "creature":
            if up_down == 1 or up_down == 3:
                hp_text = font.render(str(self.hp), 1, [255, 0, 0])
                sc.blit(hp_text, (self.x, self.y + sc_h // 6))
                dmg_text = font.render(str(self.damage), 1, [0, 0, 0])
                sc.blit(dmg_text, (self.x + sc_w // 16, self.y + sc_h // 6))
                mana_text = font.render(str(self.manacost), 1, [0, 0, 255])
                sc.blit(mana_text, (self.x, self.y))

            if up_down == 2:
                hp_text = font.render(str(self.hp), 1, [255, 0, 0])
                sc.blit(hp_text, (self.x, self.y + sc_h // 9))
                dmg_text = font.render(str(self.damage), 1, [0, 0, 0])
                sc.blit(dmg_text, (self.x + sc_w // 26, self.y + sc_h // 9))
                mana_text = font.render(str(self.manacost), 1, [0, 0, 255])
                sc.blit(mana_text, (self.x, self.y))
        elif self.type == "cast" and up_down == 2:
            mana_text = font.render(str(self.manacost), 1, [0, 0, 255])
            sc.blit(mana_text, (self.x, self.y))

        if self.target_status == 1:
            pygame.draw.rect(sc, [0, 155, 0], (self.x, self.y, self.width, self.height), 3)
        elif self.target_status == 2:
            pygame.draw.rect(sc, [155, 0, 0], (self.x, self.y, self.width, self.height), 3)

    def update(self, sc, font, sc_w, sc_h, up_down, index):
        # up_down: 0 - opponent hand, 1 - opponent table, 2 - player hand, 3 - player table
        # index - number of card in drawing
        if up_down == 0:
            self.x = sc_w // 34 * (9 + 3 * index)
            self.y = sc_h // 20
            self.width = sc_w // 34 * 2
            self.height = sc_h // 7
        elif up_down == 1:
            self.y = sc_h // 20 * 5
            self.width = sc_w // 12
            self.height = sc_h // 5
            if index == 0:
                self.x = sc_w // 25
            else:
                self.x = sc_w // 25 * (4 + 3 * (index - 1))
        elif up_down == 2:
            self.x = sc_w // 34 * (8 + 3 * index)
            self.y = sc_h // 20 * 17
            self.width = sc_w // 34 * 2
            self.height = sc_h // 7
        elif up_down == 3:
            self.y = sc_h // 20 * 11
            self.width = sc_w // 12
            self.height = sc_h // 5
            if index == 0:
                self.x = sc_w // 25
            else:
                self.x = sc_w // 25 * (4 + 3 * (index - 1))

        self.draw(sc, font, sc_w, sc_h, up_down)
