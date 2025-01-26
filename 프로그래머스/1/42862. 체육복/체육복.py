def solution(n, lost, reserve):
    # 중복 제거: reserve에 있고 lost에도 있으면 제외
    reserve_af = set(reserve) - set(lost)  # reserve에 있지만 lost에 없는 학생들
    lost_af = set(lost) - set(reserve)  # lost에 있지만 reserve에 없는 학생들

    for r in reserve_af:
        if r - 1 in lost_af:
            lost_af.remove(r - 1)  # 앞번호 학생에게 빌려줌
        elif r + 1 in lost_af:
            lost_af.remove(r + 1)  # 뒷번호 학생에게 빌려줌


    # 체육복이 없는 학생 수는 lost 리스트의 길이
    return n - len(lost_af)