# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import pandas as pd
import ClientRest

class QModel(QtCore.QAbstractTableModel):

  def __init__(self, data):
    QtCore.QAbstractTableModel.__init__(self)
    self._data = data

  def rowCount(self, parent=None):
    return self._data.shape[0]

  def columnCount(self, parent=None):
    return self._data.shape[1]

  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
    return None

  def headerData(self, col, orientation, role):
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
        return self._data.columns[col]
    return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 160, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BtPgProduct = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BtPgProduct.setMinimumSize(QtCore.QSize(100, 100))
        self.BtPgProduct.setObjectName("BtPgProduct")
        self.verticalLayout.addWidget(self.BtPgProduct)
        self.BtPgSale = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BtPgSale.setMinimumSize(QtCore.QSize(100, 100))
        self.BtPgSale.setObjectName("BtPgSale")
        self.verticalLayout.addWidget(self.BtPgSale)
        self.BtPgCompras = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BtPgCompras.setMinimumSize(QtCore.QSize(100, 100))
        self.BtPgCompras.setObjectName("BtPgCompras")
        self.verticalLayout.addWidget(self.BtPgCompras)
        self.BtPgStok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BtPgStok.setMinimumSize(QtCore.QSize(100, 100))
        self.BtPgStok.setObjectName("BtPgStok")
        self.verticalLayout.addWidget(self.BtPgStok)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(160, 40, 701, 541))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Stock = QtWidgets.QWidget()
        self.Stock.setObjectName("Stock")
        self.edStockSearch = QtWidgets.QLineEdit(self.Stock)
        self.edStockSearch.setGeometry(QtCore.QRect(150, 70, 231, 20))
        self.edStockSearch.setObjectName("edStockSearch")
        self.btStockSearch = QtWidgets.QPushButton(self.Stock)
        self.btStockSearch.setGeometry(QtCore.QRect(390, 70, 75, 23))
        self.btStockSearch.setObjectName("btStockSearch")
        self.tbStock = QtWidgets.QTableView(self.Stock)
        self.tbStock.setGeometry(QtCore.QRect(10, 140, 691, 381))
        self.tbStock.setObjectName("tbStock")
        self.stackedWidget.addWidget(self.Stock)
        self.Compra = QtWidgets.QWidget()
        self.Compra.setObjectName("Compra")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Compra)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 90, 671, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_7.addWidget(self.doubleSpinBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_8.addWidget(self.comboBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.verticalLayout_9.addWidget(self.doubleSpinBox_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.tableView_3 = QtWidgets.QTableView(self.Compra)
        self.tableView_3.setGeometry(QtCore.QRect(20, 160, 671, 331))
        self.tableView_3.setObjectName("tableView_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.Compra)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 510, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.Compra)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 50, 251, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_11 = QtWidgets.QLabel(self.Compra)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.Compra)
        self.Venda = QtWidgets.QWidget()
        self.Venda.setObjectName("Venda")
        self.lcdSaleTotal = QtWidgets.QLCDNumber(self.Venda)
        self.lcdSaleTotal.setGeometry(QtCore.QRect(570, 20, 131, 41))
        self.lcdSaleTotal.setObjectName("lcdSaleTotal")
        self.TbSale = QtWidgets.QTableView(self.Venda)
        self.TbSale.setGeometry(QtCore.QRect(20, 190, 671, 311))
        self.TbSale.setObjectName("TbSale")
        self.formLayoutWidget = QtWidgets.QWidget(self.Venda)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.edSaleCliente = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edSaleCliente.setObjectName("edSaleCliente")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.edSaleCliente)
        self.edSaleBarcode = QtWidgets.QLineEdit(self.Venda)
        self.edSaleBarcode.setGeometry(QtCore.QRect(20, 90, 251, 20))
        self.edSaleBarcode.setObjectName("edSaleBarcode")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Venda)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 671, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.edSaleProduct = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edSaleProduct.setObjectName("edSaleProduct")
        self.verticalLayout_2.addWidget(self.edSaleProduct)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.edSalveQTD = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.edSalveQTD.setObjectName("edSalveQTD")
        self.verticalLayout_3.addWidget(self.edSalveQTD)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.cbSaleUnit = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cbSaleUnit.setObjectName("cbSaleUnit")
        self.verticalLayout_5.addWidget(self.cbSaleUnit)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.edSalePrice = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.edSalePrice.setObjectName("edSalePrice")
        self.verticalLayout_4.addWidget(self.edSalePrice)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.btSaleAddItem = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btSaleAddItem.setObjectName("btSaleAddItem")
        self.horizontalLayout.addWidget(self.btSaleAddItem)
        self.label_5 = QtWidgets.QLabel(self.Venda)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.btSalveSave = QtWidgets.QPushButton(self.Venda)
        self.btSalveSave.setGeometry(QtCore.QRect(610, 510, 75, 23))
        self.btSalveSave.setObjectName("btSalveSave")
        self.stackedWidget.addWidget(self.Venda)
        self.Produtos = QtWidgets.QWidget()
        self.Produtos.setObjectName("Produtos")
        self.TabProduList = QtWidgets.QTabWidget(self.Produtos)
        self.TabProduList.setGeometry(QtCore.QRect(0, 0, 701, 571))
        self.TabProduList.setObjectName("TabProduList")
        self.tabProdutosList = QtWidgets.QWidget()
        self.tabProdutosList.setObjectName("tabProdutosList")
        self.tbProd = QtWidgets.QTableView(self.tabProdutosList)
        self.tbProd.setGeometry(QtCore.QRect(0, 120, 701, 431))
        self.tbProd.setShowGrid(False)
        self.tbProd.setSelectionBehavior( QtWidgets.QAbstractItemView.SelectRows)
        self.tbProd.setObjectName("tbProd")
        self.edProdSearch = QtWidgets.QLineEdit(self.tabProdutosList)
        self.edProdSearch.setGeometry(QtCore.QRect(160, 40, 231, 20))
        self.edProdSearch.setObjectName("edProdSearch")
        self.btProdSearch = QtWidgets.QPushButton(self.tabProdutosList)
        self.btProdSearch.setGeometry(QtCore.QRect(400, 40, 75, 23))
        self.btProdSearch.setObjectName("btProdSearch")
        self.TabProduList.addTab(self.tabProdutosList, "")
        self.TabProdcCad = QtWidgets.QWidget()
        self.TabProdcCad.setObjectName("TabProdcCad")
        self.TabProduList.addTab(self.TabProdcCad, "")
        self.stackedWidget.addWidget(self.Produtos)
        self.lbPgActual = QtWidgets.QLabel(self.centralwidget)
        self.lbPgActual.setGeometry(QtCore.QRect(186, 10, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbPgActual.setFont(font)
        self.lbPgActual.setTextFormat(QtCore.Qt.PlainText)
        self.lbPgActual.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPgActual.setObjectName("lbPgActual")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.TabProduList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.BtPgProduct, self.BtPgSale)
        MainWindow.setTabOrder(self.BtPgSale, self.BtPgCompras)
        MainWindow.setTabOrder(self.BtPgCompras, self.BtPgStok)
        MainWindow.setTabOrder(self.BtPgStok, self.TabProduList)
        MainWindow.setTabOrder(self.TabProduList, self.edProdSearch)
        MainWindow.setTabOrder(self.edProdSearch, self.btProdSearch)
        MainWindow.setTabOrder(self.btProdSearch, self.tbProd)
        MainWindow.setTabOrder(self.tbProd, self.edSaleCliente)
        MainWindow.setTabOrder(self.edSaleCliente, self.edSaleBarcode)
        MainWindow.setTabOrder(self.edSaleBarcode, self.edSaleProduct)
        MainWindow.setTabOrder(self.edSaleProduct, self.edSalveQTD)
        MainWindow.setTabOrder(self.edSalveQTD, self.cbSaleUnit)
        MainWindow.setTabOrder(self.cbSaleUnit, self.edSalePrice)
        MainWindow.setTabOrder(self.edSalePrice, self.btSaleAddItem)
        MainWindow.setTabOrder(self.btSaleAddItem, self.TbSale)
        MainWindow.setTabOrder(self.TbSale, self.btSalveSave)
        MainWindow.setTabOrder(self.btSalveSave, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.doubleSpinBox_3)
        MainWindow.setTabOrder(self.doubleSpinBox_3, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.doubleSpinBox_4)
        MainWindow.setTabOrder(self.doubleSpinBox_4, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.tableView_3)
        MainWindow.setTabOrder(self.tableView_3, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.edStockSearch)
        MainWindow.setTabOrder(self.edStockSearch, self.btStockSearch)
        MainWindow.setTabOrder(self.btStockSearch, self.tbStock)


        self.products = ClientRest.Produtos()
        ## acions
        self.BtPgProduct.clicked.connect(lambda: self.changeModule(3))
        self.BtPgSale.clicked.connect(lambda: self.changeModule(2))
        self.BtPgCompras.clicked.connect(lambda: self.changeModule(1))
        self.BtPgStok.clicked.connect(lambda: self.changeModule(0))
        self.stackedWidget.currentChanged.connect(self.changeTitle)
        self.edProdSearch.textChanged.connect(self.SearchProduct)

        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BtPgProduct.setText(_translate("MainWindow", "Produtos"))
        self.BtPgSale.setText(_translate("MainWindow", "Vendas"))
        self.BtPgCompras.setText(_translate("MainWindow", "Compras"))
        self.BtPgStok.setText(_translate("MainWindow", "Estoque"))
        self.btStockSearch.setText(_translate("MainWindow", "Pesquisar"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_4.setText(_translate("MainWindow", "Adicionar"))
        self.pushButton_5.setText(_translate("MainWindow", "Salvar"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Cliente"))
        self.label.setText(_translate("MainWindow", "Produto"))
        self.label_2.setText(_translate("MainWindow", "Quatidade"))
        self.label_3.setText(_translate("MainWindow", "Unidade"))
        self.label_4.setText(_translate("MainWindow", "Valor"))
        self.btSaleAddItem.setText(_translate("MainWindow", "Adicionar"))
        self.label_5.setText(_translate("MainWindow", "Barcode"))
        self.btSalveSave.setText(_translate("MainWindow", "Salvar"))
        self.btProdSearch.setText(_translate("MainWindow", "Pesquisar"))
        self.TabProduList.setTabText(self.TabProduList.indexOf(self.tabProdutosList), _translate("MainWindow", "Lista"))
        self.TabProduList.setTabText(self.TabProduList.indexOf(self.TabProdcCad), _translate("MainWindow", "Cadastro"))
        self.lbPgActual.setText(_translate("MainWindow", "Produtos"))


    #Process Functions
    def SearchProduct(self):
        query = self.edProdSearch.text()
        if len(query) > 3:
            #print(self.products.GetProducts(query))
            df = pd.DataFrame(self.products.GetProducts(query)).rename(columns= self.products.colouns_pt)
            self.tbProd.setModel(QModel(df))
            
            


    # UI functions
    def changeModule(self,index):
        self.stackedWidget.setCurrentIndex(index)

    def changeTitle(self):
        if self.stackedWidget.currentIndex() == 0:
            self.lbPgActual.setText('Estoque')
        elif self.stackedWidget.currentIndex() == 1:
            self.lbPgActual.setText('Compras')
        elif self.stackedWidget.currentIndex() == 2:
            self.lbPgActual.setText('Vendas')
        elif self.stackedWidget.currentIndex() == 3:
            self.lbPgActual.setText('Produtos')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
