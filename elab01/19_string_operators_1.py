# 1. Concatenation (การต่อสตริง)
# Operator: +

# print('Safari' + 'World')
# ผลลัพธ์ที่ได้คือ 
"SafariWorld"
# 1

# place = 'Safari' + ' ' + 'World'
# print(place)
# ผลลัพธ์ที่ได้คือ 
"Safari World"
# 1

# 2. Repetition (การคูณสตริง)
# Operator: *

# print("un" * 3)
# ผลลัพธ์ที่ได้คือ 
"ununun"
# 1

# text = 3 * 'str'
# print(text)
# ผลลัพธ์ที่ได้คือ 
"strstrstr"
# 1

# Exercise

# 1. ผลลัพธ์ที่ได้จากคำสั่ง print('12' + '123') คือ 
"12123"
# 1

# 2. ผลลัพธ์ที่ได้จากคำสั่ง print(str(210) + str(320)) คือ 
"210320"
# 1

# 3. ผลลัพธ์ที่ได้จากคำสั่ง print('1234' +
''
# 1
# ) คือ 1234

# 4. ผลลัพธ์ที่ได้จากคำสั่ง print('1234567890' * 3) คือ 
"123456789012345678901234567890"
# 1

# เรื่องผิดบ่อยที่ควรระวัง
# สตริง + ตัวเลข ไม่ได้
# สตริง * สตริง ไม่ได้
# ตัวแปรที่เก็บค่าตัวเลข ถ้าต้องการให้ทำงานแบบสตริง ให้ใช้ str() ช่วย เช่น
# x = 30
# print(x + x) ได้ผลลัพธ์เป็น 
"60"
# 1

# print(str(x) + str(x)) ได้ผลลัพธ์เป็น 
"3030"
# 1
# เครื่องหมายเปิดหรือปิดสตริงไม่ครบ
# เก็บ quote แบบเดียวกับที่ใช้เป็นสตริง โดยไม่ใส่ \ เช่น
# s = "You shouted "Yeah!" very loudly after last examination"
