from variable import *

class Button():
    def __init__(self, color, pos):
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.w = pos[2]
        self.h = pos[3]
        self.n = 1

        self.clicked = False
    
    def get_rect(self):
        return (self.x, self.y, self.w, self.h)
    
    def change_color(self, new_color):
        self.color = new_color

    def title_button_right(self, text, size, dpos = [0,0]):
        font(text, (adjust_center_width(style=(self.x, self.w), o = size) + dpos[0], 
                    adjust_center_height(style=(self.y, self.h), o = size) + dpos[1]), 
                    size, "black")

    def draw(self, img = None, border = None, border_raidus = -1, show = False, good = False):
        pos = pygame.mouse.get_pos()
        action = False
        if border != None:
            rect = pygame.draw.rect(screen, border[0], (self.x - border[1],
                                                 self.y - border[1],
                                                 self.w + border[1] * 2,
                                                 self.h + border[1] * 2),
                                                 border_radius=border_raidus)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

        if img != None:
            screen.blit(img, adjust_center(img, (self.x, self.y, self.w, self.h)))

        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        return action
    
    def adjust_box_text(self, text = "Hello", pos_text = (None, None), size_text = 0, color_text = (0,0,0)):
        return text, pos_text, size_text, color_text
    
    def draw_box(self, text = "Đi bộ", img = None,size = 75):
        border1 = 5
        border_raidus1 = 5
        pos = pygame.mouse.get_pos()
        color_alpha = (0,0,0, 50)
        border_raidus = 10

        kp = 0

        img = pygame.transform.scale(img, (100,100))
        draw_rect_alpha(color_alpha, (0,0, screen_width, scren_height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), border_radius=border_raidus)

        font(text, (None, None), size, (0,0,0))

        screen.blit(img, (adjust_center_width(img, (self.x, self.w)),
                          adjust_center_height(img,(self.y, self.h)) - 95))
        
        pygame.draw.rect(screen, "black", (adjust_center_width(style = (self.x, self.w), o = 150) - 100 - border1,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 90 - border1, 150 + border1 * 2,50 + border1 * 2), border_radius=border_raidus1)
        
        decine = pygame.draw.rect(screen, "red", (adjust_center_width(style = (self.x, self.w), o = 150) - 100,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 90, 150,50))
        
        pygame.draw.rect(screen, "black", (adjust_center_width(style = (self.x, self.w), o = 150) + 100 - border1,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 90 - border1, 150 + border1 * 2,50 + border1 * 2), border_radius=border_raidus1)
        
        accept = pygame.draw.rect(screen, "lime", (adjust_center_width(style = (self.x, self.w), o = 150) + 100,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 90, 150,50))
        
        font("Từ Chối", (adjust_center_width(style = (self.x, self.w), o = 150) - 100 +35 // 2,
                         adjust_center_height(style = (self.y, self.h), o = 50) + 90), 35,"black")
        
        font("Chấp nhận", (adjust_center_width(style = (self.x, self.w), o = 150) + 84 + 35 // 2,
                        adjust_center_height(style = (self.y, self.h), o = 50) + 90), 35,"black")

        if decine.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 1
        
        elif accept.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 2
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return kp
    
    def draw_box_1(self, text = "Đi bộ", img = None,size = 75):
        border1 = 5
        border_raidus1 = 5
        pos = pygame.mouse.get_pos()
        color_alpha = (0,0,0, 50)
        border_raidus = 10

        kp = False
        
        img = pygame.transform.scale(dic2[img], (100,100))
        draw_rect_alpha(color_alpha, (0,0, screen_width, scren_height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), border_radius=border_raidus)
        font(text, (None, None), size, (0,0,0))

        screen.blit(img, (adjust_center_width(img, (self.x, self.w)),
                          adjust_center_height(img,(self.y, self.h)) - 95))
        
        pygame.draw.rect(screen, "black", (adjust_center_width(style = (self.x, self.w), o = 150) - 100 - border1,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 90 - border1, 350 + border1 * 2,50 + border1 * 2), border_radius=border_raidus1)
        
        accept = pygame.draw.rect(screen, "lime", (adjust_center_width(style = (self.x, self.w), o = 150) - 100,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 90, 350,50))
        
        font("OK", (adjust_center_width(style = (self.x, self.w), o = 150) + 35 +35 // 2,
                         adjust_center_height(style = (self.y, self.h), o = 50) + 90), 35,"black")

        if accept.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return kp

    def draw_box_2(self, your_store = None):
        """
            0 : img
            1 : text_result
            2 : [1,....,10]
            3 : time
        """
        border1 = 5
        border_raidus1 = 5
        pos = pygame.mouse.get_pos()
        color_alpha = (0,0,0, 50)
        border_raidus = 10

        kp = 0

        IMG = pygame.transform.scale(dic2[your_store[0]], (100,100))
        draw_rect_alpha(color_alpha, (0,0, screen_width, scren_height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), border_radius=border_raidus)

        font(your_store[1], (None, None, "OPS"), 35, (0,0,0), (self.x, self.y, self.w, self.h), (0, -150))

        screen.blit(IMG, (adjust_center_width(IMG, (self.x, self.w)),
                          adjust_center_height(IMG,(self.y, self.h)) - 250))
        
        delete_edge = 50
        delete_x = adjust_center_width(style = (self.x, self.w), o = delete_edge) + 325
        delete_y = adjust_center_height(style = (self.y, self.h), o = delete_edge) + 250

        pygame.draw.rect(screen, "black", (delete_x - border1, delete_y - border1, delete_edge + border1 * 2,
                                           delete_edge + border1 * 2), border_radius=border_raidus1)

        delete = pygame.draw.rect(screen, "red", (delete_x, delete_y, delete_edge, delete_edge))

        screen.blit(trash_icon,adjust_center(trash_icon,(delete_x, delete_y, delete_edge, delete_edge)))

        exit_width = 160
        exit_height = 60
        exit_x = adjust_center_width(style = (self.x, self.w), o = exit_width) + 200
        exit_y = adjust_center_height(style = (self.y, self.h), o = exit_height) + 250
        exit = pygame.draw.rect(screen, "black", (exit_x, exit_y, exit_width,exit_height), 5, border_radius=border_raidus1)
        
        font("Thoát", (None, None, "OPS"), 35,"black", (exit_x, exit_y, exit_width, exit_height))

        your_store_choice = list(sorted(your_store[2]))
        row1 = []; row2 = []; row3 = []
        dem_row = []

        xem_them_img = screen.blit(dau_cham_thang_xem_them_icon,(adjust_center_width(dau_cham_thang_xem_them_icon) + 350,
                                                  50))

        for i in your_store_choice:
            if khoang(i,1,4): 
                row1.append(i)
                
                if 1 not in dem_row:
                    dem_row.append(1)

            elif khoang(i,5,7): 
                row2.append(i)

                if 2 not in dem_row:
                    dem_row.append(2)

            elif khoang(i,8,10): 
                row3.append(i)

                if 3 not in dem_row:
                    dem_row.append(3)
        
        khung_width = 500
        khung_height = len(dem_row) * 100
        khung_x = adjust_center_width(style = (self.x, self.w), o = khung_width)
        khung_y = adjust_center_height(style = (self.y, self.h), o = khung_height) + 50

        Color_khung = None
        for i in range(1, len(dem_row) + 1):
            if i % 2 == 0:
                Color_khung = "white"
            
            else:
                Color_khung = (153, 204, 255)

            pygame.draw.rect(screen, Color_khung, (khung_x, khung_y + (100 * (i-1)), khung_width, 100), border_radius=10)

        pygame.draw.rect(screen,"black",(khung_x, khung_y, khung_width, khung_height), 5, border_radius=10)

        add_image_khung(your_store_choice, khung_x, khung_y, row1, row2,row3)

        font(f"{your_store[-1][0]}/{your_store[-1][1]}/20{your_store[-1][2]}", (None, scren_height - 150), 35, "black",d=(-100,20))
        font(f"{your_store[-1][3]} : {your_store[-1][4]}", (None, scren_height - 110), 35, "black",d=(-150,20))


        if delete.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 1
        
        elif exit.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 2
        
        if xem_them_img.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 3


        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return kp

    def draw_box_3(self, text, img = None, size = 75):
        border1 = 5
        border_raidus1 = 5
        pos = pygame.mouse.get_pos()
        color_alpha = (0,0,0, 50)
        border_raidus = 10

        kp = 0

        img = pygame.transform.scale(img, (100,100))
        draw_rect_alpha(color_alpha, (0,0, screen_width, scren_height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), border_radius=border_raidus)

        font(text, (None, None), size, (0,0,0), d = (0, -90))

        screen.blit(img, (adjust_center_width(img, (self.x, self.w)),
                          adjust_center_height(img,(self.y, self.h)) - 180))
        
        pygame.draw.rect(screen, "black", (adjust_center_width(style = (self.x, self.w), o = 150) - 170 - border1,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 190 - border1, 150 + border1 * 2,50 + border1 * 2), border_radius=border_raidus1)
        
        decine = pygame.draw.rect(screen, "red", (adjust_center_width(style = (self.x, self.w), o = 150) - 170,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 190, 150,50))
        
        pygame.draw.rect(screen, "black", (adjust_center_width(style = (self.x, self.w), o = 150) + 170 - border1,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 190 - border1, 150 + border1 * 2,50 + border1 * 2), border_radius=border_raidus1)
        
        accept = pygame.draw.rect(screen, "lime", (adjust_center_width(style = (self.x, self.w), o = 150) + 170,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 190, 150,50))
        
        font("Từ Chối",(None, None, "OPS"), 35, "black",OPS = (adjust_center_width(style = (self.x, self.w), o = 150) - 170,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 190, 150,50))
        
        font("Chấp nhận", (None, None, "OPS"), 35, "black", OPS = (adjust_center_width(style = (self.x, self.w), o = 150) + 170,
                                         adjust_center_height(style = (self.y, self.h), o = 50) + 190, 150,50))

        pygame.draw.rect(screen, "black", ((adjust_center_width(style=(self.x, self.w))) + 200,
                         adjust_center_height(style=(self.y, self.h)) + 137, 200, 75), border1, border_radius=10)
        
        font("Số Lượng", (None, None), 45, "black",d=(-200,15))
        font(f"{self.n}", (None, None), 45, "black", d= (-10 * len(str(self.n)) + 80,20))

        up = screen.blit(up_arrow_icon, (adjust_center_width(up_arrow_icon, (self.x, self.y, self.w, self.h)) + 400,
                                    adjust_center_height(up_arrow_icon, (self.x, self.y, self.w, self.h)) + 100))
        
        down = screen.blit(down_arrow_icon,(adjust_center_width(down_arrow_icon, (self.x, self.y, self.w, self.h)) + 400,
                                     adjust_center_height(down_arrow_icon, (self.x, self.y, self.w, self.h)) + 160))

        if self.n <= 100000:
            if up.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.n += 1
        
        if self.n > 1:
            if down.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.n -= 1

        if decine.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 1
        
        elif accept.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 2
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return kp, self.n

    def reset(self):
        self.n = 0
    
    def draw_box_4(self, diem, so_luong_lst):
        pos = pygame.mouse.get_pos()

        border_radius = 10
        color_alpha = (0,0,0, 100)
        draw_rect_alpha(color_alpha, (0,0, screen_width, scren_height))

        border_bg = 5
        kp = 0
        pygame.draw.rect(screen, "white",(self.x - border_bg, self.y - border_bg, 
                                          self.w + border_bg * 2, self.h + border_bg * 2), border_radius=border_radius)
        pygame.draw.rect(screen, self.color,(self.x, self.y, self.w, self.h), border_radius=border_radius)

        Exit = screen.blit(x_icon,(self.x - x_icon.get_width() // 2, self.y - x_icon.get_height() // 2))

        if len(str(diem)) > 10:
            Diem_string = str(diem)
            dau = Diem_string[:9]
            cuoi = Diem_string[9:len(Diem_string)]
            font(f"Điểm của bạn: {dau}x10",(None, None, "OPS"), 45,(255,255,98),(self.x, self.y, self.w, self.h), d = (0, -240))
            font(f"{len(cuoi)}",(None, None, "OPS"), 35,(255,255,98),(self.x, self.y, self.w, self.h), d = (10 * len(str(len(cuoi))) + 270, -250))

        else:
            font(f"Điểm của bạn: {diem}", (None, None, "OPS"), 45, (255,255,98),(self.x, self.y, self.w, self.h), d = (0, -240))

        screen.blit(bottle_group_bao_ni_long_icon, (self.x + 100 - 20,self.h - 250))
        screen.blit(bottle_group_bao_giay_icon, (self.x + 250 - 20, self.h - 250))
        screen.blit(bottle_group_ly_nhua_icon, (self.x + 400 - 20, self.h - 250))
        screen.blit(bottle_group_ly_giay_icon, (self.x + 550 - 20, self.h - 250))
        for i in range(4):
            font(f"{so_luong_lst[i]}", (self.x + 140 + (150 * i), self.h - 110), 75, (255,142,0))

        if Exit.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                kp = 1
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        return kp

class Button1:
    def __init__(self):
        self.x = 60
        self.y = 200
        self.w = 225
        self.h = 250
        self.clicked = False
    
    def Box_Nhat_Ky(self, index, time, img):
        action = False
        pos = pygame.mouse.get_pos()

        if self.x == None or self.y == None or self.w == None or self.h == None:
            raise Exception("biến pos bằng giá trị None")
        
        img = pygame.transform.scale(dic2[img], (100,100)).convert_alpha()

        dx = (index - 1) * 325

        pygame.draw.rect(screen, "#242628", (self.x + dx, self.y, self.w, self.h), border_radius=10)

        screen.blit(img, (adjust_center_width(img, (self.x + dx, self.w)),
                          adjust_center_height(img,(self.y, self.h)) - 70))
        
        font(f"{time[0]}-{time[1]}-{time[2]}", (None, None, "OPS"), 35, "white", OPS = (self.x + dx, self.y,self.w,self.h))
        
        x_detail = adjust_center_width(style = (self.x + dx, self.w), o = 150)
        y_detail = adjust_center_height(style = (self.y, self.h), o = 50) + 70
        detail = pygame.draw.rect(screen, "#f2726a", (x_detail, y_detail, 150, 50), 1,border_radius=10)

        font("Chi tiết",(None, None, "OPS"),25, "white",(x_detail,y_detail,150,50))

        if detail.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action