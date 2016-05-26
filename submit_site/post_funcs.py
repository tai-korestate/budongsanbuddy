def upload_file(fil_name):
    with open(string(fil_name),"wb+") as destination:
        for chunk in fil_name.chunk():
            destination.write(chunk)
  
