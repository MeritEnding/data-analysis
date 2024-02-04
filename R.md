# R 요약
  통계분석 데이터가 복잡해지면 복잡해질수록 쉬워진다.

## R 설치 후
  Tools 
   자료형
   1)숫자형 
   2)문자형 " "
   3)논리형 TRUE FALSE
  
  ```
  > 3
  [1] 3
  > hi
  에러: 객체 'hi'를 찾을 수 없습니다
  > "hi"
  [1] "hi"
  > 35
  [1] 35
  > 김함수
  에러: 객체 '김함수'를 찾을 수 없습니다
  > '김함수'
  [1] "김함수"
  > "김함수"
  [1] "김함수"
  > 3+2i
  [1] 3+2i
  > TRUE
  [1] TRUE
  > FALSE
  [1] FALSE
  ```
## 변수
  A=100 입력하면 Environment 확인
  사람이 많을때 변수를 이용하면 어려움
  => 자료구조 사용
  ```
  > 100
  [1] 100
  > A=100
  > A1=100
  > A_2=200
  > .B=300
  > name_1='김함수'
  > name_2='박산술'
  > name =c('김함수','박산술','이비교','송논리','최검정','유반복')
  > name =c('김함수','박산술','이비교','송논리','최검정','유반복')
  > name =c('김함수','박산술','이비교','송논리','최검정','유반복')
  > a=3
  > bb=10
  ```


## 자료구조
  데이터를 편하게 담을 수 있음
  벡터: 같은 종류의 데이터를 일렬로 나열  c('김땡땡','이땡땡','박땡땡','나땡땡')
  => 오류 있을때는 script 창에서 박스 씌운 후 Run을 누르기

  벡터형
  문자형,숫자형 동시에 입력 문자형으로 다 바뀜
  
  
  데이터프레임
  벡터를 이용해서 만든 자료형
  엑셀과 비슷함
  ```
  > weight=c(72,69,78,58,47,65)
  > name =c('김함수','박산술','이비교','송논리','최검정','유반복')
  > gender=c('남','남','남','여','여','여')
  > age=c(35,27,42,33,25,47)
  > height=c(183,177,175,167,155,173)
  > weight=c(72,69,78,58,47,65)
  > KHS=c('김함수','남',35,183,72)
  > KHS
  [1] "김함수" "남"     "35"     "183"    "72"    
  > mydf= data.frame(name,gender,age,height,weight)
  > mydf
      name gender age height weight
  1 김함수     남  35    183     72
  2 박산술     남  27    177     69
  3 이비교     남  42    175     78
  4 송논리     여  33    167     58
  5 최검정     여  25    155     47
  6 유반복     여  47    173     65
  ```


## 연산: 둘 이상의 대상을 조작하여 새로운 것을 만들어내는 것
  
  ### 산술연산자
  ```
  > 1+2
  [1] 3
  > 1-2
  [1] -1
  > 1*2
  [1] 2
  > 1/2
  [1] 0.5
  > 1/3
  [1] 0.3333333
  > 2^3
  [1] 8
  > 2**3
  [1] 8
  > a=10
  > b=2
  > a/b
  [1] 5
  > v1=c(1,2,3)
  > v2=c(4,5,6)
  > v1+v2
  [1] 5 7 9
  > v1*v2
  [1]  4 10 18
  > v1^3
  [1]  1  8 27
  ```
  ### 비교 연산자
  ```
  > 2==3
  [1] FALSE
  > 2<=3
  [1] TRUE
  > v1=c(1,2,3)
  > v2=c(4,5,6)
  > v1>v2
  [1] FALSE FALSE FALSE
  ```
  ### 논리연산
  
  and 피연산자가 둘다 TRUE =>TRUE
  
  or 피연산자가 하나만 TRUE 여도 TRUE 반환
  
  not 피연산자가 TRUE면 FALSE, FALSE면 TRUE
  
  
##조건문
   " 만약 x가 3이상이면 ,'안녕'을 출력한다"
  ```
  >x=5
  > 
  > if(x>=3){
  +   print("안녕")
  + }
  [1] "안녕"
  > x=1
  > 
  > if(x>=3){
  +   print("안녕")
  + }
  > 
```
## 반복문
```
   for
   "(1,2,3,4,5)에 들어있는 값에 10을 곱해서 하나씩 출력하시오"
  
  for(i in c(1,2,3,4,5))
  > for(i in c(1,2,3,4,5))
  + {
  +   print(i*10)
  + }
  [1] 10
  [1] 20
  [1] 30
  [1] 40
  [1] 50
  
  "(1,2,3,4,5,6,7,8,9,10) 값을 2n+3에 하나씩 입력해서 출력하시오"
  
  > for (i in 1:10)
  +   print(2*i+3)
  [1] 5
  [1] 7
  [1] 9
  [1] 11
  [1] 13
  [1] 15
  [1] 17
  [1] 19
  [1] 21
  [1] 23
```
## 함수
```
  > name =c('김함수','박산술','이비교','송논리','최검정','유반복')
  > gender=c('남','남','남','여','여','여')
  > age=c(35,27,42,33,25,47)
  > height=c(183,177,175,167,155,173)
  > weight=c(72,69,78,58,47,65)
  > mean(age)
  [1] 34.83333
  
  함수 -bmi (몸무게/키의 제곱)
  
  > cal_bmi = function( w , h ){
  +   
  +   bmi = w/(h/100)^2
  +   return(bmi)
  +   
  + }
  > cal_bmi(80,180)
  [1] 24.69136
```

## 패키지(함수,데이터) : 유용한 기능들을 공유하고 싶을때 or 사용하고싶을때

  ```
  install.packages("readxl")
  library(readxl)
  ```

## boxplot, t-test 

  여자와 남지 키 비교해보는 프로젝트
  
  t검정은 표본의 크기가 각각 30보다 커야함
  
  전체 데이터가 100개라면 크기가 작은 순서대로 나열한뒤에 25번째 Q1
  50번째 Q2
  75번째 Q3
  최댓값 100번째
  이상치 이상적인 데이터
  
   상자수염그림(각 성별의 키)
  df 데이터 프레임에서 height라는 열은 gender라는 기준으로 분류해서
   상자 수염을 그려라
   
  `boxplot(height~gender, df)`
  성별을 기준으로 키를 비교하여라
   표본의 크기가 작으면 p-vale 이상하게 나옴옴
  `t.test(height~gender,df)`

## 단축키
  ```
  Ctrl+enter : 코드 실행
  Ctrl+L: 콘솔창 비우기
  ```
## help 기능
함수 설명해주는 기능
  ```
  help(t.test)
  ?t.test
  ```


