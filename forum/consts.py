class Theme:
    news = 'News'
    chars = 'Characters'
    eps = 'Episodes'
    refs = 'References'
    prod = 'Production'
    bugs = 'bugs'

    THEME_CHOICES = (
        (news, "News"),
        (chars, "Characters"),
        (eps, "Episodes"),
        (refs, "References"),
        (prod, "Production"),
        (bugs, "Bugs"),
    )


class Genders:
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("Y", "Youkai"),
        ("B", "Beast"),
        ("H", "Helicopter Apache"),
    )