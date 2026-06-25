import math
giatri = 0.5

#Tính hàm ngược
asin_rad = math.asin(giatri) # trả về radian
acos_rad = math.acos(giatri)

# Chuyển kết quả từ Radian về độ dễ đọc
asin_deg = math.degrees(asin_rad)
acos_deg = math.degrees(acos_rad)

print(f"Góc có sin = {giatri} là: {asin_deg: .1f}° (hoặc{asin_rad: .4f} rad)")
print(f"Góc có cos: {giatri} là: {acos_deg: .1f}° (hoặc {acos_rad: .4f} rad)")