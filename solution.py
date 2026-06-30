def count_base7_ends_with_1(numbers):
    count = 0
    for num in numbers:
        # Остаток от деления на 7 равен последней цифре в системе счисления с основанием 7
        if num % 7 == 1:
            count += 1
    return count


def main():
    n = int(input().strip())
    
    numbers = []
    for _ in range(n):
        numbers.append(int(input().strip()))
    
    result = count_base7_ends_with_1(numbers)
    
    if result == 0:
        print("NO")
    else:
        print(result)


if __name__ == "__main__":
    main()
