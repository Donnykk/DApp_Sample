// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PaymentContract {
    address private payer;
    address private payee;
    uint256 private amount;

    constructor() {}

    function weixin(
        uint256 amount_to_transfer,
        address payer_add,
        address payee_add
    ) public {
        payer = payer_add;
        payee = payee_add;
        amount = amount_to_transfer;

        require(payer != address(0), "Invalid payer address");
        require(payee != address(0), "Invalid payee address");
        require(amount > 0, "Amount must be greater than zero");
        payable(payee).transfer(amount);
    }

    function check_transaction()
        public
        view
        returns (address, address, uint256)
    {
        return (payer, payee, amount);
    }
    receive() external payable {}
}
