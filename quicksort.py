quicksort = lambda l: l if len(l) == 0 else
quicksort(list(filter(lambda _: _ < l[0], l)))
+  list(filter(lambda _: _ == l[0], l))
+ quicksort(list(filter(lambda _: _ > l[0], l)))
