import exifread


def get_tags(filename):
    f = open(filename, 'rb')
    tags = exifread.process_file(f)
    for k, v in tags.items():
        print('{}, {}'.format(k, v))


get_tags('test.jpg')