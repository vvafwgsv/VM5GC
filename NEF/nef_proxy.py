

class SbiMapping():
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

