from libbitcoin.bc.config import ffi, lib

class DictionaryIterator:

    def __init__(self, parent):
        self._parent = parent
        self._index = 0

    def __next__(self):
        if self._index >= len(self._parent):
            raise StopIteration
        result = self._parent[self._index]
        self._index += 1
        return result

class DictionaryBase:

    def __init__(self, obj, language_code):
        self._obj = obj
        self._language_code = language_code

    def __del__(self):
        lib.bc_destroy_dictionary(self._obj)

    def __len__(self):
        return lib.bc_dictionary_size()

    def __getitem__(self, pos):
        return str(ffi.string(lib.bc_dictionary__const_at(self._obj, pos)),
                   "utf-8")

    def __iter__(self):
        return DictionaryIterator(self)

    def __repr__(self):
        return "<bc_dictionary language=%s>" % self._language_code

class Dictionary(DictionaryBase):

    en = DictionaryBase(lib.bc_dictionary_en(), "en")
    es = DictionaryBase(lib.bc_dictionary_es(), "es")
    ja = DictionaryBase(lib.bc_dictionary_ja(), "ja")
    zh_Hans = DictionaryBase(lib.bc_dictionary_zh_Hans(), "zh_Hans")
    zh_Hant = DictionaryBase(lib.bc_dictionary_zh_Hant(), "zh_Hant")

    @staticmethod
    def get(language_code):
        return getattr(Dictionary, language_code)

