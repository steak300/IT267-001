#lightswitch_oop.py
class LightSwitch():
    def __init__(self) -> None:
        self.switch_status = False
    
    def turnon(self):
        self.switch_status = True

    def turnoff(self):
        self.switch_status = False
    
    def show(self):
        print(f"status = {self.switch_status}")
        
#สร้างวัตถุ (object) จากแม่พิมพ์ (class)
switch_obj = LightSwitch()

#เรียกใช้เมธอด/ฟังก์ชัน
switch_obj.show()
switch_obj.turnon()
switch_obj.show()
switch_obj.turnoff()
switch_obj.show()
switch_obj.turnoff()
switch_obj.show()

