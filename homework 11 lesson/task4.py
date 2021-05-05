def str_change(input_str: str, word_to_change: str, subs: str, count_subs: int):
    input_str.replace(word_to_change, subs, count_subs)
    return input_str.replace(word_to_change, subs, count_subs)


print(str_change('let us make some changes changes', 'changes', 'you', 2))
