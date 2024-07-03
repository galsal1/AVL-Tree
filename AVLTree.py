"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. complexity : O(1)

	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0

	"""returns the key complexity : O(1) 

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value complexity : O(1) 

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child, complexity : O(1) 
	
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child, complexity : O(1) 

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent, complexity : O(1)  

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the height, complexity : O(1) 

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree, complexity : O(1) 

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key, complexity : O(1) 

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key=key
		return None


	"""sets value, complexity : O(1) 

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value=value
		return None


	"""sets left child, complexity : O(1) 

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node
		node.set_parent(self)
		return None


	"""sets right child, complexity : O(1) 

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node
		node.set_parent(self)
		return None


	"""sets parent, complexity : O(1) 

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node
		return None


	"""sets the height of the node, complexity : O(1) 

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height=h
		return None


	"""sets the size of node, complexity : O(1) 

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size = s
		return None


	"""returns whether self is not a virtual node , complexity : O(1) 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if(self.key!=None):
			return True
		return False

	"""returns the balance factor of the the node, complexity : O(1) 

	@rtype: int
	@returns: the BF of the the node
	"""
	def get_BF(self):
		return self.left.get_height() - self.right.get_height()

	"""returns whether self is left child, complexity : O(1) 

	@rtype: bool
	@returns: True if self is a left child, False otherwise.
	"""
	def is_left_child(self):
		if(self.get_parent().get_key()>self.get_key()):
			return True
		return False



"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields. complexity : O(1)

	"""
	def __init__(self):
		self.root = None
		# add your fields here



	"""searches for a value in the dictionary corresponding to the key,
	   complexity : O(log(n)) 

	@type key: int
	@param key: a key to be searched
	@rtype: any
	@returns: the value corresponding to key.
	"""
	def search(self, key):
		currentnode = self.root
		while(currentnode.get_key() != None):
			if(currentnode.get_key()==key):
				return currentnode

			elif(currentnode.get_key() > key): #requested key is smaller than currentkey
				currentnode = currentnode.get_left()

			elif(currentnode.get_key() < key): #requested key is larger than currentkey
				currentnode = currentnode.get_right()
		return None



	"""inserts val at position i in the dictionary
	   complexity : O(log(n))  

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		if (self.root == None):
			self.root = AVLNode(key, val)
			self.root.set_left(AVLNode(None, None))
			self.root.set_right(AVLNode(None, None))
			self.root.set_height(0)
			self.root.set_size(1)
			return 0

		currentnode = self.inserting_node(key,val)
		parentnode = currentnode.get_parent()
		cnt_balance_operations = 0
		while(parentnode != None):
			prevParentHeight = parentnode.get_height()
			parentnode.set_height(1 + max(parentnode.get_left().get_height(), parentnode.get_right().get_height()))
			parent_BF = parentnode.get_BF()
			if (abs(parent_BF) < 2 and prevParentHeight == parentnode.get_height()):
				break
			elif (abs(parent_BF) < 2 and prevParentHeight != parentnode.get_height()):
				parentnode = parentnode.get_parent()
				cnt_balance_operations+=1
			else:
				cnt_balance_operations += self.balance_operations(parentnode,True,parent_BF)

		return cnt_balance_operations



	"""deletes node from the dictionary
	   complexity : O(log(n)) 

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		if(node==None):
			return None
		node = self.delete_BST(node)
		parentnode = node
		cnt_balance_operations = 0
		while (parentnode != None):
			prevParentHeight = parentnode.get_height()
			parentnode.set_height(1 + max(parentnode.get_left().get_height(), parentnode.get_right().get_height()))
			parentnode.set_size(parentnode.get_left().get_size() + parentnode.get_right().get_size()+1)
			parent_BF = parentnode.get_BF()
			if (abs(parent_BF) < 2 and prevParentHeight == parentnode.get_height()):
				parentnode = parentnode.get_parent()
			elif (abs(parent_BF) < 2 and prevParentHeight != parentnode.get_height()):
				parentnode = parentnode.get_parent()
			else:
				tmpparent = parentnode.get_parent()
				cnt_balance_operations += self.balance_operations(parentnode, True, parent_BF)
				parentnode = tmpparent

		return cnt_balance_operations


	"""returns an array representing dictionary 
	   complexity : O(n) 
	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return self.tree_inorder(self.root)


	"""returns the number of items in dictionary
	   complexity : O(1) 
	
	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()	

	"""splits the dictionary at a given node
	   complexity : O(log(n)) 

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""

	def split(self, node):
		if(node==None):
			return [self,AVLTree()]
		T1 = AVLTree()
		T2 = AVLTree()
		tree = AVLTree()
		if(node==self.root):
			T1.root = self.root.get_left()
			T1.root.set_parent(None)
			T2.root = self.root.get_right()
			T2.root.set_parent(None)
		elif (node == self.get_min()):
			self.delete(node)
			T1 = AVLTree()
			T2 = self
		elif (node == self.get_max()):
			self.delete(node)
			T1 = self
			T2 = AVLTree()
		else:
			if (node.get_right().get_key() != None):
				T2.root = node.get_right()
			if (node.get_left().get_key() != None):
				T1.root = node.get_left()
			prevParentkey = node.get_key()
			parentNode = node.get_parent()
			while (parentNode != None):
				if (prevParentkey < parentNode.get_key()):
					tree.root=T2.root
					T2.root = parentNode.get_right()
					T2.root.set_parent(None)
					tree.join(T2, parentNode.get_key(), parentNode.get_value())
					T2.root = tree.root

				else:
					tree.root = parentNode.get_left()
					tree.root.set_parent(None)
					T1.join(tree, parentNode.get_key(), parentNode.get_value())
					tree.root=None


				prevParentkey = parentNode.get_key()
				parentNode = parentNode.get_parent()
		if(T1.root !=None):
			T1.root.set_parent(None)
		if (T2.root != None):
			T2.root.set_parent(None)
		return [T1, T2]

	"""joins self with key and another AVLTree
	   complexity : O(log(n)) 

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

	def join(self, tree, key, val):
		if (self.root == None or tree.root == None):
			return self.join_empty_tree(tree, key, val)
		if(self.root.get_key()==None or tree.root.get_key()==None):
			return self.join_empty_tree(tree,key,val)
		else:
			# replace between trees such that self keys be always the smallest than tree
			if (self.get_root().get_key() > tree.get_root().get_key()):
				tmp = self.get_root()
				self.root = tree.get_root()
				tree.root = tmp

			cost = self.get_root().get_height() - tree.get_root().get_height()
			x = AVLNode(key, val)
			if(cost==0):
				x.set_right(tree.get_root())
				x.set_left(self.get_root())
				self.root = x
				self.root.set_height(1 + max(self.get_root().get_left().get_height(), self.get_root().get_right().get_height()))
				self.root.set_size(self.get_root().get_left().get_size() + self.get_root().get_right().get_size() + 1)
				return abs(cost) + 1

			if(cost>0):
				a = self.find_a(tree.root.get_height())
				b=tree.root
				c= a.get_parent()
				x.set_left(a)
				x.set_right(b)
				x.set_height(1 + max(x.get_left().get_height(), x.get_right().get_height()))
				x.set_size(x.get_left().get_size() + x.get_right().get_size() + 1)
				c.set_right(x)

			if(cost<0):
				b = tree.find_b(self.root.get_height())
				a=self.root
				c= b.get_parent()
				x.set_left(a)
				x.set_right(b)
				x.set_height(1 + max(x.get_left().get_height(), x.get_right().get_height()))
				x.set_size(x.get_left().get_size() + x.get_right().get_size() + 1)
				c.set_left(x)
				self.root = tree.get_root()

			parentnode = c

			while (parentnode != None):
				prevParentHeight = parentnode.get_height()
				parentnode.set_height(1 + max(parentnode.get_left().get_height(), parentnode.get_right().get_height()))
				parentnode.set_size(parentnode.get_left().get_size() + parentnode.get_right().get_size() + 1)
				parent_BF = parentnode.get_BF()
				if (abs(parent_BF) < 2 and prevParentHeight == parentnode.get_height()):
					parentnode = parentnode.get_parent()
				elif (abs(parent_BF) < 2 and prevParentHeight != parentnode.get_height()):
					parentnode = parentnode.get_parent()
				else:
					parentnode = self.balance_operations(parentnode, False, parent_BF)
					

			return abs(cost) + 1


	"""compute the rank of node in the self
	   complexity : O(log(n))   

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		cnt = 1
		currentnode = self.root
		while (currentnode.get_key() !=node.get_key()):
			if(currentnode.get_key()>=node.get_key()):
				currentnode =currentnode.get_left()
			else:
				cnt += currentnode.get_left().get_size()+1
				currentnode = currentnode.get_right()
		return currentnode.get_left().get_size()+cnt


	"""finds the i'th smallest item (according to keys) in self
	   complexity : O(log(n))

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		if(i==1):
			return self.get_min()
		currentNode = self.root
		while(i>0):
			lefttreesize = currentNode.get_left().get_size()
			if(lefttreesize<i):
				i-=lefttreesize+1
				if(i!=0):
					currentNode = currentNode.get_right()
			else:
				currentNode=currentNode.get_left()
		return currentNode





	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root



	'extra methods'

	"""making Left Rotation if the root BF equal to 2 and the left son is equal to 1
	   complexity : O(1)
	   
	    @rtype: AVLNode
	    @returns: the current root of the SubTree after the rotation
	    """
	def left_rotation(self,root):
		right = root.get_right()
		left_right_tree = right.get_left()
		right.set_left(root)
		root.set_right(left_right_tree)
		root.set_height(1 + max(root.get_right().get_height(),root.get_left().get_height()))
		root.set_size(root.get_right().get_size() + root.get_left().get_size()+1)
		right.set_height(1 + max(right.get_right().get_height(), right.get_left().get_height()))
		right.set_size(right.get_right().get_size() + right.get_left().get_size()+1)
		right.set_parent(None)
		return right

	"""making Right Rotation if the root BF equal to 2 and the left son is equal to 1
       complexity : O(1)
       
    @rtype: int
    @returns: the number of balancing operations
    """

	def right_rotation(self,root):
		left = root.get_left()
		rightLeftTree = left.get_right()
		left.set_right(root)
		root.set_left(rightLeftTree)
		root.set_height(1 + max(root.get_right().get_height(),root.get_left().get_height()))
		left.set_height(1 + max(left.get_right().get_height(), left.get_left().get_height()))
		root.set_size(root.get_right().get_size() + root.get_left().get_size() + 1)
		left.set_size(left.get_right().get_size() + left.get_left().get_size() + 1)
		left.set_parent(None)
		return left

	"""insert new Node to the Tree without balance
	   complexity : O(log(n))

	@rtype: int
	@returns: the number of balancing operations
	"""
	def inserting_node(self, key,val):
		currentnode = self.root
		while (currentnode.get_key() != None):
			currentnode.set_size(currentnode.get_size() + 1)
			if (currentnode.get_key() > key):  # requested key is smaller than currentkey
				currentnode = currentnode.get_left()

			elif (currentnode.get_key() < key):  # requested key is larger than currentkey
				currentnode = currentnode.get_right()

		currentnode.set_key(key)
		currentnode.set_value(val)
		currentnode.set_left(AVLNode(None, None))
		currentnode.set_right(AVLNode(None, None))
		currentnode.set_height(0)
		currentnode.set_size(1)

		return currentnode

	"""Return True if node is root of the tree else return False
	   complexity : O(1)

	@rtype: bool
	@returns: True if node is root of the tree else return False
	"""
	def is_node_root(self,node):
		return self.root.get_key() == node.get_key()

	"""Performs the required rotations of SubTree given the parent BF of the node
	   complexity : O(1)

	@rtype: AVLNode or int
	@returns: the parent node of the Subtree or the number of the balance operations
	"""
	def balance_operations(self, node,method_flag,parent_BF):
		cnt_balance_operations=0
		if (parent_BF == 2):
			if (node.get_left().get_BF() == -1):  # we are in the (2,-1) case therefore first we rotate left.
				node.set_left(self.left_rotation(node.get_left()))
				cnt_balance_operations += 1
			if (self.is_node_root(node)):  # either way we rotate right
				self.root = self.right_rotation(node)
			elif (node.get_parent().get_key() > node.get_key()):
				node.get_parent().set_left(self.right_rotation(node))
			else:
				node.get_parent().set_right(self.right_rotation(node))
			cnt_balance_operations = 1 + cnt_balance_operations

		elif (parent_BF == -2):
			if (node.get_right().get_BF() == 1):  # we are in the (-2,1) case therefore first we rotate right.
				node.set_right(self.right_rotation(node.get_right()))
				cnt_balance_operations += 1
			if (self.is_node_root(node)):
				self.root = self.left_rotation(node)
			elif (node.get_parent().get_key() > node.get_key()):
				node.get_parent().set_left(self.left_rotation(node))
			else:
				node.get_parent().set_right(self.left_rotation(node))
			cnt_balance_operations = 1 + cnt_balance_operations
		if (method_flag):
			return cnt_balance_operations
		else:
			return node

	"""Binary search Tree deleting Node
	   complexity : O(log(n))

	@rtype: AVLNode or None
	@returns: the parent node of the deleted node
	"""
	def delete_BST(self,node):
		if(not node.is_real_node()):
			return None

		virtualNode =AVLNode(None,None)

		#Case 1: node is leaf
		if(not node.get_left().is_real_node() and not node.get_right().is_real_node()):
			if(self.root == node):
				self.root = AVLNode(None,None)
				return None
			parentnode = node.get_parent()
			if(parentnode.get_left() == node):
				parentnode.set_left(virtualNode)
			else:
				parentnode.set_right(virtualNode)
			return parentnode

		#Case 2.1: have only right son
		if(not node.get_left().is_real_node() and node.get_right().is_real_node()):
			if(self.root == node):
				self.root = node.get_right()
				self.root.set_parent(None)
				return None
			parentnode = node.get_parent()
			if (parentnode.get_left() == node):
				parentnode.set_left(node.get_right())
			else:
				parentnode.set_right(node.get_right())
			return parentnode

		# Case 2.2: have only left son
		if(node.get_left().is_real_node() and not node.get_right().is_real_node()):
			if(self.root == node):
				self.root = node.get_left()
				self.root.set_parent(None)
				return None
			parentnode = node.get_parent()
			if (parentnode.get_left() == node):
				parentnode.set_left(node.get_left())
			else:
				parentnode.set_right(node.get_left())
			return parentnode

		#case 3: have two children
		else:
			succesornode = self.successor(node)
			tempkey= node.get_key()
			tempval =node.get_value()
			node.set_key(succesornode.get_key())
			node.set_value(succesornode.get_value())
			succesornode.set_key(tempkey)
			succesornode.set_value(tempval)
			self.delete(succesornode)
			return node.get_parent()

	"""Searching and return the successor of the given node 
	   complexity : O(log(n))

	@rtype: AVLNode
	@returns: the successor of the given node
	"""
	def successor(self,node):
		if(node.get_right().get_key()!=None):
			currentnode = node.get_right()
			while(currentnode.get_left().get_key() != None):
				currentnode = currentnode.get_left()
			return currentnode
		else:
			currentnode = node
			while(currentnode.get_key() > currentnode.get_parent().get_key()):
				currentnode = currentnode.get_parent()
			return currentnode.get_parent()

	"""Recursion Function the order the key of the Tree in array
	   complexity : O(n)

	@rtype: array
	@returns: A sorted array of the keys
	"""
	def tree_inorder(self,root):
		if(root==None or root.get_key()==None):
			return []
		leftside = self.tree_inorder(root.get_left())
		rightside = self.tree_inorder(root.get_right())
		return leftside+[(root.get_key(),root.get_value())]+rightside

	"""Join two AVLTree that at least one of them is empty tree
	   complexity : O(log(n))

	@rtype: AVLTree()
	@returns: the AVLTree after joining
	"""
	def join_empty_tree(self,tree,key,val):
		if(self.root == None and tree.get_root() == None):
			self.insert(key,val)
			return 1
		elif (tree.root == None):
			cost = self.root.get_height()
			self.insert(key, val)
			return cost
		elif (self.root == None):
			cost = tree.root.get_height()
			tree.insert(key, val)
			self.root = tree.root
			return cost
		elif(self.root.get_key() == None and tree.get_root().get_key() == None):
			self.insert(key,val)
			return 1
		elif(tree.root.get_key() == None):
			cost = self.root.get_height()
			self.insert(key,val)
			return cost

		else:
			cost = tree.root.get_height()
			tree.insert(key,val)
			self.root=tree.root
			return cost

	"""Finding the maximum key at the given height
	   complexity : O(log(n))

	@rtype: AVLNode
	@returns: Node with the maximum key at the given height
	"""
	def find_a(self,height):
		a = self.get_root()
		while (a.get_height() > height):
			a = a.get_right()

		return a

	"""Finding the minimum key at the given height
	   complexity : O(log(n))

	@rtype: AVLNode
	@returns: Node with the minimum key at the given height
	"""
	def find_b(self,height):
		b = self.get_root()
		while (b.get_height() > height):
			b = b.get_left()

		return b

	"""Return the node with minimum key
	   complexity : O(log(n))

	@rtype: AVLNode
	@returns: the node with minimum key
	"""
	def get_min(self):
		currentNode = self.root
		while(currentNode.get_left().get_key() != None):
			currentNode= currentNode.get_left()
		return currentNode

	"""Return the node with maximum key
	   complexity : O(log(n))

	@rtype: AVLNode
	@returns: the node with maximum key
	"""
	def get_max(self):
		currentNode = self.root
		while(currentNode.get_right().get_key() != None):
			currentNode= currentNode.get_right()
		return currentNode