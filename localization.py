import os
import json
from functools import reduce


class Localization:
    def __init__(self, path):
        self.locale_path = "./locales"
        self.locales = {}
        self.current_locale = ""

    def set_locales_directory(self, path):
        self.locale_path = "./{}".format(path)
        self.locales = {}
        self.current_locale = "en"

        for filename in os.listdir(self.locale_path):
            with open(os.path.join(self.locale_path, filename), "r") as jsonFile:
                locale_name = filename.replace(".json", "")
                self.locales[locale_name] = json.load(jsonFile)
                jsonFile.close()

    def set_locale(self, locale_name):
        assert locale_name in self.locales.keys(), "There is no locale [{}] in folder [{}]".format(locale_name, self.locale_path)
        self.current_locale = locale_name

    def get(self, key, locale):
        assert locale != "", "There is no set locale"
        assert (type(locale) == str), "You passed locale in wrong type: {}. It should be str".format(locale)
        assert locale in self.locales.keys(), "There is no locale [{}] in folder [{}]".format(locale, self.locale_path)

        path = key.split(".")
        result = reduce(lambda obj, obj_key: obj.get(obj_key), path, self.locales[locale])

        assert type(result) is str, "The key should lead to the final translation, not to the group"
        return result


localization = Localization("locales")


def _(text, custom_locale=None):
    locale = custom_locale if custom_locale else localization.current_locale
    return localization.get(text, locale)
