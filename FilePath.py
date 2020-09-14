def check_path(filename):
    try:
        return filename.rindex('/')
    except ValueError:
        return -1

def get_dir(filename):
    file_index = check_path(filename)
    if file_index != -1:
        return filename[0: file_index + 1]
    else:  
        return ""

def get_filename(filename):
    file_index = check_path(filename)
    if file_index != -1:
        return filename[file_index + 1:]
    else:
        return filename


def get_file_type(filename):
    try:
        return filename[filename.rindex(".") + 1:]
    except:
        return ''

    


assert(get_dir("log/cups/access_log") == "log/cups/")
assert(get_dir("log/cups/") == "log/cups/")
assert(get_dir("cups/access_log") == "cups/")
assert(get_dir("access_log") == "")
assert(get_filename("log/cups/access_log") == "access_log")
assert(get_filename("log/cups/") == "")
assert(get_filename("cups/access_log") == "access_log")
assert(get_filename("access_log") == "access_log")
assert(get_file_type("log/cups/access_log") == "")
assert(get_file_type("base/FileHelper.cpp") == "cpp")
assert(get_file_type("base/FileHelper.cpp.bak") == "bak")