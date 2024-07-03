# Project Title: AVL Tree Implementation

## Project Description

This project involves the implementation of an AVL Tree in Python as part of a Data Structures course. The AVL Tree is a self-balancing binary search tree that maintains its balance through rotations during insertions and deletions.

## Repository Structure

- `AVLTree.py`: Contains the source code for the AVL Tree implementation.
- `README.md`: Project overview and instructions.

## Requirements

- **Programming Language**: Python 3.11
- **Libraries**: No external libraries are to be used. The implementation should be based solely on standard Python.

## Implementation Details

The AVL Tree implementation should include the following functionalities:

- **Search**: `search(k)` - Searches for a node with key `k`.
- **Insert**: `insert(k, s)` - Inserts a node with key `k` and value `s`, returns the number of balancing operations performed.
- **Delete**: `delete(x)` - Deletes the node pointed to by `x`, returns the number of balancing operations performed.
- **AVL to Array**: `avl_to_array()` - Converts the AVL tree to a sorted array.
- **Size**: `size()` - Returns the number of nodes in the tree.
- **Split**: `split(x)` - Splits the tree into two AVL trees based on node `x`.
- **Join**: `join(t, k, s)` - Joins the current tree with another tree `t` and a new node with key `k` and value `s`, returns the balancing "cost".
- **Rank**: `rank(x)` - Returns the rank of the node pointed to by `x`.
- **Select**: `select(i)` - Returns the node with rank `i`.
- **Get Root**: `get_root()` - Returns the root node of the tree.
