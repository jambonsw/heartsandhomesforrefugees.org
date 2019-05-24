"""Settings used by Index page of HHR"""
from mezzanine.conf import register_setting

register_setting(
    name="intro",
    label="Introduction to HHR",
    description="Introduction to appear on the home page of the site",
    editable=True,
    default=(
        "Hearts and Homes for Refugees (HHR) is a non-profit grassroots "
        "humanitarian group in Westchester County, New York. Our mission is to "
        "support those U.S. Department of State approved agencies that welcome, "
        "protect and advocate for refugees in our communities. We are a growing "
        "network of volunteers &mdash; families and neighbors, community "
        "organizations, and people of goodwill from all faith and civic groups. We "
        "offer our talents, time, and expertise to identify and utilize resources "
        "that will offer hope and help to refugees, in keeping with the time-honored "
        "American practice of welcoming newcomers. We hope to inspire, educate and "
        "motivate others to do the&nbsp;same.\n\nJoin us to change the outcome for "
        "refugees, one family at&nbsp;a&nbsp;time. "
    ),
)

register_setting(
    name="disclaimer",
    label="HHR Disclaimer",
    description="Disclaimer to appear after HHR Intro on the home page of the site",
    editable=True,
    default=(
        "HHR is an apolitical initiative that welcomes concerned individuals from "
        "every religious, faith-based and civic background and does not represent "
        "any specific faith or community group except its&nbsp;own. "
    ),
)
