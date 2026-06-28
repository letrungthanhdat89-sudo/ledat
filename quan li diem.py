class QuanLyDiem:
    def __init__(self):
        # Lưu trữ dữ liệu dưới dạng danh sách các dict
        self.danh_sach_diem = []

    def _tinh_xep_hang(self, diem):
        """Tự động tính toán xếp hạng dựa trên điểm số"""
        if diem >= 9.0:
            return "Xuất sắc"
        elif diem >= 8.0:
            return "Giỏi"
        elif diem >= 6.5:
            return "Khá"
        elif diem >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

    def nhap_diem(self):
        print("\n--- NHẬP ĐIỂM HỌC SINH ---")
        ma_mon = input("Nhập mã môn học (VD: MATH101): ").strip().upper()
        ho_ten = input("Nhập họ tên học sinh: ").strip()
        
        if not ma_mon or not ho_ten:
            print("❌ Mã môn học và Họ tên không được để trống!")
            return

        # Kiểm tra tính hợp lệ của điểm số
        try:
            diem = float(input("Nhập điểm (0.0 -> 10.0): "))
            if diem < 0 or diem > 10:
                print("❌ Điểm phải nằm trong khoảng từ 0 đến 10!")
                return
        except ValueError:
            print("❌ Điểm nhập vào phải là một số!")
            return

        # Tự động xếp hạng
        xep_hang = self._tinh_xep_hang(diem)

        # Lưu vào danh sách
        hoc_sinh = {
            "ma_mon": ma_mon,
            "ho_ten": ho_ten,
            "diem": diem,
            "xep_hang": xep_hang
        }
        self.danh_sach_diem.append(hoc_sinh)
        print(f"✔️ Đã nhập điểm thành công cho học sinh {ho_ten} (Xếp hạng: {xep_hang})")

    def hien_thi_bang_diem(self):
        print("\n" + "="*68)
        print(f"| {'Mã Môn':<10} | {'Họ và Tên Học Sinh':<25} | {'Điểm':<6} | {'Xếp Hạng':<13} |")
        print("="*68)
        
        if not self.danh_sach_diem:
            print(f"| {'Bảng điểm hiện đang trống.':^64} |")
        else:
            for hs in self.danh_sach_diem:
                print(f"| {hs['ma_mon']:<10} | {hs['ho_ten']:<25} | {hs['diem']:<6.1f} | {hs['xep_hang']:<13} |")
        print("="*68 + "\n")

    def sua_diem(self):
        print("\n--- SỬA ĐIỂM HỌC SINH ---")
        if not self.danh_sach_diem:
            print("❌ Chưa có dữ liệu điểm để sửa.")
            return

        ho_ten = input("Nhập chính xác họ tên học sinh cần sửa điểm: ").strip()
        ma_mon = input("Nhập mã môn học cần sửa điểm: ").strip().upper()

        found = False
        for hs in self.danh_sach_diem:
            if hs['ho_ten'].lower() == ho_ten.lower() and hs['ma_mon'] == ma_mon:
                found = True
                print(f"-> Tìm thấy học sinh {hs['ho_ten']} môn {hs['ma_mon']} với điểm cũ là: {hs['diem']}")
                
                try:
                    diem_moi_str = input("Nhập điểm mới (Bỏ trống & Enter để giữ nguyên): ").strip()
                    if diem_moi_str:
                        diem_moi = float(diem_moi_str)
                        if 0 <= diem_moi <= 10:
                            hs['diem'] = diem_moi
                            hs['xep_hang'] = self._tinh_xep_hang(diem_moi) # Cập nhật lại xếp hạng mới
                            print("✔️ Cập nhật điểm và xếp hạng mới thành công!")
                        else:
                            print("❌ Điểm mới không hợp lệ (phải từ 0 -> 10).")
                except ValueError:
                    print("❌ Điểm phải là một số.")
                break
        
        if not found:
            print("❌ Không tìm thấy học sinh khớp với tên và mã môn học đã nhập.")

    def xoa_diem(self):
        print("\n--- XÓA ĐIỂM HỌC SINH ---")
        ho_ten = input("Nhập họ tên học sinh cần xóa: ").strip()
        ma_mon = input("Nhập mã môn học cần xóa: ").strip().upper()

        for i, hs in enumerate(self.danh_sach_diem):
            if hs['ho_ten'].lower() == ho_ten.lower() and hs['ma_mon'] == ma_mon:
                self.danh_sach_diem.pop(i)
                print(f"✔️ Đã xóa điểm môn {ma_mon} của học sinh {ho_ten}.")
                return
        print("❌ Không tìm thấy dữ liệu phù hợp để xóa.")


# ==========================================
# GIAO DIỆN MENU ĐIỀU KHIỂN
# ==========================================
if __name__ == "__main__":
    ql_diem = QuanLyDiem()

    # Dữ liệu mẫu (Demo)
    ql_diem.danh_sach_diem.append({"ma_mon": "PROG101", "ho_ten": "Nguyễn Văn A", "diem": 8.5, "xep_hang": "Giỏi"})
    ql_diem.danh_sach_diem.append({"ma_mon": "MATH102", "ho_ten": "Trần Thị B", "diem": 4.5, "xep_hang": "Yếu"})

    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ ĐIỂM ---")
        print("1. Xem bảng điểm học sinh")
        print("2. Nhập điểm mới")
        print("3. Sửa điểm học sinh")
        print("4. Xóa điểm học sinh")
        print("5. Thoát")
        
        lua_chon = input("Mời bạn chọn chức năng (1-5): ").strip()
        
        if lua_chon == "1":
            ql_diem.hien_thi_bang_diem()
        elif lua_chon == "2":
            ql_diem.nhap_diem()
        elif lua_chon == "3":
            ql_diem.sua_diem()
        elif lua_chon == "4":
            ql_diem.xoa_diem()
        elif lua_chon == "5":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại.")