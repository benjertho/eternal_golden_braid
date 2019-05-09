# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:12:32 2019

@author: thompson
"""
from treelib import Tree

def checkString(s):
    return (s == 'MU')

def rule1(tree, node, count):
    if (tree[node].tag[-1] == 'I'):
        count += 1
        string = tree[node].tag + 'U'
        tree.create_node(string, count, parent=tree[node].identifier)
        return [checkString(string), count]
    return [False, count]

def rule2(tree, node, count):
    count += 1
    string = tree[node].tag + tree[node].tag[1:]
    tree.create_node(string, count, parent=tree[node].identifier)
    return [checkString(string), count]

def rule3(tree, node, count):
    for i in range(len(tree[node].tag) - 2):
        if (tree[node].tag[i] == 'I' and tree[node].tag[i+1] == 'I' and tree[node].tag[i+2] == 'I'):
            count += 1
            string = tree[node].tag[:i] + 'U' + tree[node].tag[i+3:]
            tree.create_node(string, count, parent=tree[node].identifier)
            if checkString(string):
                return [True, count]
    return [False, count]

def rule4(tree, node, count):
    for i in range(len(tree[node].tag) - 1):
        if (tree[node].tag[i] == 'U' and tree[node].tag[i+1] == 'U'):
            count += 1
            string = tree[node].tag[:i] + tree[node].tag[i+2:]
            tree.create_node(string, count, parent=tree[node].identifier)
            if checkString(string):
                return [True, count]
    return [False, count]

def buildTree(tree):
    current_node = 0
    node_count = 1
    limit = 1000
    
    while node_count < limit:
        #node = tree.get_node(current_node)

        [found, node_count] = rule1(tree, current_node, node_count)
        if found:
            break
        [found, node_count] = rule2(tree, current_node, node_count)
        if found:
            break
        [found, node_count] = rule3(tree, current_node, node_count)
        if found:
            break
        [found, node_count] = rule4(tree, current_node, node_count)
        if found:
            break
        
        current_node += 1
        
    if node_count < limit:
        print("Found!")
    else:
        print("Failed")
        
        
    
tree = Tree()
tree.create_node("MI", 0)
buildTree(tree)

