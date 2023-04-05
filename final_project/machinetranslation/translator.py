"""
This Python file instantiates all required packages for the
IBM Language Translator service.
"""

import os
# import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version='2018-05-01',
                                           authenticator=authenticator)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """ This function will translate English to French """
    text_to_translate = language_translator.translate(text=english_text,
                                                      model_id='en-fr').get_result()
    french_text = text_to_translate['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """ This function will translate French to English """
    text_to_translate = language_translator.translate(text=french_text,
                                                      model_id='fr-en').get_result()
    english_text = text_to_translate['translations'][0]['translation']
    return english_text
