def solution(phone_book):
    phone_book.sort()
    LEN_PB = len(phone_book)
    for i in range(LEN_PB - 1):
        if phone_book[i + 1].startswith(phone_book[i]): return False
        # for j in range(i + 1, LEN_PB):
        #     if phone_book[j].startswith(phone_book[i]):
        #         return False
    return True

# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
# phone_book = ["12","123","1235","567","88"]
# print(solution(phone_book))
