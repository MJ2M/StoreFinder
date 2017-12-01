import os
from PyQt4.QtGui import *
import sys
import PyQt4_StoreFinder
from PyQt4.QtGui import QListWidgetItem
import csv  # csv 모듈 임포트
import random

print(os.getcwd() + "testPic")

## 데이터 처리 >> CSV를 읽어들임. 해당 코드는 라포를 출력

## in range() 에는 행의 수를 넣어줌. 일단 100 넣어둠
myData = [[0] * 6 for i in range(100)]
with open('store.csv') as f:
    store = list(csv.reader(f))


##print(store[0][0])

## 파일 이름과 대조해서 각 인덱스에 맞게 그림 세팅


## 사용자 정의 다이얼로그를 위한 클래스. QDialog와 Qt레이아웃의 Ui_Dialog 클래스 상속
class MyDialog(QDialog, PyQt4_StoreFinder.Ui_Dialog):
    ## 생성자 함수
    def __init__(self):
        QDialog.__init__(self)

        ## PyQt4_StoreFinder 레이아웃을 기준으로 위젯 생성 및 레이아웃 설정
        self.setupUi(self)

        ## 초기 맛집 리스트 정보 입력
        SetList(self)

        ## 초기 화면 이미지 세팅. 현재 자신의 디렉토리에서 불러온다.
        pix = QPixmap(os.getcwd() + "/MainPic")
        self.store_image.setPixmap(pix)

        ## 위젯 이벤트 핸들링 >> 객체.clicked.connect(self.실행 함수)
        self.itemList.clicked.connect(self.ItemClicked)
        self.favoriteList.clicked.connect(self.ItemClicked)
        self.total_button.clicked.connect(self.TotalClicked)
        self.korean_button.clicked.connect(self.KoreanClicked)
        self.cafe_button.clicked.connect(self.CafeClicked)
        self.pub_button.clicked.connect(self.PubClicked)
        self.etc_button.clicked.connect(self.EtcClicked)
        self.random_button.clicked.connect(self.RandomClicked)
        self.add_button.clicked.connect(self.AddClicked)
        self.delete_button.clicked.connect(self.DeleteClicked)

    ## 아이템 선택 시
    def ItemClicked(self):

        ## 아이템의 이름을 이용하여 CSV상의 자료 세팅
        ## name_label // category_label //introduction_label //address_label // store_image
        for i in range(94):
            if (self.itemList.currentItem().text() == store[i][2]):
                ## name_label
                self.name_label.setText(store[i][2])
                ## category_label
                self.category_label.setText(store[i][1])
                ## introduction_label
                self.introduction_label.setText(store[i][4])
                ## address_label
                self.address_label.setText(store[i][3])
                ##store_image
                pix = QPixmap(os.getcwd() + "/Pic/" + store[i][2])
                self.store_image.setPixmap(pix)

    ## 카테고리 버튼 기능 함수
    def TotalClicked(self):
        ResetList(self)
        SetList(self)

    def KoreanClicked(self):
        ResetList(self)
        SetCategoryList(self, "한식")

    def EtcClicked(self):
        ResetList(self)
        SetCategoryList(self, "기타 음식")

    def CafeClicked(self):
        ResetList(self)
        SetCategoryList(self, "카페")

    def PubClicked(self):
        ResetList(self)
        SetCategoryList(self, "술집")

    ## 랜덤 버튼 기능 함수

    def RandomClicked(self):

        ##무작위로 아이템 선택, 메세지 출력 및 리스트에서 골라준다.

        randNum = random.randrange(0, self.itemList.count())
        self.itemList.setCurrentItem(self.itemList.item(randNum))

        ## 위의 ItemClicked 에서 사용되는 코드를 재사용.
        ## 함수로 빼고 싶었지만 오류가 나서 이대로 보류.

        for i in range(94):
            if (self.itemList.currentItem().text() == store[i][2]):
                ## name_label
                self.name_label.setText(store[i][2])
                ## category_label
                self.category_label.setText(store[i][1])
                ## introduction_label
                self.introduction_label.setText(store[i][4])
                ## address_label
                self.address_label.setText(store[i][3])
                ##store_image
                pix = QPixmap(os.getcwd() + "/Pic/" + store[i][2])
                self.store_image.setPixmap(pix)

        ## 메세지 출력
        QMessageBox.information(self, "여기로 결정!", self.itemList.currentItem().text())

    def AddClicked(self):
        # 현재 item 리스트에서 선택한 값을 이용해 favorite 리스트에 아이템 추가

        check = True

        for i in range(self.favoriteList.count()):

            if (self.favoriteList.item(i).text() == self.itemList.currentItem().text()):
                check = False

        if (check == True):
            self.favoriteList.addItem(self.itemList.currentItem().text())
            QMessageBox.information(self, "Info", "추가 완료")

    def DeleteClicked(self):
        # 현재 favorite 리스트에서 선택된 아이템을 삭제
        item = self.favoriteList.takeItem(self.favoriteList.currentRow())
        item = None
        QMessageBox.information(self, "Info", "삭제 완료")


### 리스트 관련 커스텀 함수

## 리스트 아이템 전부 리셋(삭제)
def ResetList(self):
    while (self.itemList.count() > 0):
        item = self.itemList.takeItem(0)
        item = None


## 리스트 아이템 전부 세팅
def SetList(self):
    for i in range(94):
        if (store[i][2] != ""):
            self.itemList.addItem(store[i][2])


## 카테고리에 이름에 맞게 리스트 아이템 세팅
def SetCategoryList(self, category):
    for i in range(94):
        if (store[i][2] != ""):
            if (store[i][1] == category):
                self.itemList.addItem(store[i][2])


### App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

## 완료된 작업

## PyQt4 모듈 사용 방법 찾기(Qt Designer >> .py 변환 등)

## Qt Designer로 리스트 위젯, 추가 버튼, 삭제 버튼 UI 생성

## 리스트에 아이템 추가 및 삭제 기능 구현

## CSV 파싱(맛집 이름, 소개 등의 텍스트) 작업

## (필수 )프로그램 실행시 모든 맛집의 정보를 미리 리스트에 입력하도록 처리.

## (필수) 리스트에서 아이템 선택 시, 선택된 아이템의 이름에 따라 데이터 탐색&맛집 정보(글&이미지) 세팅 처리.

## (추가) 카테고리별로 리스트에서 맛집 토글 기능 구현

## (추가) 랜덤으로 맛집을 추천해주는 기능 구현


## 전달 사항

##(1) 버그 = 등촌 칼국수의 이미지가 로드되지 않습니다. 원인은 발견하지 못했습니다.

##(2) 파리바게트, 뚜레쥬르는 이미지가 없어서 직접 추가하였습니다 (교내 지점이 맞는지는 불명)

##(3) 미묘라멘(히카루호시), 스트라다의 경우 이미지가 없어서 메인 이미지와 동일하게

##해두었습니다. PIC 폴더에서 이미지 파일을 교체하고 실행하면 바로 변경되므로

##여유가 남는 경우 추가되면 더 좋을 것 같습니다.








