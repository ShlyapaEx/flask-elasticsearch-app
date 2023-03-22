def camel_to_snake(text: str) -> str:
    """
    Функция camel_to_snake преобразует строку из camelCase в snake_case.
    Например, 'camelCase' становится 'camel_case'.

    ::param text: str: Строка, которую мы хотим преобразовать
    :return: Строка в snake_case
    """
    return ''.join(['_'+c.lower() if c.isupper() else c for c in text]).lstrip('_')


def spaces_before_capital_letters(text: str) -> str:
    """
    Функция spaces_before_capital_letters принимает строку 
    и возвращает ту же строку с пробелами перед заглавными буквами.
    Например, "HelloWorld" превратится в "Hello World".

    :param text: str: Строка, которую преобразуем
    :return: Строка с пробелами
    """
    return ''.join(' ' + char if char.isupper() else char.strip()
                   for char in text).strip()
