from .util.pattern import Pattern


pattern = Pattern(r"^{}{}{}$".format(
    Pattern.whoIs,
    Pattern.relation,
    Pattern.nominal,
))