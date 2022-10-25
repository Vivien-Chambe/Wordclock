import time
import pygame 
import random as r

grid =[
        ["I","L","N","E","S","T","O","D","E","U","X"],
        ["Q","U","A","T","R","E","T","R","O","I","S"], 
        ["N","E","U","F","U","N","E","S","E","P","T"], 
        ["H","U","I","T","S","I","X","C","I","N","Q"], 
        ["M","I","D","I","X","M","I","N","U","I","T"], 
        ["O","N","Z","E","R","H","E","U","R","E","S"], 
        ["M","O","I","N","S","O","L","E","D","I","X"],
        ["E","T","R","Q","U","A","R","T","P","M","D"],
        ["V","I","N","G","T","-","C","I","N","Q","U"], 
        ["E","T","S","D","E","M","I","E","P","A","M"], 
        ]  

def print_clock (grid,font,screen,timestamp):
    
    hour = timestamp[0]
    minutes = timestamp[1]

    if minutes>30:
        hour = (hour+1)%24

##Print des heures
    for i in range(2):
        text = font.render(grid[0][i], True, (255, 255, 255))
        screen.blit(text, ((1+i)*50, 50))
    for i in range(3,6):
        text = font.render(grid[0][i], True, (255, 255, 255))
        screen.blit(text, ((1+i)*50, 50))

    if hour == 2 or hour == 14:
        for i in range(7,11):
            text = font.render(grid[0][i], True, (255, 255, 255))
            screen.blit(text, ((1+i)*50, 50))
    elif hour == 3 or hour == 4 or hour == 15 or hour == 16:
        y = 1
        if hour == 3 or hour == 15:
            for i in range(6,11):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        else:
            for i in range(0,6):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
    elif hour == 9 or hour == 1 or hour == 7 or hour == 21 or hour == 13 or hour == 19:
        y = 2
        if hour == 9 or hour == 21:
            for i in range(0,4):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        elif hour == 1 or hour == 13:
            for i in range(4,7):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        else:
            for i in range(7,11):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
    elif hour == 5 or hour == 6 or hour == 8 or hour == 17 or hour == 18 or  hour == 20:
        y = 3
        if hour == 5 or hour == 17:
            for i in range(7,11):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        elif hour == 6 or hour == 18:
            for i in range(4,7):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        else:
            for i in range(0,4):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
    elif hour == 10 or hour == 0 or hour == 22 or hour == 12:
        y = 4
        if hour == 10 or hour == 22:
            for i in range(2,5):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        elif hour == 0:
            for i in range(5,11):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
        else:
            for i in range(0,4):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
    else:
        y = 5
        if hour == 11 or hour == 23:
            for i in range(0,4):
                text = font.render(grid[y][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (y+1)*50))
    if hour !=0 and hour != 12:
        for i in range(5,10):
            text = font.render(grid[5][i], True, (255, 255, 255))
            screen.blit(text, ((1+i)*50, (6)*50))
        if hour != 1 and hour != 13:
            text = font.render(grid[5][10], True, (255, 255, 255))
            screen.blit(text, ((1+10)*50, (6)*50))

    ##Print des minutes
    if (minutes >= 15  and minutes <20) or (minutes >= 45 and minutes <50):
        if (minutes >= 15  and minutes <20):
            for i in range(0,2): ##ET premier
                text = font.render(grid[7][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (8)*50))
            for i in range(3,8): ##QUART
                text = font.render(grid[7][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (8)*50))
                ##print des minutes modulo 5
        elif (minutes >= 45 and minutes <50):
            for i in range(0,5): ##MOINS
                text = font.render(grid[6][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (7)*50))
            for i in range(6,8): ##LE
                text = font.render(grid[6][i], True, (255, 255, 255))
                screen.blit(text, ((1+i)*50, (7)*50))

    elif (minutes >= 30  and minutes <35):
        for i in range(0,2): ##ET deuxieme
            text = font.render(grid[9][i], True, (255, 255, 255))
            screen.blit(text, ((1+i)*50, (10)*50))
        for i in range(8,11): ##DEMI
            text = font.render(grid[7][i], True, (255, 255, 255))
            screen.blit(text, ((1+i)*50, (8)*50))




def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Word Clock")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 50)


    timestamp = [time.localtime()[3],time.localtime()[4]]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    timestamp = [r.randint(0,23),r.randint(0,59)]
                    print (timestamp)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return
        screen.fill((0, 0, 0))
        print_clock(grid,font,screen,timestamp)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()