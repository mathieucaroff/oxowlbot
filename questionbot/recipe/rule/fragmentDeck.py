from .fragment import ActiveFragment, ConstantFragment


# Who is a cat?
#
# :1_Lwho_Upron_Nx_Rroot_FPronType=Int_==.
# :2_Lbe_Uaux_N1_Rcop_FMood=Ind_FNumber=Sing_FPerson=3_FTense=Pres_FVerbForm=Fin_<.
# :3_La_Udet_Nx_Rdet_FDefinite=Ind_FPronType=Art_>.
# :4_Lcat_Unoun_N1_Rnsubj_FNumber=Sing_<=. :5_L?_Upunct_Nx_Rpunct_F_<--



whoIs = ConstantFragment(overview=r"<Lwh(?:o|ich),Upron>~<Lbe,Uaux>")
# whoIs: who is
# whoIs: which were


relation = ActiveFragment(
    overview=r" +(?:__ +)*((?:{detail} +<Uadp,Rcase>)+)",
    detail=r"<!!(?:Unoun|Hpast)>",
)
# relation: friend of
# relation: married with


nominal = ActiveFragment(
    overview=r"((?:~{detail})+)",
    detail=r"<!!(?:Upropn|Unoun),(?:Rcompound|Rnmod|Rnsubj)>",
)
# nominal: individual: Cadance
# nominal: individual: Twilight Sparkle
# nominal: class: Kirin
# nominal: class: Earth Pony
