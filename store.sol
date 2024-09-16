// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StorageContract {
    uint256 private stored_num;

    function store_m(uint256 num) public {
        stored_num = num;
    }

    function view_m() public view returns (uint256) {
        return stored_num;
    }
}
