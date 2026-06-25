import math

def giai_phuong_trinh_bac_hai(a, b, c):
    print(f"\n Giải Phương Trình: {a}x^2 + {b}x + {c} = 0 ")

    #kiểm tra điều kiện a phải khác 0
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            x = -c / b
            print(f"Phương trình bậc nhất có 1 nghiệm: x = {x: .2f}")
        return
    # Tính Delta
    delta = b**2 - 4*a*c
    print(f"--> Delta = {delta}")

    # Biện luận nghiệm theo Delta
    if delta < 0:
        print("--> Phương trình vô nghiệm (trên tập số thực).")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"--> Phương trình có nghiệm kép: x = {x:.2f}")
    else:
        
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2  * a)
        print(f"--> Phương trình có 2 nghiệm phân biệt:")
        print(f" x1 = {x1: .2f}")
        print(f"x2 = {x2: .2f}")

        giai_phuong_trinh_bac_hai(1, -5, 6)

        giai_phuong_trinh_bac_hai(1, -4, 4)

        giai_phuong_trinh_bac_hai(1, 1, 1)