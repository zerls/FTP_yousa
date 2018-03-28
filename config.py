class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    CURRENT_DIR = 'F:/'


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
