# Improve_Smart_Crossroads
부산 연산 교차로의 스마트교차로의 교통 데이터를 통해 신호 주기를 개선 시켜 최적에 근사한 신호를 찾는 프로젝트

# 전체 프레임워크
## 스마트교차로 신호 개선 프레임워크
![image](https://github.com/025792/Improve_Smart_Crossroads/assets/145456342/3e0f96b4-ac0d-4f60-9c9d-2af6a0c912d6)  
[프레임워크 코드 링크](https://github.com/choibumku00/Improve_Smart_Crossroads/blob/main/%EC%8A%A4%EB%A7%88%ED%8A%B8%EA%B5%90%EC%B0%A8%EB%A1%9C_%EC%8B%A0%ED%98%B8_%EA%B0%9C%EC%84%A0_%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC.ipynb)

# 실험 결과
## 기존 속도 대비 개선 속도 
![image](https://github.com/choibumku00/Improve_Smart_Crossroads/assets/101037541/f20bdd33-015e-4ff8-a5a8-d6c34cf1800e)

## LSTM DNN 정확도 측정
기존 교통량으로 1시간 후 교통량을 LSTM으로 알아낸다.  
그 교통량을 가지고 DNN에 넣어 속도를 예측한다.  
이 속도를 기존 속도와 비교한다.  
### 기존
![image](https://github.com/choibumku00/Improve_Smart_Crossroads/assets/101037541/e504634c-5a4e-46fa-b14e-5907e188bfd8)

### 날씨 제거
![lstm_dnn 정확도(날씨 제거)](https://github.com/choibumku00/Improve_Smart_Crossroads/assets/101037541/eea813fc-b3b4-4cbc-8d70-70f4dd80b87f)


## 개별 모델 정확도
### 기존
LSTM MSE: 338.56  
DNN MSE: 8.00  
LSTM + DNN MSE: 8.29  

### 날씨 제거
LSTM MSE: 351.84  
DNN MSE: 8.03  
LSTM + DNN MSE: 8.10  
