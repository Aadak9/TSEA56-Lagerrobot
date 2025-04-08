/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.9.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLabel *Korlage;
    QPushButton *Autonomt;
    QPushButton *Manuellt;
    QLabel *Lagermiljo;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLabel *Kolumner;
    QLabel *Rader;
    QLabel *Varor;
    QComboBox *Col_edit;
    QComboBox *Row_edit;
    QComboBox *Varor_edit;
    QMenuBar *menubar;
    QMenu *menuGUI;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1108, 647);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        Korlage = new QLabel(centralwidget);
        Korlage->setObjectName("Korlage");
        Korlage->setGeometry(QRect(900, 0, 131, 41));
        Korlage->setScaledContents(false);
        Autonomt = new QPushButton(centralwidget);
        Autonomt->setObjectName("Autonomt");
        Autonomt->setGeometry(QRect(830, 50, 80, 24));
        Manuellt = new QPushButton(centralwidget);
        Manuellt->setObjectName("Manuellt");
        Manuellt->setGeometry(QRect(910, 50, 80, 24));
        Lagermiljo = new QLabel(centralwidget);
        Lagermiljo->setObjectName("Lagermiljo");
        Lagermiljo->setGeometry(QRect(180, 10, 131, 16));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName("gridLayoutWidget");
        gridLayoutWidget->setGeometry(QRect(40, 80, 341, 311));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(0, 0, 0, 0);
        Kolumner = new QLabel(centralwidget);
        Kolumner->setObjectName("Kolumner");
        Kolumner->setGeometry(QRect(80, 30, 61, 20));
        Rader = new QLabel(centralwidget);
        Rader->setObjectName("Rader");
        Rader->setGeometry(QRect(180, 30, 61, 20));
        Varor = new QLabel(centralwidget);
        Varor->setObjectName("Varor");
        Varor->setGeometry(QRect(280, 30, 61, 20));
        Col_edit = new QComboBox(centralwidget);
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->addItem(QString());
        Col_edit->setObjectName("Col_edit");
        Col_edit->setGeometry(QRect(80, 50, 65, 24));
        Row_edit = new QComboBox(centralwidget);
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->addItem(QString());
        Row_edit->setObjectName("Row_edit");
        Row_edit->setGeometry(QRect(160, 50, 65, 24));
        Varor_edit = new QComboBox(centralwidget);
        Varor_edit->addItem(QString());
        Varor_edit->addItem(QString());
        Varor_edit->addItem(QString());
        Varor_edit->addItem(QString());
        Varor_edit->addItem(QString());
        Varor_edit->setObjectName("Varor_edit");
        Varor_edit->setGeometry(QRect(260, 50, 65, 24));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 1108, 21));
        menuGUI = new QMenu(menubar);
        menuGUI->setObjectName("menuGUI");
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuGUI->menuAction());

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        Korlage->setText(QCoreApplication::translate("MainWindow", "K\303\266rl\303\244ge:", nullptr));
        Autonomt->setText(QCoreApplication::translate("MainWindow", "Autonomt", nullptr));
        Manuellt->setText(QCoreApplication::translate("MainWindow", "Manuellt", nullptr));
        Lagermiljo->setText(QCoreApplication::translate("MainWindow", "Lagermilj\303\266", nullptr));
        Kolumner->setText(QCoreApplication::translate("MainWindow", "Kolumner", nullptr));
        Rader->setText(QCoreApplication::translate("MainWindow", "Rader", nullptr));
        Varor->setText(QCoreApplication::translate("MainWindow", "Varor", nullptr));
        Col_edit->setItemText(0, QCoreApplication::translate("MainWindow", "1", nullptr));
        Col_edit->setItemText(1, QCoreApplication::translate("MainWindow", "2", nullptr));
        Col_edit->setItemText(2, QCoreApplication::translate("MainWindow", "3", nullptr));
        Col_edit->setItemText(3, QCoreApplication::translate("MainWindow", "4", nullptr));
        Col_edit->setItemText(4, QCoreApplication::translate("MainWindow", "5", nullptr));
        Col_edit->setItemText(5, QCoreApplication::translate("MainWindow", "6", nullptr));
        Col_edit->setItemText(6, QCoreApplication::translate("MainWindow", "7", nullptr));
        Col_edit->setItemText(7, QCoreApplication::translate("MainWindow", "8", nullptr));
        Col_edit->setItemText(8, QCoreApplication::translate("MainWindow", "9", nullptr));
        Col_edit->setItemText(9, QCoreApplication::translate("MainWindow", "10", nullptr));

        Row_edit->setItemText(0, QCoreApplication::translate("MainWindow", "1", nullptr));
        Row_edit->setItemText(1, QCoreApplication::translate("MainWindow", "2", nullptr));
        Row_edit->setItemText(2, QCoreApplication::translate("MainWindow", "3", nullptr));
        Row_edit->setItemText(3, QCoreApplication::translate("MainWindow", "4", nullptr));
        Row_edit->setItemText(4, QCoreApplication::translate("MainWindow", "5", nullptr));
        Row_edit->setItemText(5, QCoreApplication::translate("MainWindow", "6", nullptr));
        Row_edit->setItemText(6, QCoreApplication::translate("MainWindow", "7", nullptr));
        Row_edit->setItemText(7, QCoreApplication::translate("MainWindow", "8", nullptr));
        Row_edit->setItemText(8, QCoreApplication::translate("MainWindow", "9", nullptr));
        Row_edit->setItemText(9, QCoreApplication::translate("MainWindow", "10", nullptr));

        Varor_edit->setItemText(0, QCoreApplication::translate("MainWindow", "1", nullptr));
        Varor_edit->setItemText(1, QCoreApplication::translate("MainWindow", "2", nullptr));
        Varor_edit->setItemText(2, QCoreApplication::translate("MainWindow", "3", nullptr));
        Varor_edit->setItemText(3, QCoreApplication::translate("MainWindow", "4", nullptr));
        Varor_edit->setItemText(4, QCoreApplication::translate("MainWindow", "5", nullptr));

        menuGUI->setTitle(QCoreApplication::translate("MainWindow", "GUI", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
