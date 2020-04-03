

def try_close_files(*files_streams):
    for file in files_streams:
        try:
            file.close()
        except:
            pass