#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::clearGrid()
{
    QLayoutItem *item;
    while ((item = ui->gridLayout->takeAt(0)) != nullptr)
    {
        if (item->widget())
            {
                delete item->widget();
            }
        delete item;
    }
}

void MainWindow::generateGrid()
{
    int cols = ui->Col_edit->currentText().toInt();
    int rows = ui->Row_edit->currentText().toInt();

    clearGrid();

    for (int row = 0; row < rows; ++row) {
        for (int col = 0; col < cols; ++col) {
            QLabel *cell = new QLabel(QString("(%1,%2)").arg(row).arg(col));
            cell->setStyleSheet("border: 1px solid gray; background: #eee; padding: 4px;");
            cell->setAlignment(Qt::AlignCenter);
            ui->gridLayout->addWidget(cell, row, col);
        }
    }

}

void MainWindow::on_comboBox_currentIndexChanged(int index)
{
    int rows = ui->Row_edit->currentText().toInt();
    int cols = ui->Col_edit->currentText().toInt();

    generateGrid();
}

