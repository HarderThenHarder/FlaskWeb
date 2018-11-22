def is_isbn_or_key(q):
    """
    judge the user's input is use ISBN type search or Key type search
    :param q:
    :return:
    """
    q_or_isbn = 'q'
    if len(q) == 13 and q.isdigit():
        q_or_isbn = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        q_or_isbn = 'isbn'
    return q_or_isbn
