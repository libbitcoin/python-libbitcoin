typedef struct bc_points_info_t bc_points_info_t;
typedef struct bc_output_info_list_t bc_output_info_list_t;

void bc_select_outputs__select(bc_points_info_t* out,
    const bc_output_info_list_t* unspent, uint64_t minimum_value);

