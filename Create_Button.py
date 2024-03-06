from variable import *
from button import *

path = "asset"
                # Menu
# Button
b1 = Button("white", (200, adjust_center_height(style = (100, scren_height)), 200, 200))
b2 = Button("white", (600, adjust_center_height(style = (100, scren_height)), 200, 200))

# Back Button
b3 = Button("white", (30, 80, 50, 50))
b3_1 = Button("white", (30, 230, 50, 50))

        # Add Group
# Button Bottle Group
b4 = Button("white", (100, adjust_center_height(style = (100, scren_height)), 200, 200))

# Túi
b4_1 = Button("white", (100, adjust_center_height(style = (100, scren_height)) - 70, 150, 150))
b4_2 = Button("white", (100, adjust_center_height(style = (100, scren_height)) + 130, 150, 150))

# Ly
b4_3 = Button("white", (600, adjust_center_height(style = (100, scren_height)) - 70, 150, 150))
b4_4 = Button("white", (600, adjust_center_height(style = (100, scren_height)) + 130, 150, 150))

# Button Car Group
b5 = Button("white", (400, adjust_center_height(style = (100, scren_height)), 200, 200))

b5_1 = Button("white", (100, adjust_center_height(style = (100, scren_height)), 200, 200))
b5_2 = Button("white", (400, adjust_center_height(style = (100, scren_height)), 200, 200))
b5_3 = Button("white", (700, adjust_center_height(style = (100, scren_height)), 200, 200))

# Button Leaf Group
b6 = Button("white", (700, adjust_center_height(style = (100, scren_height)), 200, 200))
b6_1 = Button("white", (100, adjust_center_height(style = (100, scren_height)), 200, 200))
b6_2 = Button("white", (400, adjust_center_height(style = (100, scren_height)), 200, 200))
b6_3 = Button("white", (700, adjust_center_height(style = (100, scren_height)), 200, 200))

b7 = Button("gray", (700, scren_height - 100, 200, 50))

edge = 300
BOX = Button("white", (adjust_center_width(style = (edge + 200, screen_width)),
                      adjust_center_height(style=(edge,scren_height)),edge + 200, edge))

BOX2 = Button("white", (adjust_center_width(style = (600, screen_width)),
                      adjust_center_height(style=(500,scren_height)),600, 500))

BOX1 = Button("white", (adjust_center_width(style = (edge + 200, screen_width)),
                      adjust_center_height(style=(edge,scren_height)),edge + 200, edge))

BOX_nhat_ky = Button1()

edge = 600
BOX_nhat_ky_1 = Button("white", (adjust_center_width(style = (edge + 200, screen_width)),
                      adjust_center_height(style=(edge,scren_height)),edge + 200, edge))


black_gray = (36, 38, 40)
edge_button_arrow = 75
left_arrow_button = Button("white", (0 + edge_button_arrow,scren_height - edge_button_arrow * 2, edge_button_arrow, edge_button_arrow))
right_arrow_button = Button("white", (screen_width - edge_button_arrow * 2, 
                                           scren_height - edge_button_arrow * 2, edge_button_arrow,edge_button_arrow))

edge = 550

blue_gd = (51, 68, 153)
Box_Nhat_ky_2 = Button(blue_gd,((adjust_center_width(style = (edge + 200, screen_width)),
                      adjust_center_height(style=(edge,scren_height)),edge + 200, edge)))