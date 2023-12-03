# Improve_Smart_Crossroads
부산 연산 교차로의 스마트교차로의 교통 데이터를 통해 신호 주기를 개선 시켜 최적에 근사한 신호를 찾는 프로젝트

# 전체 프레임워크
## 스마트교차로 신호 개선 프레임워크
![image](https://github.com/choibumku00/Improve_Smart_Crossroads/assets/101037541/6f5489d4-902c-4907-89fc-75ab02a35d2d)
[프레임워크 코드 링크](https://github.com/choibumku00/Improve_Smart_Crossroads/blob/main/%EC%8A%A4%EB%A7%88%ED%8A%B8%EA%B5%90%EC%B0%A8%EB%A1%9C_%EC%8B%A0%ED%98%B8_%EA%B0%9C%EC%84%A0_%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC.ipynb)

# 실험 결과
## 기존 속도 대비 개선 속도 
![image](https://github.com/choibumku00/Improve_Smart_Crossroads/assets/101037541/f20bdd33-015e-4ff8-a5a8-d6c34cf1800e)

## LSTM DNN 정확도 측정
기존 교통량으로 1시간 후 교통량을 LSTM으로 알아낸다.  
그 교통량을 가지고 DNN에 넣어 속도를 예측한다.  
이 속도를 기존 속도와 비교한다.  
![image](https://github.com/choibumku00/Improve_Smart_Crossroads/assets/101037541/e504634c-5a4e-46fa-b14e-5907e188bfd8)
