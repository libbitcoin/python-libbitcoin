typedef enum bc_rule_fork_t
{
    bc_rule_fork__no_rules = 0,

    /// allow minimum difficulty blocks (hard fork, testnet)
    bc_rule_fork__easy_blocks = 1,

    /// pay-to-script-hash enabled (soft fork)
    bc_rule_fork__bip16_rule = 2,

    /// no duplicated unspent transaction ids (hard fork, necessary)
    bc_rule_fork__bip30_rule = 4,

    /// coinbase must include height (soft fork)
    bc_rule_fork__bip34_rule = 8,

    /// strict DER signatures required (soft fork)
    bc_rule_fork__bip66_rule = 16,

    /// nop2 becomes check locktime verify (soft fork)
    bc_rule_fork__bip65_rule = 32,

    /// assume hash collisions cannot happen (hard fork, invalid)
    bc_rule_fork__allowed_duplicates = 64,

    /// hard code activation heights (hard fork, unnecessary)
    bc_rule_fork__deep_freeze = 128,

    /// rules that require bip34 style activation
    bc_rule_fork__activations = 56,

    /// the valid set of changes to the original rule set
    bc_rule_fork__consensus = 62,

    bc_rule_fork__all_rules = 0xffffffff

} bc_rule_fork_t;

