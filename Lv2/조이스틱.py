def solution(name):
    answer = 0
    n = len(name)
    
    # 1. 상하 이동 (알파벳 맞추기)
    for char in name:
        up = ord(char) - ord('A')
        down = ord('Z') - ord(char) + 1
        
        if up < down:
            answer += up
        else:
            answer += down

    # 2. 좌우 이동 (커서 옮기기)
    # 일단 기본값은 '오른쪽으로 끝까지 쭉 가는 경우'로 설정
    min_move = n - 1
    
    for i in range(n):
        # 현재 위치(i) 바로 다음부터 연속된 'A'가 끝나는 지점 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        # 경우 ①: 오른쪽으로 i까지 갔다가 유턴해서 뒤쪽 처리
        go_right_then_left = (i * 2) + (n - next_idx)
        
        # 경우 ②: 처음부터 왼쪽으로 돌아 뒤쪽 먼저 처리 후, 다시 오른쪽 i까지 이동
        go_left_then_right = i + (n - next_idx) * 2
        
        # 오른쪽 쭉 가는 것보다 유턴하는 게 더 효율적이면 최솟값 갱신
        if go_right_then_left < min_move:
            min_move = go_right_then_left
            
        if go_left_then_right < min_move:
            min_move = go_left_then_right
            
    return answer + min_move