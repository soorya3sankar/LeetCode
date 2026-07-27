int findComplement(int num) {
    unsigned int helper = 1;
    while (helper < num) {
        helper = (helper << 1) | 1;
    }
    return num ^ helper;
}
