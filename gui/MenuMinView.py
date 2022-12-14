import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from util.ReadDataBase import *

form_class = uic.loadUiType("./resources/simple_menu.ui")[0]
form_class2 = uic.loadUiType("./resources/simple_payment.ui")[0]
class MenuMinView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.readDb =  ReadDB()
        readData = self.readDb.getAllMenu()
        self.simple_payment = self.Simple_payment(self)
        self.vlayout = QVBoxLayout()
        self.hlayout_list = []

        self.image_list = [self.product_image_1,self.product_image_2,self.product_image_3,self.product_image_4,
                           self.product_image_5,self.product_image_6,self.product_image_7,self.product_image_8]

        self.name_list  = [self.product_name_1, self.product_name_2, self.product_name_3, self.product_name_4,
                           self.product_name_5, self.product_name_6, self.product_name_7, self.product_name_8]

        self.price_list = [self.product_price_1, self.product_price_2, self.product_price_3, self.product_price_4,
                           self.product_price_5, self.product_price_6, self.product_price_7, self.product_price_8]
        print(len(readData))

        for index in range(0, len(readData)):
            img_obj = QPixmap(readData[index]['p_img_url'])
            img_obj.scaledToWidth(284)
            img_obj.scaledToHeight(177)
            self.image_list[index].setPixmap(img_obj)
            self.name_list[index].setText(readData[index]['p_name'])
            self.name_list[index].setFont(QtGui.QFont("궁서", 20))

            self.price_list[index].setText(str(readData[index]['p_price']))
            self.price_list[index].setFont(QtGui.QFont("궁서", 20))



    class Simple_payment(QDialog, form_class2):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            QDialog.__init__(self, outer_instance)
            self.setupUi(self)

            img_obj = QPixmap("./resources/etc/card.jpg")
            self.card_image.setPixmap(img_obj)
        def showModal(self):
            return super().exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MenuMinView()
    myWindow.show()
    app.exec_()
