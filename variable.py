# Khởi Tạo Mô Đun
import pygame
import datetime
from image import *
import json
from data_analysis import *

# Variable Screen and Caption
screen_width = 1000
scren_height = 700
screen = pygame.display.set_mode((screen_width, scren_height))
pygame.display.set_caption("Nhật Ký Bảo Vệ Môi Trường")
pygame.display.set_icon(icon_window)
count1 = 0
count2 = 0
count3 = 0
timer = 100

# Function

    # Adjust
def adjust_center(img = None, style = (None, None, screen_width, scren_height)):
    if img != None:
        if style[0] == None or style[1] == None:
            return (style[2] // 2 - img.get_width() // 2, 
                    style[3] // 2 - img.get_height() // 2)
        
        if style[0] != None and style[1] != None:
            return (style[0] + style[2] // 2 - img.get_width() // 2, 
                    style[1] + style[3] // 2 - img.get_height() // 2)
    
    if img == None:
        return (style[2] // 2 - style[0] // 2, style[3] // 2 - style[1] // 2)
    
def adjust_center_width(img = None, style = (None, screen_width), o = None):
    """
        style[0] : x
        style[1] : width
    """
    if img != None:
        if style[0] == None:
            return style[1] // 2 - img.get_width() // 2
        
        if style[0] != None:
            return style[0] + style[1] // 2 - img.get_width() // 2
    
    if img == None:
        if o == None:
            return style[1] // 2 - style[0] // 2
        
        if o != None:
            return style[0] + style[1] // 2 - o // 2
    
def adjust_center_height(img = None, style = (None, scren_height), o = None):
    """
        style[0] : x
        style[1] : width
    """
    if img != None:
        if style[0] == None:
            return style[1] // 2 - img.get_height() // 2
        
        if style[0] != None:
            return style[0] + style[1] // 2 - img.get_height() // 2
    
    if img == None:
        if o == None:
            return style[1] // 2 - style[0] // 2
    
        if o != None:
            return style[0] + style[1] // 2 - o // 2

# Font
def font(text, pos, size, color, OPS = None, d = (0,0)):
    f1 = pygame.font.Font("asset/UVNThanhPhoNang.TTF", size)
    f1 = f1.render(text, False, color)

    x = pos[0]
    y = pos[1]

    if x == None:
        x = ((screen_width // 2) - (f1.get_width() // 2)) + d[0]

    if y == None:
        y = ((scren_height // 2) - (f1.get_height() // 2)) + d[1]
    
    try:
        if pos[2] == "OPS":
            x = adjust_center_width(f1, (OPS[0], OPS[2])) + d[0]
            y = adjust_center_height(f1, (OPS[1],OPS[3])) + d[1]
    
    except:
        pass

    screen.blit(f1, (x,y))    

# Color
cyan = (51, 204, 204)
show = False
show1 = False
show2 = False
show3 = False

text = ""
img = None
store_tam_thoi = []
K = 0
done_store = []
BBBB = store_tam_thoi.copy()

def Chap_Nhan_Them(kind = None, A = 0):
    global store_tam_thoi, BBBB
    """
        1 : Túi ni lông
        2 : Túi Giấy
        3 : Ly nhựa
        4 : Ly giấy

        5 : Đi bộ
        6 : Đi xe đạp
        7 : Đi xe máy

        8 : Nhặt rác
        9 : Tái chế
        10 : Trồng cây

        [1,3,7]
    """
    if A == 0:
        if kind not in store_tam_thoi:
            store_tam_thoi.append(kind)
    
    elif A == 1:
        store.append(store_tam_thoi)

        BBBB = store_tam_thoi.copy()
        store_tam_thoi = []

        return store_tam_thoi, BBBB

def draw_rect_alpha(color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    screen.blit(shape_surf, rect)

def khoang(n, start, end):
    if start <= n and n <= end:
        return True
    
    return False

dic = {
    1 : bottle_group_bao_ni_long_icon,
    2 : bottle_group_bao_giay_icon,
    3 : bottle_group_ly_nhua_icon,
    4 : bottle_group_ly_giay_icon,
    5 : car_group_di_bo_icon,
    6 : car_group_dap_xe_icon,
    7 : car_group_xe_may_icon,
    8 : leaf_group_nhat_rac_icon,
    9 : leaf_group_tai_che_icon,
    10 : leaf_group_trong_cay_icon
}

dic2 = {
    1 : lo_lang_icon,
    2 : wow_icon,
    3 : happy_icon,
    4 : vui_tim_icon,
}

r1 = [270, 370, 470, 570]
r2 = [270, 370, 470]
r3 = [270, 370, 470]

new_r1 = []
new_r2 = []
new_r3 = []


def copy_r():
    global new_r1, new_r2, new_r3

    new_r1 = r1.copy()
    new_r2 = r2.copy()
    new_r3 = r3.copy()

copy_r()

def add_image_khung(row = None, khung_x = None, khung_y = None, row1 = None, row2 = None, row3 = None):
    global new_r1, new_r2, new_r3

    done = False

    if done == False:
        y = 0
        x = 0
        for i in range(len(row)):
            img_width = 100
            img_height = 100

            if khoang(row[i], 1,4):
                y = khung_y

                if i == 0:
                    y = khung_y + 10
                    img_width = 75
                    img_height = 75
                
                x = new_r1[0]
                del new_r1[0]

            if khoang(row[i], 5,7):
                x = 0

                if len(row1) == 0:
                    y = khung_y
                
                else:
                    y = khung_y + 100

                if row[i] == 5:
                    y += 10
                    img_width = 75
                    img_height = 75
                
                x = new_r2[0]
                del new_r2[0]

            if khoang(row[i], 8, 10):
                if len(row1) == 0 and len(row2) == 0:
                    y = khung_y
                
                elif len(row2) == 0 and len(row1) != 0:
                    y = khung_y + 100

                else:
                    y = khung_y + 200

                x = 0

                if row[i] == 9 or row[i] == 10:
                    y += 10
                    img_width = 75
                    img_height = 75
                
                x = new_r3[0]
                del new_r3[0]
            
            Img = pygame.transform.scale(dic[row[i]], (img_width, img_height))
            screen.blit(Img,(x,y))
    
    copy_r()

o = None
img_i = None
text_result_i = None
store_i = None
Index_i = 0
page = 0
page_lim = 1
lst_time = []

def load_file():
    f = open("asset/data.json", mode = "r")
    data_json = json.load(f)

    n = len(data_json)

    F = []

    if n == 0:
        return F
    
    else:
        for i in range(1, n+1):
            F.append(data_json[f"n{i}"])
        
    return F

store = load_file()

def save_file(data):
    kp = {}
    for i in range(1, len(data) + 1):
        kp[f"n{i}"] = store[i-1]
        
    with open("asset/data.json","w", encoding="utf-8") as da:
        json.dump(kp, da,indent=4)