# [배열 놀이 ](https://www.codetree.ai/missions/4/problems/play-with-array)

|유형|문제 경험치|난이도|
|---|---|---|
|[Novice Low / 1차원 배열 / 탐색](https://www.codetree.ai/missions?missionId=4)|30xp|![어려움][hard]|








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


배열 원소의 index를 찾아야 해서 idx를 쓴다는 게 오타를 내서 inx를 썼었는데, 전화위복으로 그 변수를 다시 쓸 수 있었던 문제. 방금 전 상황을 다시 생각해도 신기하다.

찾는 원소가 배열에 없을 시 0을 출력해야 하나, 이 경우 idx=0인 경우와 구분이 안 될 수 있다는 문제가 있었다. 이걸 코드상으로 어떻게 구현하는지가 최대 난관이었다. 실제로 다른 부분들은 다 별 문제없이 구현을 완료한 상황이었기에.

고민하다가 inx라는, 잘못 설정했던 변수가 눈에 들어왔고, '저걸 일종의 flag 변수로 쓴다면 어떨까?' 라는 생각이 번쩍 들었다.

- 찐으로 찾는 원소가 없다 -> inx = -1
- 찾는 원소가 있다 -> inx = 1 (변수값 변경)
- 이후 inx의 값에 따라 0을 출력할지, idx의 값을 출력할지 결정

이렇게 정해 놓고 코드를 테스트해 보니 너무 잘 돌아갔고, 제출하니 그대로 정답 처리되었다. 참 신기하다. 이렇게도 문제가 해결이 될 수 있구나. 
