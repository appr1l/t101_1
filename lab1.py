#! /home/crsnx/Desktop/t1o1/t101_1/.venv/bin/python3
import generate_and_evaluate as ge

def executor(rules):
    """Removes conflicting rules.

    Keyword arguments:
	rules (list of dict): dictionary of rules
    """
    pass

def reshala(rules, facts):
    """Summary
    
    Args:
        rules (list of dict): dictionary of rules
        facts (list): list of facts
    
    Returns:
        list: knowledge base
    """
    def _and(rule_list, facts_list):
    	pass
    def _not(rule_list, facts_list):
    	pass
    def _or(rule_list, facts_list):
    	pass
    for rule in rules:
    	operator = list(rule.get('if'))[0] # забираем логический ключ операции
    	if operator == 'and':
    		pass
    	if operator == 'not':
    		pass
    	if operator == 'or':
    		pass



def main():
	rules = ge.generate_simple_rules(100,4,10)
	facts = ge.generate_rand_facts(100,10)
	#print(len(rules))
	print(list(rules[0].get('if').keys())[0])
	print(rules[0].get('if').values())
	print(rules[0].get('then'))
	print(facts)

if __name__=='__main__':
	main()