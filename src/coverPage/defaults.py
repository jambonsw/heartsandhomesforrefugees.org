"""Settings used by Index page of HHR"""
from mezzanine.conf import register_setting

register_setting(
    name="intro",
    label="Introduction to HHR",
    description="Introduction to appear on the home page of the site",
    editable=True,
    default=(
        "Hearts and Homes for Refugees is a nonprofit grassroots"
        " humanitarian organization that works with U.S. State"
        " Department-designated agencies to welcome, assist and"
        " advocate for refugees. We are a growing network of volunteers"
        " — families, neighbors, community organizations, and people of"
        " goodwill from all faith and civic groups — committed to"
        " offering refugees hope and opportunity. In keeping with"
        " time-honored American tradition, we offer refuge to those"
        " fleeing violence and persecution and identify and tap"
        " resources that aid refugee populations. We use our expertise"
        " and experience to educate, inspire and equip others to"
        " welcome the stranger."
    ),
)

register_setting(
    name="disclaimer",
    label="HHR Disclaimer",
    description="Disclaimer to appear after HHR Intro on the home page of the site",
    editable=True,
    default=(
        "HHR is an apolitical initiative that welcomes concerned"
        " individuals from every religious, faith-based and civic"
        " background and does not represent any specific faith or"
        " community group except its own."
    ),
)
