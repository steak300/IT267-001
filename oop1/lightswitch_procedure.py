#สร้างฟังก์ชันเปิดไฟ
def turnon():
    global switch_status
    switch_status = True #เปลี่ยนสถานะเป็นเปิดไฟ

#สร้างฟังก์ชันปิดไฟ
def turnoff():
    global switch_status
    switch_status = False

switch_status = False #ปิด

print(f"Status = {switch_status}")#False
turnon()
print(f"Status = {switch_status}")#True
turnoff()
print(f"Status = {switch_status}")
turnoff()
print(f"Status = {switch_status}")

