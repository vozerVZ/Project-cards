import pygame


def draw(sc, sc_w, sc_h):
    #Opponent hand
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 9, sc_h // 20, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 12, sc_h // 20, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 15, sc_h // 20, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 18, sc_h // 20, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 21, sc_h // 20, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 24, sc_h // 20, sc_w // 34 * 2, sc_h // 7), 2)
    #----------------
    #Opponent table
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 4, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 7, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 10, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 13, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 16, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 19, sc_h // 20 * 5, sc_w // 12, sc_h // 5), 2)
    #----------------
    # Player hand
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 8, sc_h // 20 * 17, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 11, sc_h // 20 * 17, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 14, sc_h // 20 * 17, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 17, sc_h // 20 * 17, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 20, sc_h // 20 * 17, sc_w // 34 * 2, sc_h // 7), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 34 * 23, sc_h // 20 * 17, sc_w // 34 * 2, sc_h // 7), 2)
    # ----------------
    # Player table
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 4, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 7, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 10, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 13, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 16, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 19, sc_h // 20 * 11, sc_w // 12, sc_h // 5), 2)
    # ----------------
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 23, sc_h // 20 * 5, sc_w // 24, sc_h // 5), 2)  # Opponent deck
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 25 * 23, sc_h // 20 * 11, sc_w // 24, sc_h // 5), 2)  # Player deck
    pygame.draw.rect(sc, [0, 0, 0], (sc_w // 20 * 18, sc_h // 80 * 41, sc_w // 12, sc_h // 20), 2)  # Ready button
