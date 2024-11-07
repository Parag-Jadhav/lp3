// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract BloodBank {
    
    address public owner;

    // Enum for blood types
    enum BloodType { A_POS, A_NEG, B_POS, B_NEG, AB_POS, AB_NEG, O_POS, O_NEG }

    // Structure to hold blood stock information for a specific blood type at a specific location
    struct BloodStock {
        uint256 quantity;
    }

    // Mapping to track blood stocks by location and blood type
    mapping(string => mapping(BloodType => BloodStock)) public bloodStocks;

    // Event to log stock changes
    event StockUpdated(string location, BloodType bloodType, uint256 quantity);

    constructor() {
        owner = msg.sender;
    }

    // Modifier to allow only the owner to execute specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation");
        _;
    }

    // Function to add or update blood stock at a specific location
    function updateBloodStock(string memory location, BloodType bloodType, uint256 quantity) public onlyOwner {
        bloodStocks[location][bloodType].quantity = quantity;
        emit StockUpdated(location, bloodType, quantity);
    }

    // Function to get the blood stock of a specific blood type at a specific location
    function getBloodStock(string memory location, BloodType bloodType) public view returns (uint256) {
        return bloodStocks[location][bloodType].quantity;
    }

    // Function to remove a specified quantity of blood stock from a location
    function removeBloodStock(string memory location, BloodType bloodType, uint256 quantity) public onlyOwner {
        require(bloodStocks[location][bloodType].quantity >= quantity, "Not enough stock available");
        bloodStocks[location][bloodType].quantity -= quantity;
        emit StockUpdated(location, bloodType, bloodStocks[location][bloodType].quantity);
    }
}
