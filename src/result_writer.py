from src.result import Result


def format_result(data):
    formatted = str(data.query_id)
    formatted += f' {data.iteration}'
    formatted += f' {data.doc_number}'
    formatted += f' {str(data.rank)}'
    formatted += f' {str(data.score)}'
    formatted += f' {data.system}'
    return formatted


if __name__ == '__main__':
    result1 = Result(10, 'docNumber1', 1, 2.5)
    result2 = Result(10, 'docNumber2', 2, 2.2)
    for result in [result1, result2]:
        print(format_result(result))
