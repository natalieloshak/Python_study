def delete_html_tags_and_hashes(input_file="draft.html", output_file="cleaned.txt"):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    result = ""
    inside_tag = False

    for char in text:
        if char == "<":
            inside_tag = True
        elif char == ">":
            inside_tag = False
        elif not inside_tag:
            result += char

    lines = result.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if line:
            line = line.replace("#", "")
            cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    with open(input_file, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    print(
        f"✅ Файл '{input_file}' оновлено, результат також записано у '{output_file}'"
    )


delete_html_tags_and_hashes()
