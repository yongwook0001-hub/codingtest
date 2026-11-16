import math

def solution(signals):
    cycles = [g + y + r for g, y, r in signals]
    
    # 2. 모든 신호등의 패턴이 다시 처음으로 리셋되는 시간(최소공배수) 구하기
    max_time = math.lcm(*cycles)
    
    # 3. 1초부터 max_time초까지 1초씩 확인
    for t in range(1, max_time + 1):
        # 현재 시각 t에 "모든" 신호등이 노란불인지 확인
        if all(g <= (t - 1) % (g + y + r) < g + y for g, y, r in signals):
            return t  # 모두 노란불이 되는 가장 빠른 시각 반환
            
    # 끝까지 확인했는데 한 번도 겹치지 않았다면 -1 반환
    return -1