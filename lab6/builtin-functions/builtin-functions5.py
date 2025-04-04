def all_elements_true(tpl):
    return all(tpl)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (1, "Hello", 5)
tuple4 = (0, "", None)

print(all_elements_true(tuple1))
print(all_elements_true(tuple2))
print(all_elements_true(tuple3))
print(all_elements_true(tuple4))