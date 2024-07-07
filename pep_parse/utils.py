import re


pattern = r'PEP \d+ – (?P<name>.*)'


def make_status(status, type_):
    if status == 'Draft':
        status_pep = ''
    else:
        try:
            status_pep = status[0]
        except Exception:
            status_pep = ''
    try:
        type_pep = type_[0]
    except Exception:
        type_pep = ''
    return type_pep + status_pep


def make_name(h1):
    result = ''
    for text in h1.css('::text').getall():
        result += text
    name_match = re.search(pattern, result)
    return name_match.group(1)
