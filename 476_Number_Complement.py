class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0

        to_double_res = ""
        len_to_double_res = 0
        to_ten_res = 0
        to_ten_step = 0
        calculate_to_double = True

        while True:
            if num == 0 and calculate_to_double:
                len_to_double_res = len(to_double_res) - 1
                to_double_res = to_double_res[::-1]
                calculate_to_double = False

            if num > 0 and calculate_to_double:
                to_double_res += "0" if str(num % 2) == "1" else "1"
                num = num // 2

            if not calculate_to_double:
                to_ten_res += int(to_double_res[to_ten_step]) * (2 ** len_to_double_res)
                len_to_double_res -= 1
                to_ten_step += 1

                if to_ten_step == len(to_double_res):
                    break

        return to_ten_res


s = Solution()
print(s.findComplement(2))
