import uuid
from django.core.files.storage import FileSystemStorage
import filetype


def upload_files(file , location = ""):

    error = False
    url = ''
    msg=""
    filename = ''
    type = 0

    if file.size<5000000:

        fs= FileSystemStorage()
        f = file.name.split(".")
        format = f[-1:][0]
        file_name = uuid.uuid4().hex[:8]

        filename=fs.save("{}{}.{}".format(location,file_name,format) ,file)
        url=fs.url(filename)

        type = filetype.guess(url[1:])

        if type.mime.startswith("image/"):
            type=1
        else:
            type=2

    else:
        error = True
        msg="خطا شما نمیتوانید بیشتر از 5 مگ آپلود کنید."
    
        
    return url,filename,error,msg,type

