from src.result import Result


def output_formatter(results):
    result_list = []
    for result in results:
        result_formatted = str(result.query_id)
        result_formatted += " " + result.iteration
        result_formatted += " " + result.doc_number
        result_formatted += " " + str(result.rank)
        result_formatted += " " + str(result.score)
        result_formatted += " " + result.system
        result_list.append(result_formatted)
    return result_list


if __name__ =='__main__':
    result1 = Result(10, "Q0", "docNumber1", 1, 2.5)
    result2 = Result(10, "Q0", "docNumber2", 2, 2.2)
    test_results = [result1, result2]
    output_formatter(test_results)
