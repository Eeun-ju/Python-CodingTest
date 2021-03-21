# Python-CodingTest
이것이 취업을 위한 코딩 테스트다 with 파이썬- 문제풀이<br>
코딩과 알고리즘의 꾸준한 공부를 위해 만든 파일<br>

-------------------------------------------------
예제 3-1 거스름돈 : 가장 큰 화폐 단위부터 거슬러주기 (큰 단위가 작은 단위의 배수이면 몫을 생각하기)<br>
예제 3-2 큰 수의 법칙 : 큰 수와 그 다음 큰 수를 생각하기 <br>
예제 3-3 숫자 카드 게임 : min, max 함수의 사용 <br>
예제 3-4 1이 될 때까지 : 경우 나누기 - 우선적인 경우 생각하기 <br>
예제 4-1 상하좌우 : 미로찾기, 격자 움직임을 나눌 수 있는 리스트 [0,0,1,-1]/[1,-1,0,0] 기억하기 <br>
예제 4-2 시각 : 시간문제-> 문자열 변환도 좋은 방법 <br>
예제 4-3 왕실의 나이트 : for문 사용-> 시간 복잡도 증가 경우의 수가 작다면 경우를 직접 입력해주기 <br>
예제 4-4 게임 개발 : 방문 array, 위치 array 이용하기, 2차원에서 방향은 list로 설정하기 <br>

-----------------------------------------------
예제 5-1 스택 : 최하단 원소 출력, 최상단 원소 출력 방법 구분/ list 이용 <br>
예제 5-2 큐 : colletions-deque를 이용 popleft, pop 기억하기 <br>
예제 5-3 재귀 함수 : 재귀 함수 기억하기 <br>
예제 5-4 종료 재귀 : 종료문 설정 기억하기 <br>
예제 5-5 팩토리얼 : 두 가지 방법으로 구현<br>
예제 5-6,7 인접 행렬, 리스트 : 탐색 알고리즘에서 가장 많이 사용되는 기본 형태, 모두 2차원 리스트 사용<br>
예제 5-8 DFS : 재귀 함수를 이용한 함수-visit 리스트 필요 <br>
예제 5-9 BFS : 큐를 이용한 함수-visit 리스트 필요 <br>
예제 5-10 음료수 얼려 먹기 : BFS 이용, 상 하 좌 우 2차원 배열이라고 생각하기 <br>
예제 5-11 미로 탈출 : BFS 이용, 상 하 좌 우 2차원 배열이라고 생각하기 개수 카운트 <br>

-----------------------------------------------

예제 6-1 선택 정렬 : 처음 위치부터 가장 작은 값과 자리 바꾸기 <br>
예제 6-3 미로 탈출 : 처음 위치에서 시작, 하나씩 늘려가면서 정렬 <br>
예제 6-4 퀵 정렬 : 피벗의 위치를 기준으로 2구역으로 나누기 - 재귀함수<br>
예제 6-5 파이썬 장점 퀵 정렬 : 비교 연산 횟수 증가로 참고만 하기<br>
예제 6-6 계수 정렬 : 가장 빠르게 정렬 할 수 있음, 범위가 크지 않다는 조건 하<br>
예제 6-7 sorted : 내부 정렬 함수 사용하기 리스트, 딕셔너리 모두 가능<br>
예제 6-8 sort : 리스트 객체 내장함수<br>
예제 6-9 정렬 라이브러리에서 Key를 활용 : 튜플 구성 데이터에서 sorted(key=지정) <br>
예제 6-10 위에서 아래로 : 내림차순 정리 - 내부 함수 사용이 가장 빠름(코드작성) <br>
예제 6-11 성적이 낮은 순서로 학생 출력하기 : Key 이용한 오름차순 lambda 함수 이용하면 빠름! <br>
예제 6-12 두 배열의 원소 교체 : 가장 큰 변수와 작은 변수 바꾸기 list.sort() 이용 <br>

-----------------------------------------------

예제 7-1 [순차 탐색](Ch07.이진탐색/7-1.py) : 같은 문자 위치 찾기 for 이용 <br>
예제 7-2 [재귀 함수로 구현한 이진 탐색](Ch07.이진탐색/7-2.py) : 이진 탐색은 오직 **정렬된 상태에서만** 빠르게 위치를 찾을 수 있음 mid값을 통해 위치 파악하기 <br>
예제 7-3 [반복문으로 구현한 이진 탐색](Ch07.이진탐색/7-3.py) : while문 사용 7-2와 같은 코드 <br>
예제 7-4 [한 줄 입력받아 출력](Ch07.이진탐색/7-4.py) : 입력 데이터, 탐색 범위가 큰 이진 탐색 문제에서 입력을 받기 위해 sys 라이브러리 사용 <br>
예제 7-5 [부품 찾기](Ch07.이진탐색/7-5.py) : 큰 정수 입력, 범위가 클 경우 이진 탐색 생각하기 <br>
예제 7-6 [부품 찾기](Ch07.이진탐색/7-6.py) : index list생성 <br>
예제 7-7 [부품 찾기](Ch07.이진탐색/7-7.py) : set(집합)에서 존재 여부 확인 <br>
예제 7-8 [떡볶이 떡 만들기](Ch07.이진탐색/7-8.py) : 이진 탐색을 활용한 최소 수 찾기 - 중간지점을 기준으로 내리기 or 올리기 <br>

-----------------------------------------------

예제 8-1 [피보나치 함수](Ch08.다이나믹프로그래밍/8-1.py) : 재귀 함수를 이용한 피보나치 함수 <br>
예제 8-2 [피보나치 수열](Ch08.다이나믹프로그래밍/8-2.py) : 연산 기록하기 연산 list 생성 후 결과 이용 <br>
예제 8-3 [호출 함수 확인](Ch08.다이나믹프로그래밍/8-3.py) : 연산 순서 확인하기  <br>
예제 8-4 [피보나치 수열(반복)](Ch08.다이나믹프로그래밍/8-4.py) : 연산 list 누적해서 기록 마지막 결과 사용 <br>
예제 8-5 [1로 만들기](Ch08.다이나믹프로그래밍/8-5.py) : 경우의 수 최소의 계산-> min 이용 => 계산 수 이므로 +1 잊지말기 <br>
예제 8-6 [개미 전사](Ch08.다이나믹프로그래밍/8-6.py) : 모르겠다 -> i 번째 사용 할 수 있는가? 그 중 최소,최대 무엇을 구하는가 생각하기<br>
예제 8-7 [바닥 공사](Ch08.다이나믹프로그래밍/8-7.py) : i 번째 필요한 개수 i-1인 경우, i-2인 경우의 합으로 <br>
예제 8-8 [효율적인 화폐 구성](Ch08.다이나믹프로그래밍/8-8.py) : 작은 화폐 단위부터 계산 후 큰 단위로 그 후 mini 찾기 m원에서 list 전 위치가 불가능이 아닐 때 +1과 mini <br>

------------------------------------------

예제 9-1 간단한 다익스트라 알고리즘 : visited, distance 방문 기록을 이용하여 거리 계산 <br>

----------------------------------------

예제 12-7 [럭키 스트레이트](Ch12.구현문제/럭키스트레이트.py) : 각 자리수 합 이용 str -> int(leftsum, rightsum) <br>
예제 12-8 [문자열 재정렬](Ch12.구현문제/문자열재정렬.py) : 아스키 코드 이용시 ord(string) 각 번호에 맞춰서 사용. <br>
예제 12-9 [문자열 압축](Ch12.구현문제/문자열압축.py) : 문자열 크기 1~길이/2 늘려가면서 문자열 개수 세기 <br>
예제 12-11 [뱀](Ch12.구현문제/뱀.py) : 2차원 배열 초기화 [[0 for i in range(n+1)] for j in range(n+1)], 동서남북 방향 dx, dy 생각하기 <br>

--------------------------------------

예제 13-15 [특정 거리의 도시 찾기](Ch13.DFSBFS문제/13-15.py) : 단방향 도로 예제 9-1 아이디어와 동일 **다익스트라** 알고리즘 익히기 get_smallest_node() dijkstra(start) <br>


