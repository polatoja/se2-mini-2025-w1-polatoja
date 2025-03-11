import re

def func(input_str):
    delimiters = {",", "\n"}
    
    # Check for custom delimiter
    if input_str.startswith("//"):
        delimiter_section, input_str = input_str.split("\n", 1)
        if "[" in delimiter_section:  # Multiple character delimiters
            custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            delimiters.update(custom_delimiters)
        else:  # Single character delimiter
            delimiters.add(delimiter_section[2])

    # Replace all delimiters with ","
    for d in delimiters:
        input_str = input_str.replace(d, ",")

    # Split numbers
    parts = input_str.split(",")

    # Convert to integers while filtering out empty values
    numbers = []
    for num in parts:
        num = num.strip()
        if num:  # Ignore empty values
            if "-" in num:
                raise ValueError("Negative numbers are not allowed")
            num = int(num)
            if num <= 1000:  # Ignore numbers > 1000
                numbers.append(num)

    return sum(numbers) if numbers else 0
