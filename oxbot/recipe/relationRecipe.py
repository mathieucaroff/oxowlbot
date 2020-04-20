from typing import Any, List

from .baseRecipe import BaseRecipe
from .pattern import Pattern

":1_Lwho_uPRON_Nx_Rroot_==. :2_Lbe_uAUX_Nx_Rcop_<. :3_LFluttershy_uPROPN_N1_Rnmod:poss_->. :4_L's_uPART_Nx_Rcase_<. :5_Lfriend_uNOUN_N2_Rnsubj_<--. :6_L?_uPUNCT_Nx_Rpunct_<-=."


class RelationRecipe(BaseRecipe):
    def __init__(self):
        whoIs = r"<Lwh(?:o|ich),Upron>~<Lbe,Uaux>"
        # whoIs: who is
        # whoIs: which were
        relation = r"((?:~<(?:Unoun|Hpast)> +<Uadp_Rcase>)+)"
        # relation: friend of
        # relation: married with
        individual = r"((?:~<Upropn,(?:Rcompound|Rnmod)>)+)"
        # individual: Cadance
        # individual: Twilight Sparkle

        pattern = Pattern(r"^{}{}{}$".format(whoIs, relation, individual))

        BaseRecipe.__init__(
            self, [pattern,],
        )

    def query(self) -> str:
        assert self.didMatch
        return ""

    def describe(self) -> str:
        return ""
