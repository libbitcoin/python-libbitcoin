typedef struct bc_chain_state_t bc_chain_state_t;

void bc_destroy_chain_state(bc_chain_state_t* self);

/// Properties.
size_t bc_chain_state__height(const bc_chain_state_t* self);
uint32_t bc_chain_state__enabled_forks(const bc_chain_state_t* self);
uint32_t bc_chain_state__minimum_version(const bc_chain_state_t* self);
uint32_t bc_chain_state__median_time_past(const bc_chain_state_t* self);
uint32_t bc_chain_state__work_required(const bc_chain_state_t* self);

/// Construction with zero height or any empty array causes invalid state.
bool bc_chain_state__is_valid(const bc_chain_state_t* self);

/// Determine if the fork is set for this block.
bool bc_chain_state__is_enabled(const bc_chain_state_t* self,
    bc_rule_fork_t fork);

/// Determine if this block hash fails a checkpoint at this height.
bool bc_chain_state__is_checkpoint_conflict(
    const bc_chain_state_t* self, const bc_hash_digest_t* hash);

/// This block height is less than or equal to that of the top checkpoint.
bool bc_chain_state__is_under_checkpoint(const bc_chain_state_t* self);
