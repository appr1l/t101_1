#! /home/crsnx/Desktop/t1o1/t101_1/.venv/bin/python3
"""1 лабораторка.
"""

#from time import time
import generate_and_evaluate as ge


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


def main():
    """Main
    """
    #time_start = time()
    rules = ge.generate_simple_rules(100, 4, 10)
    facts = ge.generate_rand_facts(100, 100)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(len(facts_dict))
    reshala(rules_list, facts_dict)
    print(len(facts_dict))

if __name__ == '__main__':
    main()
