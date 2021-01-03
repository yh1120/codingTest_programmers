# codingTest_programmers

### 크레인 인형뽑기 게임
#### 31-12-20
- 2시간 정도 걸렸다. 파이썬으로 코딩을 한 것이 처음이어서 익숙한 C를 대략 먼저 구현하고 이것을 파이썬으로 재코딩했다.
- 파이썬은 따로 인덱스 변수가 필요없고 그 안에서 바로 변수를 찾아서 사용할 수 있다.
- 그리고 list를 선언할 때 빈 list면 `[]`만으로도 만들 수 있었다.

### 두 개 뽑아서 더하기
#### 01-01-21
- 이 문제는 모든 인덱스에 대하여 자신보다 뒤에 있는 숫자를 더해서 list로 저장한 뒤, 이것을 set형태로 바꿔 겹치는 값을 소멸시킨다.
- 이후에 다시 list화 시켜서 움직일 수 있는 형태로 만들고 sorted 함수를 통해 오름차순 정렬을 한다.
- 인덱스 k를 둔 이유는, 현재 인덱스의 값은 알 수 있지만 그 인덱스를 따로 알지 못해서 인덱스를 정해주었다.
- 이런 식이라면 차라리 첫번째 반복문을 인덱스로 주고 뒤로 찾아나가는 식으로 하면 더 깔끔하지 않았을까 싶기도 하다.

### 완주하지 못한 선수
#### 02-01-21
- 두개의 리스트가 주어지고, 다른 하나에 비해 개수가 1개 부족하다.
- 처음에는 도전자의 이름을 완주자에서 찾고 같은 값이 있으면 그 이름을 완주자 목록에서 제거하는 식으로 진행했다.
- 하지만 이 방법은 10만명이 주어진다고 가정할 때, 대략 50억번의 검색을 해야 한다.
- 이러한 시간적 문제로, 먼저 두 목록을 sorted를 통해 정렬을 실행한다.
- 이렇게 되면 1명을 제외한 모든 이름이 순차적으로 진행이 되기 때문에 처음부터 끝까지 최대 10만번만 검색을 하면 된다.
- sorted 함수도 분명 시간이 들어가는 작업이겠지만 위의 경우보단 시간이 절약될 수 있었다.
- 다른 사람의 풀이를 보면 collections 모듈을 사용했다.
    ```angular2html
    import collections


    def solution(participant, completion):
        answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]
    ```

### 모의고사
#### 03-01-21
- 모의고사는 세개의 다른 패턴을 통해서 가장 높은 정답률을 가진 사람을 도출해내는 문제이다.
- 이것을 패턴화해서 검색하는 방법을 썼어야했는데 그 방법을 몰라서 나는 각각의 경우를 if문으로 케이스화했다.
- 하지만 이것보다 쉽게 푸는 방법은 pattern 리스트들을 정의한 후, enumerate 함수를 통해 인덱스와 해당 객체를 가져와서 그것을 비교하는 방법이다.
- 이렇게 인덱스와 객체를 같이 가져올 수 있는 함수라면 비교하기 더 수월해질 것 같다.
- 또한 케이스를 각자 나누는 것이 아니고 이것을 리스트화해서, 그곳에서 가져올 수 있게 하면 좋을 것 같다.
    ```
    def solution(answers):
        pattern1 = [1,2,3,4,5]
        pattern2 = [2,1,2,3,2,4,2,5]
        pattern3 = [3,3,1,1,2,2,4,4,5,5]
        score = [0, 0, 0]
        result = []

        for idx, answer in enumerate(answers):
            if answer == pattern1[idx%len(pattern1)]:
                score[0] += 1
            if answer == pattern2[idx%len(pattern2)]:
                score[1] += 1
            if answer == pattern3[idx%len(pattern3)]:
                score[2] += 1

        for idx, s in enumerate(score):
            if s == max(score):
                result.append(idx+1)

        return result

    ```- 그리고 list를 선언할 때 빈 list면 `[]`만으로도 만들 수 있었다.
