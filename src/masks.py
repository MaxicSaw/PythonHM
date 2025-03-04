def get_mask_card_number(card_number: str) -> str:
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def get_mask_account(account_number: str) -> str:
    return f"**{account_number[-4:]}"


real_card_number = "7000792289606361"
real_account = "73654108430135874305"

if len(real_card_number) != 16:
    print("Номер карты должен содержать ровно 16 цифр")
else:
    print(f"Номер карты: {get_mask_card_number(real_card_number)}")

if len(real_account) < 6:
    print("Номер счёта должен содержать минимално 6 цифр или более")
else:
    print(f"Номер счёта: {get_mask_account(real_account)}")
