import re

REFERENCE_YEAR = 2025

TIME_KEYWORDS = {
    '과거': [
        '어제', '지난 주', '지난 달', '작년', '재작년', '이전에', '그때', '그 시절',
        '예전', '예전에', '옛날', '한때', '과거에', '하루 전', '일주일 전', '몇 년 전',
        '과거', '예전부터', '한참 전', '얼마 전', '그 당시', '예전 같았으면', '어린 시절에',
        '작년인가 재작년쯤', '몇 해 전'
    ],
    '현재': [
        '지금', '현재', '오늘', '요즘', '요새', '방금', '막', '최근', '당장',
        '계속해서', '금일', '현시점', '현황', '올해', '금방', '요즘은', '지금도',
        '여전히', '지금 이 순간', '현재 기준으로', '요즘 같은 시기엔'
    ],
    '미래': [
        '내일', '모레', '글피', '다음주', '다음달', '다음해', '곧', '앞으로', '훗날',
        '조만간', '추후', '장래에', '향후', '차후', '미래', '장차', '예측컨대', '머지않아',
        '언젠가는', '몇 년 후쯤', '앞으로는', '나중에', '가까운 시일 내에', '내년'
    ]
}

SPECIAL_PAST_List = {
    '재작년': '2023년',
    '작년': '2024년',
    '지난 해': '2024년',
    '삼년 전': '2022년',
    '사년 전': '2021년',
    '오년 전': '2020년',
    '작년인가': '2024년',
    '재작년쯤': '2023년'
}

YEAR_PATTERN = re.compile(r'(\d{4})년')

def classify_year(year_str: str) -> str:
    year = int(year_str)
    if year < REFERENCE_YEAR:
        return '과거'
    elif year == REFERENCE_YEAR:
        return '현재'
    else:
        return '미래'

def classify_time_point(sentence: str) -> tuple[str, list[str], list[str]]:
    keywords = []
    years = []
    time_class = None

    for special_expr in SPECIAL_PAST_List.keys():
        if special_expr in sentence:
            keywords.append(special_expr)
            time_class = '과거'

    for category, expressions in TIME_KEYWORDS.items():
        for expr in expressions:
            if expr in sentence:
                if expr not in SPECIAL_PAST_List:
                    keywords.append(expr)
                    if not time_class or (time_class == '미래' and category == '과거'):
                        time_class = category

    found_years = YEAR_PATTERN.findall(sentence)
    if found_years:
        years.extend(found_years)
        year_based_class = classify_year(found_years[0])
        if not time_class:
            time_class = year_based_class
        elif time_class != year_based_class:
            time_class = year_based_class

    return time_class, keywords, years

def refine_sentence(sentence: str) -> str:
    time_class, keywords, years = classify_time_point(sentence)

    if not time_class:
        return sentence

    refined = sentence

    for special_expr, year_str in SPECIAL_PAST_List.items():
        if special_expr in refined:
            refined = refined.replace(special_expr, year_str)

    if time_class == '과거':
        past_non_special = [kw for kw in keywords if kw not in SPECIAL_PAST_List]
        if past_non_special:
            for kw in past_non_special:
                refined = refined.replace(kw, '')
            if not refined.startswith('과거'):
                refined = '과거 ' + refined

    elif time_class == '현재':
        for kw in keywords:
            refined = refined.replace(kw, '')

    elif time_class == '미래':
        if keywords and not years:
            for kw in keywords:
                refined = refined.replace(kw, '')
            refined = '앞으로의 ' + refined
        else:
            for kw in keywords:
                refined = refined.replace(kw, '')

    refined = re.sub(r'\s+', ' ', refined).strip()

    return refined

def run_time_cleaner():
    print("시간 표현 정제 시스템 (종료하려면 'exit' 입력)")
    while True:
        user_input = input("\n[원래 질문]: ").strip()
        if user_input.lower() == 'exit':
            print("프로그램을 종료합니다.")
            break
        refined = refine_sentence(user_input)
        print(f"[정제된 질문]: {refined}")

if __name__ == "__main__":
    run_time_cleaner()
