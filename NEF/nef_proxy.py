import pycurl
from io import BytesIO
from typing import Dict


def override(f):
    """decorator for override hint"""
    return f

class SbiMapping:
    """"""
    sbi_mapping = {'NRF': 16000, 'AMF': 16001, 'SMF': 16002,
                   'PCF': 16003, 'UDM': 16004, 'UDR': 16005,
                   'NSSF': 16006, 'AUSF': 16007, 'BSF': 16008}
    @classmethod
    def nf_to_sbi_port(cls, nf):
        try:
            return cls.sbi_mapping.get(nf.upper())
        except KeyError:
            print(f'Invalid key: {nf}')


class PycurlClient(object):
    """
    Singleton class that acts as a proxy between SBI interfaces of NFs in 5GS and quasi-NEF

    Attributes
    ----------
    __instance: PycurlClient
        a handle to PycurlClient object
    __libcurl_acceptable: dict
        a mapping of integer codes onto libcurl options for verification of pycurl attributes

    Methods
    -------

    """

    __instance = None
    __libcurl_acceptable: Dict[int, str] = {v: k for k, v in pycurl.__dict__.items()
                                            if not k.startswith('__') and k.isupper()}

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PycurlClient, cls).__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        self._curl_options: Dict[str, str] = dict()
        self._proxy = pycurl.Curl()

    def setopt(self, option, value):
        """Sets an option of Curl client"""

        assert option in self.__libcurl_acceptable, f'invalid option to setopt: {option}'
        try:
            self._proxy.setopt(option, value)
            self._curl_options.update({self.__libcurl_acceptable.get(option): value})
        except TypeError as err:
            print(f'invalid value: {value} to option: {option}; {err}')
        except pycurl.error as err:
            print(f'libcurl rejected option || value: {err}')

    def delopt(self, option):
        """Unsets an option of Curl client"""

        assert option in self.__libcurl_acceptable, f'invalid option to unsetopt: {option}'
        try:
            self._curl_options.pop(option)
            self._proxy.unsetopt(option)
        except KeyError:
            print(f'option valid, but unset')

    def get_targeted_nf(self):
        pass

    def get_url(self):
        pass

