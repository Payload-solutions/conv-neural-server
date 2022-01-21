

ALLOWED_EXTENSIONS = {
    'png',
    'jpg'
}


def allowed_files(filename: str):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower()\
            in ALLOWED_EXTENSIONS