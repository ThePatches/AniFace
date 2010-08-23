# Class to resolve file transfer issues
class FileIterWrapper(object):
  def __init__(self, flo, chunk_size = 1024**2):
    self.flo = flo
    self.chunk_size = chunk_size

  def next(self):
    data = self.flo.read(self.chunk_size)
    if data:
      return data
    else:
      raise StopIteration

  def __iter__(self):
    return self

MIME_HASH = {'mkv' : 'video/x-mastroka', 'avi' : 'video/x-msvideo', 'mov' : 'video/quicktime'}
BAD_TYPE = 'BAD TYPE!'

def GetMime(fname):
    ext = fname.split('.')

    if len(ext) > 1:
      try:
        return MIME_HASH[ext[1]]
      except KeyError:
        return BAD_TYPE
    else:
        return BAD_TYPE


