from enum import Enum
from libbitcoin.bc.config import lib

class RuleFork(Enum):

    no_rules = lib.bc_rule_fork__no_rules
    easy_blocks = lib.bc_rule_fork__easy_blocks
    bip16_rule = lib.bc_rule_fork__bip16_rule
    bip30_rule = lib.bc_rule_fork__bip30_rule
    bip34_rule = lib.bc_rule_fork__bip34_rule
    bip66_rule = lib.bc_rule_fork__bip66_rule
    bip65_rule = lib.bc_rule_fork__bip65_rule
    allowed_duplicates = lib.bc_rule_fork__allowed_duplicates
    deep_freeze = lib.bc_rule_fork__deep_freeze
    activations = lib.bc_rule_fork__activations
    consensus = lib.bc_rule_fork__consensus
    all_rules = lib.bc_rule_fork__all_rules

