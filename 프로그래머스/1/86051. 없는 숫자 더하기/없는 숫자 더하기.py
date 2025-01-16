def solution(numbers):
    missing_numbers = filter(lambda x: x not in numbers, range(10))
    answer = sum(missing_numbers)
    return answer
