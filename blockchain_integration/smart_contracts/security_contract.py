pragma solidity ^0.8.0;

contract SecurityContract {
    address private owner;
    mapping (address => bool) public allowedNodes;

    constructor() public {
        owner = msg.sender;
    }

    function addNode(address node) public {
        require(msg.sender == owner, "Only the owner can add nodes");
        allowedNodes[node] = true;
    }

    function removeNode(address node) public {
        require(msg.sender == owner, "Only the owner can remove nodes");
        allowedNodes[node] = false;
    }

    function checkNode(address node) public view returns (bool) {
        return allowedNodes[node];
    }
}
