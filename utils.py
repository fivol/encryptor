
def open_files_decorator(files_replace_dict):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args_with_files = []
            opened_files = []
            for arg_num, arg in enumerate(args):
                if arg_num in files_replace_dict:
                    if not arg and files_replace_dict[arg_num][0]:
                        file = files_replace_dict[arg_num][0]
                    else:
                        file = open(arg, files_replace_dict[arg_num][1])
                        opened_files.append(file)
                    args_with_files.append(file)
                else:
                    args_with_files.append(arg)

            exception = None
            result = None
            try:
                result = func(*args_with_files, **kwargs)
            except Exception as e:
                exception = e

            for file in opened_files:
                file.close()

            if exception:
                raise exception
            return result

        return wrapper
    return decorator
