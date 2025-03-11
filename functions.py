def func(input_str):
    delimiters = {",", "\n"}

    if input_str.startswith("//"):
        if input_str[2] == "[":
            delimiter_num = input_str.count("[")
            position = 3
            d = 0
            while d < delimiter_num:
                delimiter_end = input_str.find("]")
                if delimiter_end != -1:
                    custom_delimiter = input_str[position:delimiter_end]
                    delimiters.add(custom_delimiter)
                    input_str = input_str[delimiter_end + 1:]
                    print("Custom Delimiter:", custom_delimiter if 'custom_delimiter' in locals() else "None")
                    print("Remaining Input:", input_str)
                    position = 1
                    d += 1
        else:
            custom_delimiter = input_str[2]
            delimiters.add(custom_delimiter)
            input_str = input_str[3:]

    if "-" in input_str:
        raise ValueError("Negative numbers are not allowed")

    if input_str == "":
        return 0

    if input_str.isdigit():
        return int(input_str) if int(input_str) <= 1000 else 0

    for d in delimiters:
        input_str = input_str.replace(d, ",")

    parts = input_str.split(",")

    if all(part.strip().isdigit() for part in parts):
        numbers = [int(num) for num in parts if int(num) <= 1000]
        return sum(numbers)

    return 1
