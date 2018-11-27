from src.result import Result

def output_formatter(results):
    result_list = []
    for result in results:
        result_line = str(result.query_id)
        result_line += " " + result.iteration
        result_line += " " + result.doc_number
        result_line += " " + str(result.rank)
        result_line += " " + str(result.score)
        result_line += " " + result.system
        result_list.append(result_line)
    return result_list

if __name__ =='__main__':
    resultObject1 = Result(10, "Q0", "docNumber1", 1, 2.5)
    resultObject2 = Result(10, "Q0", "docNumber2", 2, 2.2)

    resultObjects = [resultObject1, resultObject2]

    output_formatter(resultObjects)
