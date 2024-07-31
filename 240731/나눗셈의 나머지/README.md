# [나눗셈의 나머지 ](https://www.codetree.ai/missions/4/problems/remainder-of-division)

|유형|문제 경험치|난이도|
|---|---|---|
|[Novice Low / 1차원 배열 / Count 배열](https://www.codetree.ai/missions?missionId=4)|20xp|![쉬움][easy]|








[b5]: https://img.shields.io/badge/Bronze_5-%235D3E31.svg
[b4]: https://img.shields.io/badge/Bronze_4-%235D3E31.svg
[b3]: https://img.shields.io/badge/Bronze_3-%235D3E31.svg
[b2]: https://img.shields.io/badge/Bronze_2-%235D3E31.svg
[b1]: https://img.shields.io/badge/Bronze_1-%235D3E31.svg
[s5]: https://img.shields.io/badge/Silver_5-%23394960.svg
[s4]: https://img.shields.io/badge/Silver_4-%23394960.svg
[s3]: https://img.shields.io/badge/Silver_3-%23394960.svg
[s2]: https://img.shields.io/badge/Silver_2-%23394960.svg
[s1]: https://img.shields.io/badge/Silver_1-%23394960.svg
[g5]: https://img.shields.io/badge/Gold_5-%23FFC433.svg
[g4]: https://img.shields.io/badge/Gold_4-%23FFC433.svg
[g3]: https://img.shields.io/badge/Gold_3-%23FFC433.svg
[g2]: https://img.shields.io/badge/Gold_2-%23FFC433.svg
[g1]: https://img.shields.io/badge/Gold_1-%23FFC433.svg
[p5]: https://img.shields.io/badge/Platinum_5-%2376DDD8.svg
[p4]: https://img.shields.io/badge/Platinum_4-%2376DDD8.svg
[p3]: https://img.shields.io/badge/Platinum_3-%2376DDD8.svg
[p2]: https://img.shields.io/badge/Platinum_2-%2376DDD8.svg
[p1]: https://img.shields.io/badge/Platinum_1-%2376DDD8.svg
[passed]: https://img.shields.io/badge/Passed-%23009D27.svg
[failed]: https://img.shields.io/badge/Failed-%23D24D57.svg
[easy]: https://img.shields.io/badge/쉬움-%235cb85c.svg?for-the-badge
[medium]: https://img.shields.io/badge/보통-%23FFC433.svg?for-the-badge
[hard]: https://img.shields.io/badge/어려움-%23D24D57.svg?for-the-badge


코드에도 주석은 달아 뒀지만 (50,3), (10,2)와 같은 케이스를 이용하여 수정 성공.

(50,3): 나머지가 0 1 0 이렇게 나오는데, 이 때 result.sort()를 넣어 한 번 소팅해 주지 않으면 0 2번 1 한번인데 각각 1번씩 등장한 걸로 카운트해 최종 정답이 3이 나오는 사태가 발생한다.

(10,2): 막판에 a=1이 되는데, 여기서 계산을 멈춰야 한다. 'a가 1 이하가 되기 전까지' 라는 말이 다소 헛갈리기 쉽지만 'a가 1 이하가 되는' 그 순간 while문은 바로 깨져야 한다. 더 이상 어떤 원소도 results에 추가되어서는 안 된다.
