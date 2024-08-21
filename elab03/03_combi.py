def fac(n,r):
    result = 1
    for x in range(n-r+1,n+1):
        result = x*result
    return result

# จงเขียนฟังก์ชัน combi(n,r) เพื่อคำนวณหาจำนวนวิีธีการจัดหมู่ของ n สิ่งโดยเลือกมา r สิ่ง
def combi(n,r):
    """Compute number of all combination from n choose r."""
    return fac(n, n) / (fac(n-r, n-r) * fac(r, r))

# 3.4 เขียนนิพจน์เพื่อหาค่าเฉลี่ยจำนวนวิธีเลือกชุด(ให้ใช้ฟังก์ชัน combi)
ans = (combi(4,3) + combi(7,3) + combi(3,3) + combi(7,3) + combi(10,3)) / 5
