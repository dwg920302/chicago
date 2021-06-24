from dataclasses import dataclass


@dataclass
class FileDTO:
    context: str
    fname: str
    url: str
    dframe: object

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    @property
    def dframe(self):
        return self._dframe

    @dframe.setter
    def dframe(self, dframe):
        self._dframe = dframe

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url
