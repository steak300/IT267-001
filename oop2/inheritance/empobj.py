from empit import EmpIT
from empmkt import EmpMKT

#create object employee IT
mike = EmpIT("001","Mike",60000)
mike.add_skill("Python, JavaSrcipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#create object employee MKT
anna = EmpMKT("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

Paul = EmpMKT("003","Paul",45000)
Paul.add_commission(35)
Paul.add_location = 'Chiang Mai'
Paul.emp_detail()
Paul.mkt_salary()


