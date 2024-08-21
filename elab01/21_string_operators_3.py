# 1. Slicing
# Operator: [:]

# subject = 'Fundamental Programming Concept'
# text = subject[12:23]
# print(text)
# print(subject)
# ผลลัพธ์ที่ได้คือ
"Programming"
# 1
"Fundamental Programming Concept"
# 1

# subject = 'Fundamental Programming Concept'
# text = subject[-19:-8]
# print(text)
# print(subject)
# ผลลัพธ์ที่ได้คือ
"Programming"
# 1
"Fundamental Programming Concept"
# 1

# 2. Slicing with Step
# Operator: [::]

# [start:stop:step]
# subject = "Fundamental Programming Concept"
# print(1, subject[12:23])
# print(2, subject[12:23:1])
# print(3, subject[12:23:2])
# ผลลัพธ์ที่ได้คือ
"1 Programming"
# 1
"2 Programming"
# 1
"3 Pormig"
# 1

# subject = "Fundamental Programming Concept"
# print(1, subject[-19:-8])
# print(2, subject[-19:-8:1])
# print(3, subject[-19:-8:2])
# ผลลัพธ์ที่ได้คือ
"1 Programming"
# 1
"2 Programming"
# 1
"3 Pormig"
# 1

# 3. Slicing with Negative Step
# subject = "Fundamental Programming Concept"
# print(1, subject[12:23])
# print(2, subject[12:23:-1])
# print(3, subject[12:23:-2])
# ผลลัพธ์ที่ได้คือ
"1 Programming"
# 1
"2" 
# 1
"3" 
# 1

# subject = "Fundamental Programming Concept"
# print(1, subject[22:11])
# print(2, subject[22:11:-1])
# print(3, subject[22:11:-2])
# ผลลัพธ์ที่ได้คือ
"1" 
# 1
"2 gnimmargorP"
# 1
"3 gimroP"
# 1

# 4. start, stop, step can be omitted
# subject = "Fundamental Programming Concept"
# print(1, subject[:23:])
# print(2, subject[:23:2])
# print(3, subject[22::-1])
# ผลลัพธ์ที่ได้คือ
"1 Fundamental Programming"
# 1
"2 FnaetlPormig"
# 1
"3 gnimmargorP latnemadnuF"
# 1

# เรื่องผิดบ่อยที่ควรระวัง
# กำหนด step ของการ slice ผิด ทำให้ได้สตริงว่าง
# กำหนดค่า start และ stop ของการ slice ผิด ทำให้ได้ค่าสตริงคลาดเคลื่อนไป
# ผลลัพธ์จากการ slice จะไม่เปลี่ยนค่าของสตริงต้นฉบับ
