cau_thu =[
    {"Ma":"CT007","Ten":"Nguyen Quang Hai","So_tran":10, "ban_thang":"5","kien_tao":"4","hieu_suat":"Tu dong tinh", "loai":"tu dong danh gia"}

]

def tu_dong(so_tran_thi_dau ,so_ban_thang ,so_kien_tao):
    return ((so_tran_thi_dau*1)+(so_ban_thang *3)+(so_kien_tao*2))


def xep_loai(hieu_suat):
    if hieu_suat <15:
        return("Cần thanh lý/Cho mượn")
    elif hieu_suat <30 :
        return("Dự bị chiến lược")
    elif hieu_suat <50 :
        return("Trụ cột đội bóng")
    else :
       return("Ngôi sao đẳng cấp")

def hien_thi_danh_sach_cau_thu ():
    if len(cau_thu) ==" ":
        print("Danh sách rỗng!")
        return
     
    for thong_tin in cau_thu:
        print("Thông tin cầu thủ:")

        print(thong_tin)
    

def tiep_nhan_cau_thu_moi ():
    ma =input("Nhập mã cầu thủ :").upper()
    for thong_tin in cau_thu :
        if thong_tin["Ma"]== ma :
            print("Mã cầu thủ bị trùng!")
            return 
    
    ten = input("Nhập tên cầu thủ :")
    so_tran =int (input("Nhập số trận :"))
    ban_thang = int (input("Nhập số bàn thắng :"))
    kien_tao = int(input("Số kiến tạo:"))

    hieu_suat =tu_dong(so_tran,ban_thang,kien_tao)
    loai = xep_loai(hieu_suat)

    thong_tin  = {
        "Mã CV" : ma,
        "Tên" :ten,
        "Số trận": so_tran,
        "Bàn thắng ":ban_thang,
        "Kiến tạo":kien_tao,
        "Hiệu suất":hieu_suat,
        "Xếp loại":loai
        
    }
    cau_thu.append(thong_tin)
    print("Đã thêm cầu thủ thành công!")

def cap_nhap_thong_tin_va_chi_so ():
    ma =input("Nhập mã muốn sửa:").upper()
    for thong_tin in cau_thu:
        if thong_tin["Ma"] == ma:
            thong_tin["Số trận"] = int(input("Nhập số trận mới:"))
            thong_tin["Số bàn thắng"] =int(input("Nhập số bàn thắng mới:"))
            thong_tin["Số kiến tạo mới"]= int(input("Nhâp số kiến tạo mới:"))

            thong_tin["Hiệu suất"] = tu_dong(thong_tin["Số trận"],thong_tin["Số bàn thắng"],thong_tin["Số kiến ta"])
            thong_tin["Xếp loạt"] = xep_loai(thong_tin["Hiệu xuất"])

            print("Cập nhập thành công!")
            return
            
    print("Không tìm thấy mã cầu thủ!")


def xoa_cau_thu():
    ma = input("Nhập mã cầu thủ cần xóa: ")

    for thong_tin in cau_thu:
        if thong_tin["Ma"] == ma:
           print("hello")
           hoi = input("Bạn có chắc chắn muốn xóa cầu thủ này khỏi danh sách không?(Y/N):")
           if hoi =="N" or hoi =="n":
               print("Không xóa cầu thủ!")
           else :
              cau_thu.remove(thong_tin)
              print("Đã xóa thành công!")
              return

    print("Không tìm thấy!")
    
def tim_kiem_cau_thu ():
    key = input("Nhập mã hoặc tên: ")

    found = False
    for thong_tin in cau_thu:
        if key in thong_tin["ma"] or key in thong_tin["ten"]:
            print(thong_tin)
            found = True

    if not found:
        print("Không tìm thấy!")


           
        


        

while True :
    print ("""
           1.Hiển thị danh sách cầu thủ
           2.Tiếp nhận cầu thủ mới
           3. Cập nhập thông tin và chỉ số 
           4. Xóa cầu thủ 
           5.Tìm kiếm cầu thủ
           6.Thống kê phân loại phong độ
           7.Đánh giá phong độ tự động 
           8. Thoạt chương trình 
        """ )
    choise =int (input("Mời bạn nhập lựa chọn:"))
    
    match choise :
        case 1:
            hien_thi_danh_sach_cau_thu ()
        
        case 2:
            tiep_nhan_cau_thu_moi ()
        
        case 3:
            cap_nhap_thong_tin_va_chi_so ()

        case 4:
            xoa_cau_thu()

        case 5:
            tim_kiem_cau_thu ()

        case 8:
            print("Thoát chương trình!")
            break
        case _:
            print("Vui lòng nhập lại!")
        
       
