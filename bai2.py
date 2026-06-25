import math
# 1. Logarit cơ số tự nhiên (ln) - Cơ số e
x = 10
ln_x = math.log(x)
print(f"ln({x}) = {ln_x: .4f}")
# 2. Logarit cơ số mười (log10)
log10_x = math.log10(x)
print(f"log10{x} = {log10_x: .4f}")

# 3. Logarit cơ số tuỳ ý
co_so = 2
gia_tri = 8
log_2_8 = math.log(gia_tri, co_so)
print(f"log cơ số {co_so} của {gia_tri} = {log_2_8: .1f}")