typedef struct bc_points_info_t bc_points_info_t;
typedef struct bc_output_info_list_t bc_output_info_list_t;

void bc_select_outputs__select(bc_points_info_t* out,
    const bc_output_info_list_t* unspent, uint64_t minimum_value);

void bc_select_outputs__select_Alg(bc_points_info_t* out,
    const bc_output_info_list_t* unspent, uint64_t minimum_value,
    bc_select_outputs__algorithm_t option);

