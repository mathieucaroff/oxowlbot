from .fragment import ActiveFragment, ConstantFragment

whoIs = ConstantFragment(overview=r"<Lwh(?:o|ich),Upron>~<Lbe,Uaux>")
# whoIs: who is
# whoIs: which were


relation = ActiveFragment(
    overview=r"((?:~<(?:Unoun|Hpast)> +<Uadp_Rcase>)+)",
    detail=r"<!!(?:Unoun|Hpast)>",
)
# relation: friend of
# relation: married with


nominal = ActiveFragment(
    overview=r"((?:~<Upropn,(?:Rcompound|Rnmod)>)+)",
    detail=r"<!!Upropn,(?:Rcompound|Rnmod)>",
)
# nominal: individual: Cadance
# nominal: individual: Twilight Sparkle
# nominal: class: Kirin
# nominal: class: Earth Pony
