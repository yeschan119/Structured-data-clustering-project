# Structured-data-clustering-project
데이터 클러스터링 프로젝트

## Purpose of this project
  + raw data에서 같은 속성을 가진 데이터를 찾아 군집화 하는 프로젝트

## member
  + 1인 프로젝트

## 사용 언어
  + python

## 사용한 알고리즘
  + DB SCAN(based on Density Based Algorithm)
  
## Loss Function
  + epsilon, minpoint

## process of the project
  + 벡터형식의 데이터를 입력받기
    ```
    data = pd.read_csv(path, sep='\t',names=columns)
    ```
  + 군집을 결정하는 반지름(epsilon)과 최소 집합(minpoints)을 결정
    ```
    eps = int(sys.argv[3])
    minpts = int(sys.argv[4])
    ```
  + 임의의 점을 선택하여 이 점과 다른 모든 점들 사이 거리를 구하기
  + epsilon보다 작은 거리에 있는 데이터의 집합 중 minpoint를 만족하는 데이터를 하나의 군집으로 결정
  + 결정된 군집안의 모든 데이터에 대해서 recursive한 방법으로 또 다른 군집을 찾기
  + 더는 다른 cluster가 나오지 않으면 해당 데이터를 완전한 하나의 cluster로 정하고 이를 제외한 다른 데이터로 clustering 반복
## 코드 실행 방법
  ```
  python cluster.py input.txt 8 15 22
  # pyhon code, input data, cluster 개수, epsilon, minpoints
  ```
## 군집화 결과
![_2021-06-06__8 01 07](https://user-images.githubusercontent.com/83147205/165156124-9264eee3-60be-47d2-95e5-4789bf63c15f.png)

