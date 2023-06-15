#!/usr/bin/python3
def best_score(a_dictionary):
      if not a_dictionary:
            return None
      max_k = None
      max_v = float('-inf')

      for key, value in a_dictionary.items():
            if isinstance(value, int) and value > max_v:
                  max_k = key
                  max_v = value

      return max_k
