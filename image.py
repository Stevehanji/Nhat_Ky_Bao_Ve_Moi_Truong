import pygame

path = "asset"
lo_lang_icon = pygame.transform.scale(pygame.image.load(f"{path}/lo_lang_icon.png"), (150,150))
wow_icon = pygame.transform.scale(pygame.image.load(f"{path}/wow_icon.png"), (150,150))
happy_icon = pygame.transform.scale(pygame.image.load(f"{path}/happy_icon.png"), (150,150))
vui_tim_icon = pygame.transform.scale(pygame.image.load(f"{path}/vui_tim_icon.png"), (150,150))
trash_icon = pygame.transform.scale(pygame.image.load(f"{path}/trash_icon.png"), (45,45))

# Image
add_icon = pygame.transform.scale2x(pygame.image.load(f"{path}/add_icon.png"))
list_icon = pygame.transform.scale(pygame.image.load(f"{path}/list_icon.png"), (150,150))
back_icon = pygame.transform.scale(pygame.image.load(f"{path}/back_icon.png"), (25,25))

# image Bottle Group
bottle_icon = pygame.transform.scale(pygame.image.load(f"{path}/bottle_icon.png"), (150,150))

bottle_group_ly_giay_icon = pygame.transform.scale(pygame.image.load(f"{path}/ly_giay_icon.png"), (150,150))
bottle_group_ly_nhua_icon = pygame.transform.scale(pygame.image.load(f"{path}/ly_nhua_icon.png"), (150,150))
bottle_group_bao_ni_long_icon = pygame.transform.scale(pygame.image.load(f"{path}/tui_ni_long_icon.png"), (150,150))
bottle_group_bao_giay_icon = pygame.transform.scale(pygame.image.load(f"{path}/tui_giay_icon.png"), (150,150))

# image car group
car_icon = pygame.transform.scale(pygame.image.load(f"{path}/car_icon.png"), (150,150))
car_group_di_bo_icon = pygame.transform.scale(pygame.image.load(f"{path}/walk_icon.png"), (150,150))
car_group_dap_xe_icon = pygame.transform.scale(pygame.image.load(f"{path}/bicycle_icon.png"), (150,150))
car_group_xe_may_icon = pygame.transform.scale(pygame.image.load(f"{path}/car_icon.png"), (150,150))

# image Leaf group
leaf_icon = pygame.transform.scale(pygame.image.load(f"{path}/leaf_icon.png"), (150,150))
leaf_group_nhat_rac_icon = pygame.transform.scale(pygame.image.load(f"{path}/pick_up_garbage_icon.png"), (150,150))
leaf_group_tai_che_icon = pygame.transform.scale(pygame.image.load(f"{path}/recycling_icon.png"), (150,150))
leaf_group_trong_cay_icon = pygame.transform.scale(pygame.image.load(f"{path}/plan_a_tree_icon.png"), (150,150))

tick_icon = pygame.transform.scale(pygame.image.load(f"{path}/tick_icon.png"), (150,150))

# Image page
left_arrow_icon = pygame.transform.scale(pygame.image.load(f"{path}/left_arrow_icon.png"), (25,25))
right_arrow_icon = pygame.transform.scale(pygame.image.load(f"{path}/right_arrow_icon.png"), (25,25))
down_arrow_icon = pygame.transform.scale(pygame.image.load(f"{path}/down_arrow_icon.png"), (45,45))
up_arrow_icon = pygame.transform.scale(pygame.image.load(f"{path}/up_arrow_icon.png"), (45,45))

# Dấu chấm thang
dau_cham_thang_nguy_hiem_icon = pygame.transform.scale(pygame.image.load(f"{path}/dau_cham_thang_icon.png"), (75,75))
dau_cham_thang_xem_them_icon = pygame.transform.scale(pygame.image.load(f"{path}/dau_cham_thang_2_icon.png"), (75,75))
tot_cho_moi_truong_icon = pygame.transform.scale(pygame.image.load(f"{path}/tot_cho_moi_truong_icon.png"), (75,75))

x_icon = pygame.transform.scale(pygame.image.load(f"{path}/x_icon.png"), (75,75))

# Icon window
icon_window = pygame.image.load(f"{path}/bao_ve_moi_truong_icon.ico")