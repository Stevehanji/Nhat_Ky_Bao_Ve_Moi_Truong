so_luong = [0 for i in range(4)]

def nhan_xet(lst_S, SL):
    diem = 0

    for i in lst_S:
        if i == 1 or i == 3:
            diem -= 1 * SL[i-1]
            
        if i == 7:
            diem -= 1
            
        if i == 2 or i == 4:
            diem += 1 * SL[i-1]

        if i == 5 or i == 6:
            diem += 1
            
        if i == 8 or i == 9 or i == 10:
            diem += 2

    if diem <= 0:
        return "Oh không, bạn cần phải cố gắng", 1, diem

    if diem >= 1 and diem <= 3:
        return "Cũng ổn, cố gắng phát huy nhe", 2, diem
    
    if diem >= 4 and diem <= 9:
        return "Wow khá đấy, cố gắng phát huy nhe", 3, diem
    
    if diem >= 10:
        return "Xuất sắc, bạn làm rất tốt, cố gắng phát huy", 4, diem