from measure import Measure

if __name__ == '__main__':
    """m1 = Measure(12.5)
    m2 = Measure(100)
    print(m1.inch_cm())
    print(m2.cm_inch())
    
    a1 = Measure(56)
    a2 = Measure(78)
    a3 = Measure(14)
    a4 = Measure(250)
    print(a1.inch_cm())
    print(a2.inch_cm())
    print(a3.cm_inch())
    print(a4.cm_inch())"""
    
    """inch_list = [52,18,20,40]
    for item in inch_list:
        m = Measure(item)
        print(m.inch_cm())"""
        
    num = float(input("Enter Number: "))
    ch = input("Chose I(inch->cm),C(cm->inch):").upper()
    m = Measure(num) 
    if ch == 'I':
        print(m.inch_cm())
    elif ch == 'C':
        print(m.cm_inch())
    else:
        print("Wrong character")