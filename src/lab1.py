#! /home/crsnx/Desktop/t1o1/t101_1/.venv/bin/python3
"""1 лабораторка.
"""

import functools
import time
import generate_and_evaluate as ge

def timer(func):
    """Таймер выполнения фунцкии
        Args:
            func (func): Фунция, которую мерим
         Returns:
            String: Строка с временем выполнения
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

def update_rules(rules):
    """Removes conflicting rules.
        Args:
            rules (dictionary): Словарь правил
        Returns:
            List of rules: Список правил(or,and,not)
    """
    rules_not = []
    rules_or = []
    rules_and = []
    for rule in rules:
        if rule.get('if').get('and') is not None:
            rules_and.extend([[rule.get('if').get('and'), rule.get('then')]])
        if rule.get('if').get('or') is not None:
            rules_or.extend([[rule.get('if').get('or'), rule.get('then')]])
        if rule.get('if').get('not') is not None:
            rules_not.extend([[rule.get('if').get('not'), rule.get('then')]])
    return [rules_or, rules_and, rules_not]

def update_facts(facts):
    """Summary
        Args:
            facts (list): Список фактов
        Returns:
            dict: Словарь фактов
    """
    facts_dict = {}
    for fact in facts:
        if facts_dict.get(fact) is None:
            facts_dict[fact] = True
    return facts_dict

@timer
def reshala(rules_list, facts_dict):
    """Summary
        Args:
            rules (list of dict): dictionary of rules
            facts (list): list of facts
        Returns:
            list: knowledge base
    """
    for rule in rules_list[0]:
        #Обработка or
        for ifor in rule[0]:
            if facts_dict.get(ifor) is True:
                if facts_dict.get(rule[1]) is None:
                    #Чтобы не было одних и тех же, проверяем наличие нового факта
                    facts_dict[rule[1]] = True

    for rule in rules_list[1]:
        #Обработка and
        for ifand in rule[0]:
            if facts_dict.get(ifand) is None:
                #Поняли, что нет факта из and-вышли из этого правила
                break
            if facts_dict.get(rule[1]) is None:
                facts_dict[rule[1]] = True

    for rule in rules_list[2]:
        #Обработка not
        for ifnot in rule[0]:
            if facts_dict.get(ifnot) is True:
                break
            if facts_dict.get(rule[1]) is None:
                facts_dict[rule[1]] = True
    return ''


def main():
    """Main
    """
    #SIMP RULES RAND FACTS
    rules = ge.generate_simple_rules(10000, 10, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{reshala(rules_list, facts_dict)} SIMP RULES RAND FACTS')
    #STAIRWAY RULES, RAND FACTS
    rules = ge.generate_stairway_rules(10000, 10, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{reshala(rules_list, facts_dict)} STAIRWAY RULES RAND FACTS')
    #RING RULES, RAND FACTS
    rules = ge.generate_ring_rules(10000, 10, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{reshala(rules_list, facts_dict)} RING RULES RAND FACTS')
    #RANDOM RULES, RAND FACTS
    rules = ge.generate_random_rules(10000, 10, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{reshala(rules_list, facts_dict)} RAND RULES RAND FACTS')

if __name__ == '__main__':
    main()
