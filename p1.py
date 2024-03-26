# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os



class Ui_MainWindow(object):
    excelfilename=[]
    excelname=[]
    select_folder_location=1
    nowfile=''
    dir_path=''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.lightGray)
        MainWindow.setPalette(palette)

        # 分组框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1500, 200))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 300, 750))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 960, 1980, 210))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter)

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 210, 1680, 750))
        self.groupBox_4.setObjectName("groupBox_4")

        # 附加功能
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 230, 300, 730))
        self.listWidget.setObjectName("listWidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 230, 1670, 730))
        self.textBrowser.setObjectName("textBrowser")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 1000, 300, 30))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)



        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 1060, 300, 30))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(False)
        # self.radioButton_2.clicked.connect(self.radioButton2_Clicked)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 1060, 1500, 30))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1820, 1060, 50, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.savefile_selcet)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 按键
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(0, 40, 150, 150))
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setAutoFillBackground(False)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("2.2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.getfile)


        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_2.setGeometry(QtCore.QRect(150, 40, 150, 150))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("2.3.ico"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.column_select)

        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_3.setGeometry(QtCore.QRect(300, 40, 150, 150))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("2.4.ico"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.directed_screening)

        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_4.setGeometry(QtCore.QRect(450, 40, 150, 150))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("2.5.ico"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.clicked.connect(self.Table_Merge)



        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_5.setGeometry(QtCore.QRect(600, 40, 150, 150))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("2.6.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon5)
        self.toolButton_5.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_5.setAutoRepeatDelay(300)
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.Statistical_Ranking)

        self.toolButton_6 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_6.setGeometry(QtCore.QRect(750, 40, 150, 150))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("2.7.ico"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon6)
        self.toolButton_6.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_6.clicked.connect(self.Chart_Generation)

        self.toolButton_7 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_7.setGeometry(QtCore.QRect(900, 40, 150, 150))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("2.8.ico"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon7)
        self.toolButton_7.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_7.setAutoRepeatInterval(100)
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_7.setAutoRaise(True)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_7.clicked.connect(MainWindow.close)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # self.textBrowser.setFontPointSize(60)
        if self.dir_path == "":
            self.textBrowser.setText('请点击导入EXCEL按钮，选择目标excel文件所在文件夹')
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(25)
            font.setFamily('微软雅黑')
            self.textBrowser.setFont(font)
            self.textBrowser.setAlignment(Qt.AlignCenter)

        # 选择文件并显示在文本框中
    def getfile(self):
        try:
            import os
            # dir_path即为选择的文件夹的绝对路径，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            if self.dir_path != "":
                print(self.dir_path)
                self.folder_location = ("%s" % self.dir_path) + '/mycell.xlsx'
                if self.radioButton_2.isChecked() == True:
                    print('模式2')
                else:
                    self.save_folder = self.folder_location
                self.list = os.listdir(self.dir_path)  # 列出文件夹下所有的目录与文件
                flag = 1 # 标识插入新行的位置
                for i in range(0, len(self.list)):  # 遍历文件列表
                    # 拼接路径和文件
                    if os.path.splitext(self.list[i])[1] == '.xls':  # 目录下包含的.xls文件
                        self.excelfilename.append(os.path.join(self.dir_path, self.list[i]))
                        self.excelname.append(self.list[i])
                        print(self.list[i])  # 输出获取的表格名
                        self.listWidget.addItem(self.list[i])
                        flag=0;

                if flag!=0:
                    from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
                    QMessageBox.information(MainWindow, "文件导入提示框", "当前文件夹无目标表格，请选择正确的文件夹", QMessageBox.Ok)
                print('1')
                print(self.excelname[0])
                print('2')
                flag1=0;
                for i in range(0,5):
                    print(self.excelname[i])
                    if self.excelname[i]!= (str(i + 1)+"月销售数据.xls"):
                        print('3')
                        from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
                        QMessageBox.information(MainWindow, "文件导入提示框", "当前文件夹表格非目标表格，请选择正确的文件夹", QMessageBox.Ok)
                        self.excelname=[]
                        self.excelfilename=[]
                        self.listWidget.clear()
                        flag1=1
                if flag1==0:
                        self.textBrowser.setText('表格导入成功')
                        font = QtGui.QFont()
                        font.setBold(False)
                        font.setPointSize(9)
                        font.setFamily('宋体')
                        self.textBrowser.setFont(font)
                        from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
                        # 使用information()方法弹出信息提示框
                        QMessageBox.information(MainWindow, "提示框", "表格导入成功", QMessageBox.Ok)

                self.listWidget.itemClicked.connect(self.listWidget_clicked)
                columns = ['买家会员名', '买家支付宝账号', '买家应付货款', '买家实际支付金额', '订单状态', '收货人姓名', '收货地址', '联系手机', '订单创建时间',
                           '订单付款时间',
                           '宝贝标题', '宝贝种类', '物流单号', '物流公司', '订单备注', '宝贝总数量', '类别', '图书编号']
                df_list = []
                for i in range(5):
                    # file_name = str(i + 1) + "月销售数据.xls"
                    sheet_name = "淘宝20180" + str(i + 5)
                    print(self.excelfilename[i])
                    df = pd.read_excel("%s" % (self.excelfilename[i]), sheet_name=sheet_name, usecols=columns)
                    df_list.append(df)
                df_list.append(pd.read_excel("%s" % (self.excelfilename[5]), sheet_name="淘宝201810"))
                self.all_df = pd.concat(df_list)


            else:
                from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
                QMessageBox.information(MainWindow, "文件导入提示框", "请选择正确的文件夹", QMessageBox.Ok)
                pass
        except Exception as e:
            print(e)


    def listWidget_clicked(self, item):
        print(item.text())
        self.nowfile = ("%s" % self.dir_path) +'/'+ item.text()
        print(self.nowfile)
        # for i in range(len(self.excelfilename)+1):
        #     if  self.list[i] == item.text():
        #         self.nowfile=self.excelfilename[i-1]


    def savefile_selcet(self):
        dir = QFileDialog()  # 创建文件对话框
        dir.setFileMode(QFileDialog.Directory)
        # dir.setOption(QFileDialog.DontUseNativeDialog, True)
        dir.setDirectory('C:\\')  # 设置初始路径为C盘
        # # 设置只显示文本文件
        # dir.setNameFilter('表格文件(*.xls)')
        if dir.exec_():  # 判断是否选择了文件
            self.filename = dir.selectedFiles()  # 获取选择的文件
            self.select_folder_location=("%s" % self.filename[0]) + '\mycell.xlsx'
            if self.radioButton_2.isChecked() == True:
                self.save_folder = self.select_folder_location
            self.textEdit.setText(self.filename[0])  # 将选择的文件显示在文本框中

    def column_select(self):
        if self.dir_path != "":
            if self.nowfile != "":
                import os
                print(self.nowfile+'=')
                self.df = pd.read_excel("%s"%self.nowfile)
                print(self.df)
                # 提取列数
                self.column_data = self.df[['买家会员名', '收货人姓名', '联系手机', '宝贝标题']]
                self.textBrowser.clear()
                print(self.column_data.iloc[0, 0])
                data = ''
                for data_i in self.column_data:
                    data = data + '\t' + data_i
                self.textBrowser.append(data)
                for i in range(self.column_data.shape[0]):
                    data = str(i) + '\t'
                    for j in range(self.column_data.shape[1]):
                        data = data + str(self.column_data.iloc[i, j]) + '\t'
                    self.textBrowser.append(data)

                print('已显示')
                print(self.save_folder)
                if not os.path.exists(self.save_folder):
                    print('不存在')
                    with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='w') as writer:
                        # 将数据帧写入一个新工作表
                        self.column_data.to_excel(writer, sheet_name='列数据提取')
                else:
                    print('存在')

                    with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='a',if_sheet_exists='new') as writer:
                        # 将数据帧写入一个新工作表
                        self.column_data.to_excel(writer, sheet_name='列数据提取')
            else :
                from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
                QMessageBox.information(MainWindow, "文件导入提示框", "请先在表格列表中选中一个表格", QMessageBox.Ok)
                pass
        else:
            from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
            QMessageBox.information(MainWindow, "文件导入提示框", "请先点击导入EXCEL按钮导入表格", QMessageBox.Ok)
            pass

    def directed_screening(self):
        if self.dir_path != "":
            import os
            df = self.all_df
            new = df[df["宝贝标题"] == '零基础学Python']
            new1 = new[['买家会员名', '收货人姓名', '联系手机', '宝贝标题']]
            self.textBrowser.clear()
            print(new1.iloc[0, 0])
            data = ''
            for data_i in new1:
                data = data + '\t' + data_i
            self.textBrowser.append(data)
            for i in range(new1.shape[0]):
                data = str(i) + '\t'
                for j in range(new1.shape[1]):
                    data = data + str(new1.iloc[i, j]) + '\t'
                self.textBrowser.append(data)

            if not os.path.exists(self.save_folder):
                with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='w') as writer:
                    # 将数据帧写入一个新工作表
                    new1.to_excel(writer, sheet_name='定向筛选')
            else:
                with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='a',if_sheet_exists='new') as writer:
                    # 将数据帧写入一个新工作表
                    new1.to_excel(writer, sheet_name='定向筛选')
        else:
            from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
            QMessageBox.information(MainWindow, "文件导入提示框", "请先点击导入EXCEL按钮导入表格", QMessageBox.Ok)
            pass

    def Table_Merge(self):
        if self.dir_path != "":
            import os
            if not os.path.exists(self.save_folder):
                with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='w') as writer:
                    # 将数据帧写入一个新工作表
                    self.all_df.to_excel(writer, sheet_name='多表合并')
            else:
                with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='a',if_sheet_exists='new') as writer:
                    # 将数据帧写入一个新工作表
                    self.all_df.to_excel(writer, sheet_name='多表合并')

            from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
            # 使用information()方法弹出信息提示框
            QMessageBox.information(MainWindow, "提示框", "表格合并成功，已存入指定文件夹", QMessageBox.Ok)

        else:
            from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
            QMessageBox.information(MainWindow, "文件导入提示框", "请先点击导入EXCEL按钮导入表格", QMessageBox.Ok)
            pass


    def Statistical_Ranking(self):
        if self.dir_path != "":
            import os
            sort = self.all_df.groupby('宝贝标题')['宝贝总数量'].apply(np.sum).sort_values(ascending=False)
            self.textBrowser.clear()
            self.textBrowser.append('序号'+'\t'+'宝贝标题              '+'\t'+'宝贝总数量')
            dict = sort.to_dict()
            a = list(dict.keys())
            b = np.array(a)
            c = list(dict.values())
            d = np.array(c)
            for i in range(len(b)):
                data = str(i) +'\t'+ str(b[i]) +'\t' +str(d[i])+ '\t'
                self.textBrowser.append(data)

            # 打开Excel文件，并创建ExcelWriter对象

            if not os.path.exists(self.save_folder):
                with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='w') as writer:
                    # 将数据帧写入一个新工作表
                    sort.to_excel(writer, sheet_name='多表统计排行')
            else:
                with pd.ExcelWriter("%s"%(self.save_folder), engine='openpyxl', mode='a',if_sheet_exists='new') as writer:
                    # 将数据帧写入一个新工作表
                    sort.to_excel(writer, sheet_name='多表统计排行')
        else:
            from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
            QMessageBox.information(MainWindow, "文件导入提示框", "请先点击导入EXCEL按钮导入表格", QMessageBox.Ok)
            pass

    def Chart_Generation(self):
        if self.dir_path != "":
            # 一、读取excel数据
            # 1．因为要获取各图书的占比图，所以必须先根据图书名进行分组。
            # （1）读取已分组的mycell.xls文件。
            # 2．筛选已分组文件中的全彩系列图书。
            # 3．计算全彩系列图书的2018年上半年销售总额。
            # 4．依次遍历全彩系列各图书的数据，然后计算每一类图书的2018年上半年销售总额。
            # 5．计算每一类图书销售总额与全彩系列图书销售总额之比。
            # 筛选全彩系列图书2018年上半年收入占80%的产品。

            # data = pd.read_excel('6月销售数据.xls', sheet_name='淘宝201810')  # pandas读取excel的函数
            data =self.all_df
            df = data[data.类别 == '全彩系列']
            # 下面这个语句是以这键值重新组合成一个pandas，以columns里的为索引
            data1 = pd.DataFrame(df, columns=['买家实际支付金额', '订单状态', '宝贝标题', '宝贝总数量', '类别', '图书编号'])
            print(df)

            data1 = data1.sort_values(by='图书编号')  # sort是以学科类别为标准排序
            df = df.reset_index(drop=True)  # 重建索引
            # 定义导出的路径，并定义好文件名
            out1 = ("%s"%self.dir_path) +'\全彩系列表格.xlsx'
            print(out1)
            data1.to_excel("%s"%out1, sheet_name="汇总", index=False)


            # df = pd.read_excel("%s"%(out1))
            data = self.all_df
            df = data[data.类别 == '全彩系列']
            df1 = df.groupby(["图书编号"])["买家实际支付金额"].sum().reset_index()
            df1 = df1.set_index('图书编号')  # 设置索引
            df1 = df1[u'买家实际支付金额'].copy()
            print(df1)
            df2 = df1.sort_values(ascending=False)  # 排序
            # SaveExcel(df2, self.rButton2.isChecked())
            print(2)
            # 图表字体为华文细黑，字号为12
            plt.rc('font', family='SimHei', size=10)
            # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
            plt.figure("贡献度分析")
            df2.plot(kind='bar',figsize=(15,8))
            plt.ylabel(u'销售收入（元）')
            p = 1.0 * df2 / df2.sum()
            print(p)
            p.plot(color='r', secondary_y=True, style='-o', linewidth=0.5)
            plt.title("图书贡献度分析")
            plt.annotate(format(p[2], '.4%'), xy=(2, p[2]), xytext=(2 *3, p[2] * 3),
                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1"))  # 添加标记，并指定箭头样式。
            plt.ylabel(u'收入（比例）')
            plt.show()

        else:
            from PyQt5.QtWidgets import QMessageBox  # 导入QMessageBox类
            QMessageBox.information(MainWindow, "文件导入提示框", "请先点击导入EXCEL按钮导入表格", QMessageBox.Ok)
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excel数据分析师"))
        # 分组框
        self.groupBox.setTitle(_translate("MainWindow", "功能选项"))
        self.groupBox_2.setTitle(_translate("MainWindow", "表格列表"))
        self.groupBox_3.setTitle(_translate("MainWindow", "输出选项"))
        self.groupBox_4.setTitle(_translate("MainWindow", "主界面"))

        # 按键
        self.toolButton.setText(_translate("MainWindow", "导入EXCEL"))
        self.toolButton_2.setText(_translate("MainWindow", "提取列数据"))
        self.toolButton_3.setText(_translate("MainWindow", "定向筛选"))
        self.toolButton_4.setText(_translate("MainWindow", "多表合并"))
        self.toolButton_5.setText(_translate("MainWindow", "多表统计排行"))
        self.toolButton_6.setText(_translate("MainWindow", "生成图表"))
        self.toolButton_7.setText(_translate("MainWindow", "退出"))

        self.radioButton.setText(_translate("MainWindow", "保存在原文件夹中"))
        self.radioButton_2.setText(_translate("MainWindow", "自定义文件夹"))
        self.pushButton.setText(_translate("MainWindow", "浏览"))

        ##字体
        font = QtGui.QFont()
        font.setBold(True)
        # font.setFamily('宋体')  # 字体
        # self.groupBox.setFont(font)
        # self.groupBox_2.setFont(font)
        # self.groupBox_3.setFont(font)
        # self.groupBox_4.setFont(font)
        font.setFamily('微软雅黑')
        self.toolButton.setFont(font)
        self.toolButton_2.setFont(font)
        self.toolButton_3.setFont(font)
        self.toolButton_4.setFont(font)
        self.toolButton_5.setFont(font)
        self.toolButton_6.setFont(font)
        self.toolButton_7.setFont(font)
        font.setPointSize(11)
        font.setBold(False)
        font.setFamily('宋体')
        self.radioButton.setFont(font)
        self.radioButton_2.setFont(font)


# 主方法
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
