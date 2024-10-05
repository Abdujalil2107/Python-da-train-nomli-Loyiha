import time

class Train():
    
    def __init__(self,name,max_speed:int,color,country):
        
        self.name = name
        self.max_speed = max_speed
        self.color = color
        self.country = country
        self.speed = 0
        self.count = 0
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def info(self):
        
        print()
        print("Ma'lumot !!!")
        print("------------")
        
        text = str(f"{self.country}(da) yasalgan Po'yezd nomi '{self.name}' {self.color} rangda maksimal tezligi {self.max_speed}km/soat")
        text_len = list(text)
        
        print(f"{self.country}(da) yasalgan Po'yezd nomi '{self.name}' {self.color} rangda maksimal tezligi {self.max_speed}km/soat",end="")
        
        if self.speed == 0:
            
            test = " va u 0km/soat tezlik bilan to'xtab turibdi."
            test = list(test)
            
            for i in test:
                text_len.append(i)
                
            print(" va u 0km/soat tezlik bilan to'xtab turibdi.")
            
        elif self.speed == 1:
            
            test = " va u 0km/soat tezlik bilan harakatlanish uchun tayyor."
            test = list(test)
            
            for i in test:
                text_len.append(i)
                
            print(" va u 0km/soat tezlik bilan harakatlanish uchun tayyor.")
            
        else:
            
            test = str(f" va u {self.speed}km/soat tezlik bilan harakatlanmoqda...")
            test = list(test)
            
            for i in test:
                text_len.append(i)
                
            print(f" va u {self.speed}km/soat tezlik bilan harakatlanmoqda...")
            
        for i in text_len:
            print("-",end="")
            
        print()
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
    def start(self):
        
        if self.speed > 0:
            print("Po'yezd harakatlanmoqda...")
            
        else:
            
            print("Po'yezd yurish uchun tayyor, 2-chi bo'lim orqali tezlik qo'shing.")
            self.speed += 1
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
    def stop(self):
        
        if self.speed == 0:
            print("Po'yezd hali joyidan qo'zg'almagan !!!")
            
        else:
            
            print("Po'yezd to'xtatilmoqda...")
            time.sleep(3)
            
            self.speed = 0
            self.count = 0
            
            print("Tabriklayman Po'yezd muvoffaqyatli to'xtatildi.")
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
    def speed_up(self):
        
        if self.speed == 0:
            print("Po'yezd hali yurish uchun tayyor emas !!!")
            
        else:
            
            if self.speed == self.max_speed:
                print("Kechirasiz siz maksimal tezlikda harakatlanmoqdasiz tezlik qo'sha olmaysiz !!!")
                
            else:
                
                try:
                    
                    self.count += 1
                    speed_add = int(input(f"Eslatma maksimal tezlik {self.max_speed}km/soat !!!\nTezlik qo'shishingiz mumkun... "))
                    
                    if self.count == 1:
                        speed_add -= 1
                        
                    test = (self.speed) + speed_add
                    
                    if test > self.max_speed:
                        print(f"Siz buncha tezlik qo'sha olmaysiz maksimal tezlik '{self.max_speed}km/soat'")
                        
                    else:
                        
                        print("Tezlik qo'shilmoqda...")
                        time.sleep(3)
                        
                        self.speed += speed_add
                        print(f"Siz {self.speed}km/soat tezlikda harakatlanmoqdasiz...")
                        
                except ValueError:
                    print("\nILTIMOS FAQAT RAQAM KIRITING !!!")
                    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
  
    def speed_down(self):
        
        if self.speed == 0:
            print("Po'yezd hali joyidan qo'zg'almagan !!!")
            
        elif self.speed == 1:
            print("Po'yezdga tezlik qo'shilmagan lekin u harakatlanish uchun tayyor.")
            
        else:
            
            try:
                
                speed_minus = int(input("Qancha kamaytirmoqchisiz... "))
                test = self.speed - speed_minus
                
                if test < 0:
                    print(f"Kechirasiz siz {self.speed}km/soat tezlikda harakatlanmoqdasiz.")
                    
                elif test == 0:
                    
                    self.speed = 0
                    self.count = 0
                    print("Tabriklayman Po'yezd muvoffaqyatli to'xtatildi.")
                    
                else:
                    
                    print("Tezlik kamaytirilmoqda...")
                    time.sleep(3)
                    
                    self.speed -= speed_minus
                    print(f"Siz {self.speed}km/soat tezlikda harakatlanmoqdasiz...")
                    
            except ValueError:
                print("\nILTIMOS FAQAT RAQAM KIRITING !!!")
                
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                

name = input("Po'yezd nomi... ")
color = input("Po'yezd rangi... ")
country = input("Qaysi mamlakatda ishlab chiqarilganligi... ")

try:

    max_speed = int(input("Maksimal Tezligi... "))

    train = Train(name,max_speed,color,country)
    train.info()


    test = 0

    while (test != 21):
        
        print()
        print("Bo'limlar:")
        print("----------")
        print("1. Po'yezd haqida ma'lumot.")
        print("---------------------------")
        print("2. Po'yezdni yurgazish.")
        print("-----------------------")
        print("3. Po'yezdni to'xtatish.")
        print("------------------------")
        print("4. Po'yezdga tezlik qo'shish.")
        print("-----------------------------")
        print("5. Po'yezdni tezligini kamaytirish.")
        print("-----------------------------------")
        
        for_case = int(input("Bo'lim raqamini kiriting... "))
        print()
        
        match(for_case):
            
            case 1: train.info(); test = 0
            case 2: train.start(); test = 1
            case 3: train.stop(); test = 0
            case 4: train.speed_up(); test = 0
            case 5: train.speed_down(); test = 0
            case _ : test = int(input("Bizda yo'q bo'lim raqamini kiritdingiz davom ettirish uchun istalgan raqamni to'xtatish uchun (21)ni kiriting... "))
        
        if test == 0:
            test = int(input("Davom ettirish uchun istalgan raqamni to'xtatish uchun (21)ni kiriting... "))
            
except ValueError:
    print("\nILTIMOS FAQAT RAQAM KIRITING !!!\n")