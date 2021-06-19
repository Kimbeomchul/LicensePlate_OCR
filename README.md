## 2021 신기술프로젝트 ( 번호판 탐지 및 OCR ) 
- 제작 기간 : Nov 2020 ~ Jan 2021
- 맡은파트 : 번호판 탐지 && OCR
- 초기목적 : SRGAN을 이용한 흐린 번호판 화질개선 프로젝트였지만 유의미한 화질개선이 
발생하지 않아 OCR로 변경
1. 번호판 인식을 위한 라벨링작업
2. 번호판 인식 모델 학습
3. 번호판 인식범위로 이미지 자르기
4. 잘라진 이미지에 대한 숫자 라벨링작업
5. 완료된 라벨링 작업에 대한 OCR모델생성
-  4&5번 에서 발생하는 낮은 인식률로인해 오픈소스를 이용한 OCR진행


## Demo
<img src="img/capstone.gif" width="300">


## What We Used
![image](https://user-images.githubusercontent.com/54543148/122645007-ed148300-d152-11eb-8dd8-44ba183a00f9.png)
![img](./img/used.png)


## Sample Screens

|screens||
|:---:|:----:|
| ![img1](/img/capstone1.png) </br>main page | ![img2](/img/capstone_map.png) </br> google map |
| ![img3](/img/capstone_search.png) </br> search page | ![img4](/img/capstone_detail.png) </br> detail page |


### Training Image Data
- https://www.kaggle.com/ 
