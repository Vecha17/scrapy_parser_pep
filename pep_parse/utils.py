import re


pattern = r'PEP \d+ – (?P<name>.*)'


def make_status(status, type):
    if status == 'Draft':
        status_pep = ''
    else:
        status_pep = status[0]
    type_pep = type[0]
    return type_pep + status_pep


def make_name(h1):
    result = ''
    for text in h1.css('::text').getall():
        result += text
    name_match = re.search(pattern, result)
    return name_match.group(1)
