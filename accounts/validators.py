from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

ORCID_ID_LENGHT = 16


def validate_orcid_id_lenght(input: str) -> bool:
    if (len(input) != ORCID_ID_LENGHT):
        raise ValidationError(_('ORCID ID has exactly 16 digits.'), )
    elif input.isdecimal() is False:
        raise ValidationError(_('ORCID ID contains only numbers.'), )
    else:
        return True
