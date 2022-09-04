from game import *


################# Main loop #####################

while not exit:


    # welcome stage
    if welcome_s == True:
        #print("welcome")
        welcome()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            # moving
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    welcome_s = False
                elif event.key == pygame.K_ESCAPE:
                    exit = True
        continue


    # pause stage
    if stop == True:
        #print("pause")
        puse()

        # key controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = False
                elif event.key == pygame.K_ESCAPE:
                    exit = True
        continue



    # game stage
    if game_over == False and stop == False:
        #print("game")
       # When snake eat the apple
        if apple_x == head_x and apple_y == head_y:
            apple_x = (random.randint(5,58)*10)
            apple_y = (random.randint(5,58)*10)
            speed = speed - 0.0005
            score = score + 1

       # key controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            # moving
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                elif event.key == pygame.K_ESCAPE:
                    stop = True

                    puse()


        # speed control
        time.sleep(speed)


        # snake changes
        head_x += x_change
        head_y += y_change

        snake_head = []
        snake_head.append(head_x)
        snake_head.append(head_y)
        snake_list.append(snake_head)


        # dispaly
        display.fill(green)
        frame()
        value = h3.render(f"loction = ({head_x},{head_y}), score = {score}, apple = {apple_x, apple_y}", True, black)
        display.blit(value, [10, 600])

        for part in snake_list:
             pygame.draw.rect(display, black, [part[0], part[1], 10, 10])

        if len(snake_list) > score + 1:
             del snake_list[0]

        pygame.draw.rect(display, black, [apple_x, apple_y, 10, 10])
        pygame.display.update()


        # When game over
        if score>=1:
            for block in range(0,len(snake_list)-1):
                if head_x == snake_list[block][0] and head_y == snake_list[block][1]:
                    game_over=True
        if head_x > 580 or head_x<10:
            game_over = True
        if head_y > 580 or head_y < 10:
            game_over = True



    if game_over == True:
        ggame_over()
        #print("game over")


        # key controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = False
                    game_over = False

                    head_x = window_width / 2
                    head_y = (window_height / 2) - 5
                    # snake_block = 10
                    # speed = 0.1
                    # snake_size = 10
                    #
                    # apple_x = (random.randint(1, 58) * 10)
                    # apple_y = (random.randint(1, 58) * 10)
                    #
                    # x_change = 0
                    # y_change = 0
                    #
                    # snake_list = []

                elif event.key == pygame.K_ESCAPE:
                    exit = True
        continue

    # exit
    if exit == True:
        #print("exit")
        pygame.quit()
        quit()



