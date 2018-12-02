from src.result import Result


def format_result(entry):
    formatted = f'{entry.query_id}'
    formatted += f' {entry.iteration}'
    formatted += f' {entry.doc_number}'
    formatted += f' {entry.rank}'
    formatted += f' {entry.score}'
    formatted += f' {entry.system}'
    return formatted


def result_writer(results, file):
    open(file, 'a+').write('\n'.join([format_result(entry) for entry in results]) + '\n')


if __name__ == '__main__':
    result1 = Result(10, 'docNumber1', 1, 2.5)
    result2 = Result(10, 'docNumber2', 2, 2.2)
    for result in [result1, result2]:
        print(format_result(result))
