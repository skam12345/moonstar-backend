sqlList = {
    'check_id': '''
        SELECT COUNT(user_id) 
        FROM user_table
        WHERE user_id = %s
    ''',
    'check_nick': '''
        SELECT COUNT(user_nickname)
        FROM user_table
        WHERE user_nickname = %s
    ''',
    'check_email': '''
        SELECT COUNT(user_email)
        FROM user_table
        WHERE user_email = %s
    ''',
    'sign_up': '''
        INSERT INTO user_table(
        user_id, 
        user_pwd, 
        user_nickname, 
        user_email, 
        user_question, 
        user_answer) VALUES(
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
    ''',
    "login": '''
        SELECT user_id, user_nickname, user_profile
        FROM user_table
        WHERE user_id = %s and user_pwd = %s
    ''',
    "gachya": '''
        SELECT orderNo, name, percentage, star
        FROM avatar_list
        WHERE a_type = %s
        ORDER BY percentage DESC
        ,star ASC
    ''',
    "extract":  '''
        SELECT name, star
        FROM avatar_list
        WHERE orderNo = %s
    '''
}