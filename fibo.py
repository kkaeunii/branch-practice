def fibo(n):
    """
    피보나치 수열의 n번째 수를 반환하는 함수

    Args:
        n(int) : 구하고자 하는 피보나치 수의 위치(0부터 시작)

    Returns:
        int : n번째 피보나치 수
    """
    if n < 0:
        raise ValueError("Input cannot be a negative number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n - 1) + fibo(n - 2)

if __name__ == "__main__":
    print(fibo(4))
