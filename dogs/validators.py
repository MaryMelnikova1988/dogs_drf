from rest_framework import serializers

SCAM_WORDS = ['продам', 'крипта', 'биржа']


def validator_scam_words(value):
    if set(value.lower().split()) & set(SCAM_WORDS):
        raise serializers.ValidationError("Использованы запрещенные слова!")
