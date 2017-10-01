class DoubleRatchetConfig(object):
    def __init__(self, symmetric_key_ratchet, aead, message_key_store_max):
        self.__symmetric_key_ratchet = symmetric_key_ratchet
        self.__aead = aead
        self.__message_key_store_max = message_key_store_max

    @property
    def skr(self):
        return self.__symmetric_key_ratchet

    @property
    def aead(self):
        return self.__aead

    @property
    def mk_store_max(self):
        return self.__message_key_store_max

class DHRatchetConfig(object):
    def __init__(self, root_chain, key_quad_class, other_pub = None):
        self.__root_chain = root_chain
        self.__key_quad_class = key_quad_class
        self.__other_pub = other_pub

    @property
    def root_chain(self):
        return self.__root_chain

    @property
    def KeyQuad(self):
        return self.__key_quad_class

    @property
    def other_pub(self):
        return self.__other_pub

class Config(object):
    def __init__(self, double_ratchet_config, dh_ratchet_config):
        self.__double_ratchet_config = double_ratchet_config
        self.__dh_ratchet_config = dh_ratchet_config

    @property
    def dr_config(self):
        return self.__double_ratchet_config

    @property
    def dh_config(self):
        return self.__dh_ratchet_config
