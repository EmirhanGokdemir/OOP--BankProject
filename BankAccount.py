# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:15:49 2021

@author: gokdemir
"""

class Bank(object): 
  def __init__(self,money): 
    self.__money = money # public / global --> "private"

  def getMoney(self): #public method 
    return self.__money

  def setMoney(self):  #public method 
    print("Para cekmek için 1'i tuslayın")
    print("Para yatırmak için 2'i tuslayın, parayı lutfen dogru bir sekilde yerleştirin.")  
    tusValue = int(input()) 
    if tusValue == 1: 
      eksi_para = input("Çekmek istediğiniz parayı giriniz: ") #int or float - str
      while (type(eksi_para) != int or float): 
        eksi_para = input("Lütfen numeric bir değer giriniz: ")

      if(eksi_para > self.__money): 
        print("Banka hesabınızdaki para: ", self.__money)
        while (eksi_para <= self.__money): 
          eksi_para = input("Lütfen daha küçük bir değer giriniz: ")

      self.__money -= eksi_para
      print("Teşekkürler çekmek istediğiniz para banka hesbaınızdan eksiltildi. ")
    
    tusValue = int(input())
    if tusValue == 2: 
      para = input("Yatırılmak istenen parayı giriniz: ") #int or float - str
      while (type(para) != int or float): 
        para = input("Lütfen numeric bir değer giriniz: ")
      self.__money += para   
      print("Para yatırma işlemi başarılı teşekkürler") 

    if tusValue != 1 or 2: 
      while tusValue == 1 or 2: 
        tusValue = int(input("Lütfen para çekmek için 1'i yatırmak için 2'yi tuşlayınız. "))




b1 = Bank(1000) #first person
b2 = Bank(2000) # second person 
b3 = Bank(0)

print(b1.getMoney())
print(b1.setMoney())


#b3.money = b1.money = b1.money + b2.money #degisikligi yapan kişi 4. bir kişi.
#print("thırd person money: " , b3.money)