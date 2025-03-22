def format_hex(int_num, length):
    str_len = length // 4
    hex_str = str(hex(int_num)).removeprefix("0x").zfill(str_len)
    return hex_str

try:
    int_input = int(input("Give an integer: "))
except ValueError:
    print("Integer please")
else:
    try:
        hex_len = int(input("Give hexadecimal length (number of bits): "))
    except ValueError:
        print("Integer please")
    else:
        str_res = format_hex(int_input, hex_len)
        print(str_res)
