from variable import *
from Create_Button import *
from math import ceil

def Change_color_K(K, color = "lime", change_k = True):
    lst = [b4_1,b4_2,b4_3,b4_4,b5_1,b5_2,b5_3,b6_1,b6_2,b6_3]

    if change_k:
        lst[K-1].change_color(color)
    
    else:
        for i in range(len(lst)):
            lst[i].change_color("white")

def Chinh():
    font("Nhật Ký Bảo Vệ Môi Trường", [None, 50], 75, "black")

    font("Trương Cảnh Chân", (None, scren_height - 70), 30, "black")
    font("Nguyễn Đắc Anh Khoa", (None, scren_height - 40), 30, "black")
    
    if b1.draw(add_icon,("black",10), 10):
        return "Them"

    if b2.draw(list_icon, ("black", 10), 10):
        return "Nhat_Ky"
    
    return "Menu"

def Them():
    global count1, store_tam_thoi, show, show1, count2, BBBB, store, so_luong, diem, is_pass
    new_img = None; new_text = None

    font("Thêm Hoạt Động Của Bạn", [None, 50], 75, "black")

    if b3.draw(back_icon, ("black", 10), 10) and count1 != 0 and show == False and show1 == False:
        count1 = 0
        return "Menu"
        
    if b4.draw(bottle_icon, ("black", 10)) and count1 != 0 and show == False and show1 == False:
        count1 = 0
        return "Add_bottle"

    b4.title_button_right("Đồ nhựa", 50, dpos=(-55,130))
        
    if b5.draw(car_icon, ("black", 10), 10) and count1 != 0 and show == False and show1 == False:
        count1 = 0
        return "Add_car"

    b5.title_button_right("Phương tiện", 50, dpos=(-90,130))
        
    if b6.draw(leaf_icon, ("black", 10), 10) and count1 != 0 and show == False:
        count1 = 0
        return "Add_active"

    b6.title_button_right("Hoạt động", 50, dpos=(-70,130))
    
    count1 += 1

    Accept_Them = len(store_tam_thoi) > 0
    
    if Accept_Them:
        b7.change_color("lime")
    
    else:
        b7.change_color("gray")

    if b7.draw(border=("black", 1), border_raidus=1) and Accept_Them:
        show = True
    
    if show == True:
        result = BOX.draw_box("Chấp nhận Thêm", tick_icon, size=65)

        if result == 1:
            show = False

        elif result == 2:
            store_tam_thoi, BBBB = Chap_Nhan_Them(A = 1)
            Change_color_K(None, change_k=False)
            show = False

            show1 = True
    
    if show1 == True:
        new_text, new_img, so_diem = nhan_xet(BBBB, so_luong)

        new_result = BOX1.draw_box_1(new_text, new_img, 25)

        if new_result and count2 != 0:
            show1 = False
            count2 = 0
            store[-1].append(so_luong)
            store[-1].append(so_diem)

            store[-1].append(new_text)

            time = datetime.datetime.now()
            day = time.day
            minute = time.minute
            hour = time.hour
            year = time.year
            month = time.month
            store[-1].append([year, month, day, hour, minute])
            store[-1].append(new_img)

            so_luong = [0 for i in range(4)]
        
        count2 += 1


    font("Hoàn Thành", [(b7.get_rect()[1] + b7.get_rect()[3] // 2) + 77,600], 40, "black")

    return "Them"

def change_text_and_img(Text, Img, k, Count1 = 0, Show = True):
    global show, text, img, count1, K
    count1 = Count1
    K = k
    img = Img
    show = Show
    text = Text

def Change_and_remove(k):
    global store_tam_thoi
    Change_color_K(k, color = "white")
    store_tam_thoi.remove(k)

def show_box_1(style = 0):
    global K, show, so_luong
    n = None

    y = 110
    dx = 250

    if style == 0:
        Box_result = BOX.draw_box(text, img)
        y = 210
        dx = 200
    
    elif style == 1:
        Box_result, n = BOX2.draw_box_3(text, img)

    good = True
    if K in [1,3,7]:
        good = False
    
    if good == True:
        screen.blit(tot_cho_moi_truong_icon,(adjust_center_width(tot_cho_moi_truong_icon) - dx,
                                             y))
            
    else:
        screen.blit(dau_cham_thang_nguy_hiem_icon,(adjust_center_width(dau_cham_thang_nguy_hiem_icon) - dx,
                                                   y))
        
    if Box_result == 1:
        show = False
        
    if Box_result == 2:
        Chap_Nhan_Them(K)
        Change_color_K(K)
        show = False

        if n != None:
            so_luong[K-1] = n
            BOX2.n = 1

def Add_bottle():
    global count1
    font("Hôm nay bạn đã", [None, 0], 75, "black")
    font("sử dụng đồ bằng gì?", [None, 80], 75, "black")

    # Button back
    if b3.draw(back_icon, ("black", 10), 10):
        return "Them"
    # back_button()
    
    # Call Button
    button_bottle_group_bao_ni_long = b4_1.draw(bottle_group_bao_ni_long_icon ,("black", 10), 10)
    button_bottle_group_bao_giay = b4_2.draw(bottle_group_bao_giay_icon ,("black", 10), 10)
    button_bottle_group_ly_nhua = b4_3.draw(bottle_group_ly_nhua_icon ,("black", 10), 10)
    button_bottle_group_ly_giay_icon = b4_4.draw(bottle_group_ly_giay_icon ,("black", 10), 10)
    count_and_show = (count1 != 0 and show == False)
    
    # Túi ni lông
    if button_bottle_group_bao_ni_long and count_and_show and 1 not in store_tam_thoi:
        change_text_and_img("Túi ni lông", bottle_group_bao_ni_long_icon, 1)
    
    elif button_bottle_group_bao_ni_long and count_and_show and 1 in store_tam_thoi:
        Change_and_remove(1)
    
    b4_1.title_button_right("Túi ni lông", 50, dpos=(120,0))

    # Túi giấy
    if button_bottle_group_bao_giay and count_and_show and 2 not in store_tam_thoi:
        change_text_and_img("Túi giấy", bottle_group_bao_giay_icon, 2)
    
    elif button_bottle_group_bao_giay and count_and_show and 2 in store_tam_thoi:
        Change_and_remove(2)
    
    b4_2.title_button_right("Túi giấy", 50, dpos=(120,0))

    # Ly nhựa
    if button_bottle_group_ly_nhua and count_and_show and 3 not in store_tam_thoi:
        change_text_and_img("ly nhựa", bottle_group_ly_nhua_icon, 3)
    
    elif button_bottle_group_ly_nhua and count_and_show and 3 in store_tam_thoi:
        Change_and_remove(3)
    
    b4_3.title_button_right("Ly nhựa", 50, dpos=(120,0))

    # Ly giấy
    if button_bottle_group_ly_giay_icon and count_and_show and 4 not in store_tam_thoi:
        change_text_and_img("ly giấy", bottle_group_ly_giay_icon, 4)
    
    elif button_bottle_group_ly_giay_icon and count_and_show and 4 in store_tam_thoi:
        Change_and_remove(4)
    
    b4_4.title_button_right("Ly giấy", 50, dpos=(120,0))

    # Show True
    if show == True:
        show_box_1(1)

    count1 += 1

    return "Add_bottle"

def Add_car():
    global count1

    font("Hôm nay bạn đã", [None, 45], 75, "black")
    font("đi phương tiện nào?", [None, 125], 75, "black")

    if b3.draw(back_icon, ("black", 10), 10):
        return "Them"
    
    # Create Button
    button_car_group_di_bo = b5_1.draw(car_group_di_bo_icon, ("black", 10), 10)
    button_car_group_dap_xe = b5_2.draw(car_group_dap_xe_icon, ("black", 10), 10)
    button_car_group_xe_may = b5_3.draw(car_group_xe_may_icon, ("black", 10), 10)
    count_and_show = (count1 != 0 and show == False)
    
    # Đi bộ
    if button_car_group_di_bo and count_and_show and 5 not in store_tam_thoi:
        change_text_and_img("Đi bộ", car_group_di_bo_icon, 5)
    
    elif button_car_group_di_bo and count_and_show and 5 in store_tam_thoi:
        Change_and_remove(5)
    
    b5_1.title_button_right("Đi bộ", 50, dpos=(-20,130))

    # Đạp xe
    if button_car_group_dap_xe and count_and_show and 6 not in store_tam_thoi:
        change_text_and_img("Đạp xe", car_group_dap_xe_icon, 6)
    
    elif button_car_group_dap_xe and count_and_show and 6 in store_tam_thoi:
        Change_and_remove(6)
    
    b5_2.title_button_right("Đạp xe", 50, dpos=(-40,130))

    # Xe máy
    if button_car_group_xe_may and count_and_show and 7 not in store_tam_thoi:
        change_text_and_img("Xe máy", car_group_xe_may_icon, 7)
    
    elif button_car_group_xe_may and count_and_show and 7 in store_tam_thoi:
        Change_and_remove(7)
    
    b5_3.title_button_right("Xe máy", 50, dpos=(-40,130))
    
    # Show
    if show == True:
        show_box_1()

    count1 += 1

    return "Add_car"

def Add_active():
    global count1

    font("Hôm nay bạn đã hành động gì", [None, 45], 75, "black")
    font("để giúp ích cho môi trường?", [None, 125], 75, "black")
    
    if b3_1.draw(back_icon, ("black", 10), 10):
        return "Them"
    
    button_leaf_group_nhat_rac = b6_1.draw(leaf_group_nhat_rac_icon, ("black", 10), 10)
    button_leaf_group_tai_che = b6_2.draw(leaf_group_tai_che_icon, ("black", 10), 10)
    button_leaf_group_trong_cay = b6_3.draw(leaf_group_trong_cay_icon, ("black", 10), 10)

    count_and_show = (count1 != 0 and show == False)

    if button_leaf_group_nhat_rac and count_and_show and 8 not in store_tam_thoi:
        change_text_and_img("Nhặt rác", leaf_group_nhat_rac_icon, 8)
    
    elif button_leaf_group_nhat_rac and count_and_show and 8 in store_tam_thoi:
        Change_and_remove(8)
    
    b6_1.title_button_right("Nhặt rác", 50, dpos=(-65,130))

    if button_leaf_group_tai_che and count_and_show and 9 not in store_tam_thoi:
        change_text_and_img("Tái chế", leaf_group_tai_che_icon, 9)
    
    elif button_leaf_group_tai_che and count_and_show and 9 in store_tam_thoi:
        Change_and_remove(9)
    
    b6_2.title_button_right("Tái chế", 50, dpos=(-50,130))

    if button_leaf_group_trong_cay and count_and_show and 10 not in store_tam_thoi:
        change_text_and_img("Trồng cây", leaf_group_trong_cay_icon, 10)
    
    elif button_leaf_group_trong_cay and count_and_show and 10 in store_tam_thoi:
        Change_and_remove(10)
    
    b6_3.title_button_right("Trồng cây", 50, dpos=(-80,130))

    if show == True:
        show_box_1()

    count1 += 1

    return "Add_active"

def Nhat_Ky():
    global show2, o, img_i, text_result_i, store_i, Index_i, page, count3, lst_time, show3
    n = len(store)

    if n > 3:
        if khoang(page + 1, 2, n-2):
            if left_arrow_button.draw(left_arrow_icon,(black_gray, 5), 10) and count3 != 0 and show2 == False: page -= 1; count3 = 0
        
        if khoang(page + 1, 1, n - 3):
            if right_arrow_button.draw(right_arrow_icon,(black_gray, 5), 10) and count3 != 0 and show2 == False: page += 1; count3 = 0

    font("Nhật Ký Của Bạn", [None, 50], 75, "black")

    if b3.draw(back_icon, ("black", 10), 10):
        page = 0
        return "Menu"
    
    if len(store) == 0:
        font("Không có nhật ký nào", (None, None),75,"black", d = (0, 100))
    
    else:
        if n < 4:
            font(f"{n}", (None, scren_height - 120), 75, "black")
            for i in range(len(store)):
                    if BOX_nhat_ky.Box_Nhat_Ky(i+1, [store[i][-2][2], store[i][-2][1], store[i][-2][0]], store[i][-1]):
                        show2 = True
                        o = store[i]
                        img_i = o[-1]
                        text_result_i = o[-3]
                        store_i = o[:len(store[i]) - 5]
                        Index_i = i
                        lst_time = []

                        for j in range(5):
                            lst_time.append(store[i][-2][j])

                    if show2 == True:
                        lst_i = [img_i, text_result_i, store_i, lst_time]
                        
                        result = BOX_nhat_ky_1.draw_box_2(lst_i)

                        if result == 1:
                            del store[Index_i]
                            show2 = False
                            break

                        elif result == 2:
                            show2 = False
                        
                                                
                        elif result == 3:
                            show3 = True
                            
                        if show3 == True:
                            result1 = Box_Nhat_ky_2.draw_box_4(store[Index_i][-4], store[Index_i][-5])
                            
                            if result1 == 1:
                                show3 = False
            
        else:
            font(f"{page+3}/{n}", (None, scren_height - 120), 75, "black")
            for i in range(3):
                    if BOX_nhat_ky.Box_Nhat_Ky(i+1, [store[i][-2][2], store[i][-2][1], store[i][-2][0]], store[i + page][-1]):
                        show2 = True
                        o = store[i + page]
                        img_i = o[-1]
                        text_result_i = o[-3]
                        store_i = o[:len(store[i + page]) - 5]
                        Index_i = i + page
                        lst_time = []

                        for j in range(5):
                            lst_time.append(store[i][-2][j])

                    if show2 == True:
                        lst_i = [img_i, text_result_i, store_i, lst_time]
                        result = BOX_nhat_ky_1.draw_box_2(lst_i)

                        if result == 1:
                            del store[Index_i]
                            show2 = False
                            page -= 1
                            break

                        elif result == 2:
                            show2 = False
                        
                        elif result == 3:
                            show3 = True
                            
                        if show3 == True:
                            result1 = Box_Nhat_ky_2.draw_box_4(store[Index_i][-4], store[Index_i][-5])
                            
                            if result1 == 1:
                                show3 = False
        
    count3 += 1

    return "Nhat_Ky"