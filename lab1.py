#! /home/crsnx/Desktop/t1o1/t101_1/.venv/bin/python3
import generate_and_evaluate as ge
from time import time

def executor(rules):
    """Removes conflicting rules.

    Keyword arguments:
	rules (list of dict): dictionary of rules
    """
    # 1. если условия совпадают на разных/тех же опператорах
    for rule in reversed(rules):
        for ind_rule in range(len(rules)-1):
            if rule['if'].values():
                pass


def reshala(rules, facts):
    """Summary
    
    Args:
        rules (list of dict): dictionary of rules
        facts (list): list of facts
    
    Returns:
        list: knowledge base
    """
    result_list = []

    def _and(rule_list, facts_list):
    	for rule in rule_list:
    		checker = False # маркер
    		for fact in facts_list:
    			if rule == fact:
    				checker = True  # нашли - тру
    		if checker == False:
    			return False
    	return True

    def _not(rule_list, facts_list):
    	for rule in rule_list:
    		for fact in facts_list:
    			if rule == fact:
    				#print(f'{rule}\t{fact}')
    				return False  # нашли ne - false	
    	return True

    def _or(rule_list, facts_list):
    	for rule in rule_list:
    		for fact in facts_list:
    			if rule == fact:
    				return True  # нашли or - true
    	return False
    	

    for rule in rules:
    	#print(rule.get('then'))
    	rule_list = list(rule.get('if').values())[0] # забираем список значений
    	if 'and' in rule.get('if'):
    		if _and(rule_list, facts): # дохуярить list values
    			result_list.append(rule.get('then'))
    	if 'not' in rule.get('if'):
    		if _not(rule_list, facts): # дохуярить list values
    			result_list.append(rule.get('then'))
    	if 'or' in rule.get('if'):
    		if _or(rule_list, facts): # дохуярить list values
    			result_list.append(rule.get('then'))

    return result_list


def main():
	#time_start = time()
    rules = ge.generate_simple_rules(100,4,10)
    facts = ge.generate_rand_facts(100,100000)
    print(sorted(list(rules[0]['if'].values())[0]) == sorted(list(rules[0]['if'].values())[0]) )
    #print(facts)
    print(reshala(rules,facts))
    
if __name__=='__main__':
	main()