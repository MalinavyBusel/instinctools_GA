import json
import multiprocessing as mp
import concurrent.futures as cf

from calc_processing.config import settings

oper_dict = settings.oper_dict
opers_list = list(oper_dict.keys())
opers = json.dumps(opers_list, indent=0)

executor = cf.ProcessPoolExecutor(max_workers=4)


# Variant 1 -------------------------------------------------------
def calculate_1(expression: str, pipe: mp.Pipe):
    try:
        oper, val1, val2 = expression.strip().split(' ')
        res = oper_dict[oper](int(val1), int(val2))
        return_val = str(round(res, 2)) + ':::'
    except ZeroDivisionError:
        return_val = ':::You are trying to divide by zero.'
    except KeyError:
        return_val = ':::There is no such operation.'
    except ValueError:
        return_val = ':::Invalid arguments or their types.'
    pipe.send(return_val)
    return None


def calculate_in_proc(expression: str):
    recv_conn, sending_conn = mp.Pipe()
    p = mp.Process(target=calculate_1, args=(expression, sending_conn))
    p.start()
    p.join()
    result_str = recv_conn.recv()
    return result_str


# Variant 2 -------------------------------------------------------
def calculate_2(expression: str):
    try:
        oper, val1, val2 = expression.strip().split(' ')
        res = oper_dict[oper](int(val1), int(val2))
        return str(round(res, 2)) + ':::'
    except ZeroDivisionError:
        return ':::You are trying to divide by zero.'
    except KeyError:
        return ':::There is no such operation.'
    except ValueError:
        return ':::Invalid arguments or their types.'


def calculate_with_process_pool_exec(expression: str, socket_conn):
    # The initializing of executor is moved out of function to line 11
    pool_process = executor.submit(calculate_2, expression)
    pool_process.conn = socket_conn
    pool_process.add_done_callback(socket_callback)
    return pool_process.result()


def socket_callback(future: cf.Future):
    future.conn.sendall(future.result().encode(encoding='utf-8'))
    return None
