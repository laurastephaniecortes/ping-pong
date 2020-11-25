

class DevConfig(object):
    DEBUG = True

class ProdConfig(object):
    DEBUG = False

app_configuration = {
    'development': DevConfig,
    'production': ProdConfig,
}