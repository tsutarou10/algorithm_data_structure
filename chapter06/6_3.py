def main():
    print("Start Game!")

    left = 20
    right = 36

    while right - left > 1:
        mid = int(left + (right - left) / 2)

        print(f"Is the age less then {mid} ? (yes / no)")

        ans = input()

        if ans == "yes":
            right = mid
        else:
            left = mid
    print(f"The age is {left} !")


main()
