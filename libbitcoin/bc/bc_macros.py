def byte_array(typename):
    return """
    size_t bc_TYPENAME_size();
    typedef struct bc_TYPENAME_t bc_TYPENAME_t;
    bc_TYPENAME_t* bc_create_TYPENAME();
    bc_TYPENAME_t* bc_create_TYPENAME_Data(const uint8_t* data);
    bc_TYPENAME_t* bc_create_TYPENAME_Base16(
        const char* encoded_bytes);
    void bc_destroy_TYPENAME(bc_TYPENAME_t* self);
    uint8_t* bc_TYPENAME__data(bc_TYPENAME_t* self);
    const uint8_t* bc_TYPENAME__cdata(const bc_TYPENAME_t* self);
    bc_string_t* bc_TYPENAME__encode_base16(
        const bc_TYPENAME_t* self);
    """.replace("TYPENAME", typename)

def hash_type(hashtype):
    return """
    typedef struct bc_HASHTYPE_t bc_HASHTYPE_t;
    bc_HASHTYPE_t* bc_create_HASHTYPE();
    bc_HASHTYPE_t* bc_create_HASHTYPE_Array(const uint8_t* data);
    void bc_destroy_HASHTYPE(bc_HASHTYPE_t* self);
    uint8_t* bc_HASHTYPE__data(bc_HASHTYPE_t* self);
    const uint8_t* bc_HASHTYPE__cdata(const bc_HASHTYPE_t* self);
    bc_string_t* bc_HASHTYPE__encode_base16(
        const bc_HASHTYPE_t* self);
    bool bc_HASHTYPE__equals(const bc_HASHTYPE_t* self,
        const bc_HASHTYPE_t* other);
    """.replace("HASHTYPE", hashtype)

def vector(typename, itemtype):
    return """
    typedef struct bc_TYPENAME_t bc_TYPENAME_t;
    bc_TYPENAME_t* bc_create_TYPENAME();
    void bc_destroy_TYPENAME(bc_TYPENAME_t* self);
    /*****Do not delete the objects returned by these accessors.*****/
    ITEMTYPE* bc_TYPENAME__at(bc_TYPENAME_t* self, size_t pos);
    const ITEMTYPE* bc_TYPENAME__const_at(const bc_TYPENAME_t* self,
        size_t pos);
    /****************************************************************/
    size_t bc_TYPENAME__size(const bc_TYPENAME_t* self);
    bool bc_TYPENAME__empty(const bc_TYPENAME_t* self);
    void bc_TYPENAME__clear(bc_TYPENAME_t* self);
    void bc_TYPENAME__erase(bc_TYPENAME_t* self, size_t pos);
    void bc_TYPENAME__insert(bc_TYPENAME_t* self,
        size_t pos, ITEMTYPE* obj);
    void bc_TYPENAME__push_back(bc_TYPENAME_t* self, ITEMTYPE* obj);
    /* Methods that don't try to consume the passed pointer, but
       the semantics remain the same as the normal push_back() */
    void bc_TYPENAME__insert_consume(bc_TYPENAME_t* self,
        size_t pos, ITEMTYPE** obj);
    void bc_TYPENAME__push_back_consume(bc_TYPENAME_t* self,
        ITEMTYPE** obj);
    void bc_TYPENAME__resize(bc_TYPENAME_t* self, size_t count);
    """.replace("TYPENAME", typename).replace("ITEMTYPE", itemtype)

