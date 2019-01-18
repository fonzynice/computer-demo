class Computer:

    company = 'Apple Inc'

    def __init__(self):
        self.make = 'Macintosh'
        self.model = 'Macbook Pro'
        self.CPU = 'i7'
        self.RAM = '16GB'
        self.HDD = '1TB'

    def update1(self):
        self.CPU = 'i5'
        return self.CPU

    def update2(self):
        self.RAM = '8GB'
        return self.RAM

    def update3(self):
        self.HDD = '500GB'
        return self.HDD


macbook_pro = Computer()

print(macbook_pro.company,'\n'
      'Macbook Pro 2018 CPU: ',macbook_pro.CPU, '\n',
      '                RAM:' ,macbook_pro.RAM,'\n',
      '                HDD:' ,macbook_pro.HDD, '\n', '\n'
      'Macbook Pro 2016 CPU: ', macbook_pro.update1(), '\n'
      '                 RAM:',   macbook_pro.update2(),'\n'
      '                 HDD:',macbook_pro.update3())


