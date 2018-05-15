from dynaconf import settings

print(settings.SECRET)  # noqa
# >>> 'vault_works'


with settings.using_namespace('dev'):
    assert settings.SECRET == 'vault_works_in_dev'
